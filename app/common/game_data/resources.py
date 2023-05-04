from pydantic import BaseModel


class Resources(BaseModel):
    player_id: int | None = None
    token: str | None = None

    # Utils
    monster_bone: int | None = None
    leather_scraps: int | None = None
    oil: int | None = None

    # Armor
    armor: int | None = None
    mastercrafted_armor: int | None = None

    # Swords
    silver_sword: int | None = None
    kingslayers_silver_sword: int | None = None
    steel_sword: int | None = None
    kingslayers_steel_sword: int | None = None

    # Diamonds
    diamond_dust: int | None = None
    diamond: int | None = None

    # Ingots
    dark_steel_ingot: int | None = None
    meteorite_silver_ingot: int | None = None
    green_gold_ingot: int | None = None

    # Potions
    swallow_potion: int | None = None

    # Ores
    dark_steel_ore: int | None = None
    meteorite_silver_ore: int | None = None
    green_gold_ore: int | None = None

    # Herbs
    arenaria: int | None = None
    nostrix: int | None = None
    wolfsbane: int | None = None
