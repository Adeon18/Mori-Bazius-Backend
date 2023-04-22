# API Gateway Service

Service that accepts information from the game and further passes it onto the other services.
"Lives" on port `9000`.

## Usage


**GET** the top `limit` most powerful players by power.
```
localhost:9000/game_data/leagueboard?limit=<limit>
```

</br>

**GET** player stats by player_id - works with `game_data_service`.
```
localhost:9000/game_data/stats?player_id=<player_id>
```

</br>

**POST** player stats by player_id - works with `game_data_service`.
```
localhost:9000/game_data/stats?player_id=<player_id>
```
Example body of the request:
```json
{
    "power": 0,
    "level": 0,
    "hunters": 0,
    "masters": 0,
    "exp": 0
}
```

</br>

**GET** player resources by player_id - works with `game_data_service`.
```
localhost:9000/game_data/resources?player_id=<player_id>
```

</br>

**POST** player resources by player_id - works with `game_data_service`.
```
localhost:9000/game_data/resources?player_id=<player_id>
```
Example body of request:
```json
{
    "arenaria": 0,
    "nostrix": 0,
    "wolfsbane": 0,
    "swallow_potion": 0,
    "meteorite_silver_ore": 0,
    "dark_steel_ore": 0,
    "green_gold_ore": 0,
    "meteorite_silver_ingot": 0,
    "dark_steel_ingot": 0,
    "green_gold_ingot": 0,
    "diamond_dust": 0,
    "diamond": 0,
    "monster_bone": 0,
    "leather_scraps": 0,
    "oil": 0,
    "armor": 0,
    "mastercrafted_armor": 0,
    "steel_sword": 0,
    "kingslayers_steel_sword": 0,
    "silver_sword": 0,
    "kingslayers_silver_sword": 0
}
```