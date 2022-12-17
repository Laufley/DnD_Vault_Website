DROP TABLE players_history;
DROP TABLE players;
DROP TABLE campaigns;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE players_history (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    campaign_id INT NOT NULL REFERENCES campaigns(id) ON DELETE CASCADE
);