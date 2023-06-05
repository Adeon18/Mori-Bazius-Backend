CREATE KEYSPACE hunters WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 3};

USE hunters;


// Stores up-to-date stats per player: GAME_LOGIC
CREATE TABLE player_stats_by_player_id (
    player_id int,
    player_name text,
    level int,
    power int,
    exp int,
    hunters int,
    masters int,
    PRIMARY KEY (player_id, power)
) WITH CLUSTERING ORDER BY (power DESC);


// Stores up-to-data resources per player: GAME_LOGIC!
CREATE TABLE game_data_by_player_id (
    player_id int,
    player_name text,

    // Utils
    monster_bone int,
    leather_scraps int,
    oil int,

    // Armor
    armor int,
    mastercrafted_armor int,

    // Swords
    silver_sword int,
    kingslayers_silver_sword int,
    steel_sword int,
    kingslayers_steel_sword int,

    // diamonds
    diamond_dust int,
    diamond int,

    // ingots
    dark_steel_ingot int,
    meteorite_silver_ingot int,
    green_gold_ingot int,

    // potions
    swallow_potion int,

    // Ores
    dark_steel_ore int,
    meteorite_silver_ore int,
    green_gold_ore int,

    // herbs
    arenaria int,
    nostrix int,
    wolfsbane int,

    PRIMARY KEY(player_id)
);


// Stores all the stats save requests by time(with precision to minutes) and player id as logs: GAME_ANALISYS_DATA
CREATE TABLE player_stats_by_player_id_and_time_logs (
    player_id int,
    time text,
    player_name text,
    level int,
    power int,
    exp int,
    hunters int,
    masters int,
    PRIMARY KEY (player_id, time)
);


// Stores all the resource save requests by time(with precision to minutes) and player id as logs: GAME_ANALISYS_DATA
CREATE TABLE game_data_by_player_id_and_time_logs (
    player_id int,
    time text,
    player_name text,

    // Utils
    monster_bone int,
    leather_scraps int,
    oil int,

    // Armor
    armor int,
    mastercrafted_armor int,

    // Swords
    silver_sword int,
    kingslayers_silver_sword int,
    steel_sword int,
    kingslayers_steel_sword int,

    // diamonds
    diamond_dust int,
    diamond int,

    // ingots
    dark_steel_ingot int,
    meteorite_silver_ingot int,
    green_gold_ingot int,

    // potions
    swallow_potion int,

    // Ores
    dark_steel_ore int,
    meteorite_silver_ore int,
    green_gold_ore int,

    // herbs
    arenaria int,
    nostrix int,
    wolfsbane int,

    PRIMARY KEY(player_id, time)
);

CREATE TABLE hunters.average_growth_by_player_id (
    player_id INT PRIMARY KEY,
    avg_growth_monster_bone DOUBLE,
    avg_growth_leather_scraps DOUBLE,
    avg_growth_oil DOUBLE,
    avg_growth_armor DOUBLE,
    avg_growth_mastercrafted_armor DOUBLE,
    avg_growth_silver_sword DOUBLE,
    avg_growth_kingslayers_silver_sword DOUBLE,
    avg_growth_steel_sword DOUBLE,
    avg_growth_kingslayers_steel_sword DOUBLE,
    avg_growth_diamond_dust DOUBLE,
    avg_growth_diamond DOUBLE,
    avg_growth_dark_steel_ingot DOUBLE,
    avg_growth_meteorite_silver_ingot DOUBLE,
    avg_growth_green_gold_ingot DOUBLE,
    avg_growth_swallow_potion DOUBLE,
    avg_growth_dark_steel_ore DOUBLE,
    avg_growth_meteorite_silver_ore DOUBLE,
    avg_growth_green_gold_ore DOUBLE,
    avg_growth_arenaria DOUBLE,
    avg_growth_nostrix DOUBLE,
    avg_growth_wolfsbane DOUBLE
);