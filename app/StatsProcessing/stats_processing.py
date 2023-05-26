import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, lag
from pyspark.sql.window import Window


spark = SparkSession.builder\
    .appName("CassandraTableReader") \
    .config("spark.cassandra.connection.host","cassandra-node-1")\
    .config("spark.cassandra.connection.port","9042")\
    .getOrCreate()

def hourly_job():
    df = spark.read\
    .format("org.apache.spark.sql.cassandra")\
    .options(table="game_data_by_player_id_and_time_logs", keyspace="hunters")\
    .load()
    
    # Calculate average growth for each column
    columns = [
        "monster_bone", "leather_scraps", "oil",
        "armor", "mastercrafted_armor",
        "silver_sword", "kingslayers_silver_sword",
        "steel_sword", "kingslayers_steel_sword",
        "diamond_dust", "diamond",
        "dark_steel_ingot", "meteorite_silver_ingot", "green_gold_ingot",
        "swallow_potion",
        "dark_steel_ore", "meteorite_silver_ore", "green_gold_ore",
        "arenaria", "nostrix", "wolfsbane"
    ]

    growth_df = df.withColumn("previous_player_id", lag("player_id").over(Window.orderBy("time")))

    for column in columns:
        growth_column = "growth_" + column
        growth_df = growth_df.withColumn(growth_column, col(column) - lag(col(column)).over(Window.partitionBy("player_id").orderBy("time")))

    growth_df = growth_df.filter(growth_df.previous_player_id.isNotNull()).drop("previous_player_id")
    
    avg_growth_df = growth_df.groupBy("player_id").agg(*[avg(col).alias("avg_" + col) for col in growth_df.columns if col.startswith("growth_")])
    # Write avg_growth_df to Cassandra table, replacing old values
    avg_growth_df.write\
        .format("org.apache.spark.sql.cassandra")\
        .options(table="average_growth_by_player_id", keyspace="hunters")\
        .mode("overwrite")\
        .option("confirm.truncate", "true")\
        .save()


while True:
    hourly_job()

    # Sleep for 1 minute
    time.sleep(60)

    # # Sleep for 1 hour
    # time.sleep(3600)

spark.stop()