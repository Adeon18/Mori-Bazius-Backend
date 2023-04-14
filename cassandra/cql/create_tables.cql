CREATE KEYSPACE hunters WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 3};

USE hunters;

CREATE TABLE player_stats_by_player_id (
    player_id int,
    level int,
    power int,
    wins int,
    loses int,
    win_rate_percent int,
    total_upgr int,
    upgr_0 int,
    upgr_1 int,
    upgr_2 int,
    upgr_3 int,
    PRIMARY KEY (player_id, power)
);

CREATE TABLE game_data_by_player_id (
    player_id int,

    // Utils
    monster_bone int,
    leather_scrap int,
    oil int,

    // Armor
    armor int,
    mastercrafted_armor int,

    // Swords
    silver_sword int,
    silver_kingslayers_sword int,
    steel_sword int,
    steel_kingslayers_sword int,

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

    // mosters
    brook int,
    kikimora int,
    wyvern int,

    // herbs
    arenaria int,
    nostrix int,
    wolfsbane int,

    PRIMARY KEY(player_id)
);

