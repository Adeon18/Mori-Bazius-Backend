# Guilds Service

Service that manages guilds logic. Operates on mongoDB, lives on port `6969`.

---

## Usage

### Searching
**GET** list of `limit` existing guilds:  
```
localhost:6969/guilds?limit=<limit>
```  
Returns dict of format:
```
{"guilds": [...list limit of guilds...]}
```
One guild representation example:   
```
{
    '_id': '647f0aabfc497f2074f9df00',
    'name': 'MyGuild',
    'description': 'Best guild ever',
    'num_members': 1,
    'limit_members': 20}]
}
```

<br>

**GET** list of members of a guild by its `gid`:
```
localhost:6969/members?gid=<gid>
```
Returns list of format:
```
[...members...]
```
One member representation example:
```
{
    '_id': ObjectId('647f0aabfc497f2074f9df01'),
    'gid': '647f0aabfc497f2074f9df00',
    'player_id': 2,
    'player_name':
    'alorthius'
}
```

<br>

**GET** guild info in which player with `player_id` participates:
```
localhost:6969/guild?player_id=<player_id>
```
Returns guild dict:
```
{
    "_id": "647f0aabfc497f2074f9df00",
    "name": "MyGuild",
    "description": "Best guild ever",
    "num_members": 2,
    "limit_members": 20
}
```

---

### Guild manipulations

**POST** a newly created guild:
```
localhost:6969/guilds/new
```
Request example:
```
{
    "name": "MyGuild",
    "description": "Best guild ever",
    "limit_members": 20,
    "player_id": 1,
    "player_name": "alorthius"
}
```
It creates a new guild and joins the player to it

<br>

**DELETE** existing guild with gid `gid` with all members:
```
localhost:6969/guilds/delete?gid=<gid>
```

---

### Members manipulations


**POST** new member of an existing guild:
```
localhost:6969/guilds/members/new
```
Request example:
```
{
    "gid": "647f0aabfc497f2074f9df00",
    "player_id": 1,
    "player_name": "alorthius"
}
```
Increases the number of members of a guild

<br>

**DELETE** existing member of an existing guild:
```
localhost:6969/guilds/leave?gid=<gid>&player_id=<player_id>
```
A player with id `player_id` leaves the guild with gid `gid`.  
Decreases the number of members of a guild. If 0 members left, delete the guild

