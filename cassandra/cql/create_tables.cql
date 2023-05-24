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


// Stores all the stats save requests by time(with precision to seconds) and player id as logs: GAME_ANALISYS_DATA
CREATE TABLE player_stats_by_time_logs (
    time text,
    player_id int,
    player_name text,
    level int,
    power int,
    exp int,
    hunters int,
    masters int,
    PRIMARY KEY (text, player_id)
);


// Stores all the resource save requests by time(with precision to seconds) and player id as logs: GAME_ANALISYS_DATA
CREATE TABLE game_data_by_time_logs (
    time text,
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

    PRIMARY KEY(time, player_id)
);

