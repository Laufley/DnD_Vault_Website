DROP TABLE players_history;
DROP TABLE players;
DROP TABLE campaigns;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    dm VARCHAR(255),
    max_capacity INT,
    price INT,
    details VARCHAR(255) 
);

CREATE TABLE players_history (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    campaign_id INT NOT NULL REFERENCES campaigns(id) ON DELETE CASCADE
);