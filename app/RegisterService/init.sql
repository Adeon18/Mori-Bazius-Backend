CREATE TABLE IF NOT EXISTS users (
    uid serial PRIMARY KEY,
    username VARCHAR (50) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL,
    created_on TIMESTAMP NOT NULL
)