# Snapshot Service

Service, that approximately every 2 minutes, reads all the players' resourec data and stats and snapshots
it with specifying the minute and saves that data to the `player_stats_by_player_id_and_time_logs` and
`game_data_by_player_id_and_time_logs` tables in cassandra for further **stat batch processing analisys**.
Also can return the entries for a specific `player_id` from logs for the last `N` minutes.
Lives on port `9010`.

## Usage

### Pulling the resource logs

**GET** the **game resource** logs for the player_id `X` for the last `N` minutes:
```
localhost:9010/logged_resources?player_id=<X>&last_minutes=<N>
```

Example of the response for `localhost:9010/logged_resources?player_id=3&last_minutes=5`:

```json
[
    {"player_id":3,"time":"2023-05-24-18-17","arenaria":0,"armor":0,"dark_steel_ingot":0,"dark_steel_ore":0,"diamond":0,"diamond_dust":0,"green_gold_ingot":0,"green_gold_ore":0,"kingslayers_silver_sword":0,"kingslayers_steel_sword":0,"leather_scraps":0,"mastercrafted_armor":0,"meteorite_silver_ingot":0,"meteorite_silver_ore":0,"monster_bone":0,"nostrix":0,"oil":0,"player_name":null,"silver_sword":0,"steel_sword":0,"swallow_potion":0,"wolfsbane":0},{"player_id":3,"time":"2023-05-24-18-18","arenaria":0,"armor":0,"dark_steel_ingot":0,"dark_steel_ore":0,"diamond":0,"diamond_dust":0,"green_gold_ingot":0,"green_gold_ore":0,"kingslayers_silver_sword":0,"kingslayers_steel_sword":0,"leather_scraps":0,"mastercrafted_armor":0,"meteorite_silver_ingot":0,"meteorite_silver_ore":0,"monster_bone":0,"nostrix":0,"oil":0,"player_name":null,"silver_sword":0,"steel_sword":0,"swallow_potion":0,"wolfsbane":0},{"player_id":3,"time":"2023-05-24-18-20","arenaria":0,"armor":0,"dark_steel_ingot":0,"dark_steel_ore":0,"diamond":0,"diamond_dust":0,"green_gold_ingot":0,"green_gold_ore":0,"kingslayers_silver_sword":0,"kingslayers_steel_sword":0,"leather_scraps":0,"mastercrafted_armor":0,"meteorite_silver_ingot":0,"meteorite_silver_ore":0,"monster_bone":0,"nostrix":0,"oil":0,"player_name":null,"silver_sword":0,"steel_sword":0,"swallow_potion":0,"wolfsbane":0}
]
```

### Pulling the stats logs

**GET** the **game stats** logs for the player_id `X` for the last `N` minutes:
```
localhost:9010/logged_stats?player_id=<X>&last_minutes=<N>
```

Example of the response for `localhost:9010/logged_stats?player_id=3&last_minutes=50`:

```json
[
    {"player_id":3,"time":"2023-05-24-17-42","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-43","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-44","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-45","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-46","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-47","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-48","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-49","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-50","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-17-51","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-03","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-05","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-07","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-09","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-11","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-12","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-14","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-16","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-17","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-18","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-20","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-21","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125},{"player_id":3,"time":"2023-05-24-18-29","exp":0,"hunters":0,"level":0,"masters":0,"player_name":null,"power":125}
]
```