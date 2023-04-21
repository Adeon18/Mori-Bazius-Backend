# Game Data Service

Service for saving and getting player stats and resources for the game.

## Initialization

First, build the image using the `build.sh` script.

To run the container you should specify the endpoint and port for your Cassandra server. By default `CASSANDRA_ENDPOINT=cassandra-node-1` and `CASSANDRA_PORT=9042`.

```
CASSANDRA_ENDPOINT=<address> CASSANDRA_PORT=<port> ./run.sh
```

To stop the container use `stop.sh`

## Usage

There are several GET and POST requests that are supported now. For simplicity the address in the examples will be `localhost:8000`. You can use tools like **Postman** for testing purposes.

**GET** player stats by player_id
```
localhost:8000/stats?player_id=<player_id>
```

</br>

**POST** player stats by player_id
```
localhost:8000/stats?player_id=<player_id>
```
Example body of the request:
```json
{
    "level": 0,
    "power": 0,
    "wins": 0,
    "loses": 0,
    "win_rate_percent": 0,
    "total_upgr": 0,
    "upgr_0": 0,
    "upgr_1": 0,
    "upgr_2": 0,
    "upgr_3": 0
}
```

</br>

**GET** player resources by player_id
```
localhost:8000/resources?player_id=<player_id>
```

</br>

**POST** player resources by player_id
```
localhost:8000/resources?player_id=<player_id>
```
Example body of request:
```json
{
    "monster_bone": 0,
    "leather_scrap": 0,
    "oil": 0,
    "armor": 0,
    "mastercrafted_armor": 0,
    "silver_sword": 0,
    "silver_kingslayers_sword": 0,
    "steel_sword": 0,
    "steel_kingslayers_sword": 0,
    "diamond_dust": 0,
    "diamond": 0,
    "dark_steel_ingot": 0,
    "meteorite_silver_ingot": 0,
    "green_gold_ingot": 0,
    "swallow_potion": 0,
    "dark_steel_ore": 0,
    "meteorite_silver_ore": 0,
    "green_gold_ore": 0,
    "brook": 0,
    "kikimora": 0,
    "wyvern": 0,
    "arenaria": 0,
    "nostrix": 0,
    "wolfsbane": 0
}
```