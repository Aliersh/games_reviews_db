-- Tables creation

CREATE TABLE games(
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	genre TEXT NOT NULL,
	esrb_rating TEXT,
	release_date DATE NOT NULL,
	multiplayer BOOLEAN,
	developer_id INT NOT NULL,
	publisher_id INT NOT NULL
);

CREATE TABLE developers(
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL
);

CREATE TABLE publishers(
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL
);

CREATE TABLE platforms(
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL
);

CREATE TABLE review_sites(
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL
);

CREATE TABLE games_reviews(
	score INT NOT NULL,
	total_reviews INT NOT NULL,
	recommendation FLOAT NOT NULL,
	positive_reviews INT,
	game_id INT NOT NULL,
	review_site_id INT NOT NULL
);

CREATE TABLE games_platforms (
	game_id INT NOT NULL,
	platform_id INT NOT NULL
);

-- Adding foreign keys

ALTER TABLE games
ADD CONSTRAINT fk_games_developers
FOREIGN KEY (developer_id)
REFERENCES developers (id);

ALTER TABLE games
ADD CONSTRAINT fk_games_publishers
FOREIGN KEY (publisher_id)
REFERENCES publishers (id);

ALTER TABLE games_reviews
ADD CONSTRAINT fk_games_reviews_games
FOREIGN KEY (game_id)
REFERENCES games (id);

ALTER TABLE games_reviews
ADD CONSTRAINT fk_games_reviews_reviews
FOREIGN KEY (review_site_id)
REFERENCES review_sites (id);

ALTER TABLE games_platforms
ADD CONSTRAINT fk_games_platforms_games
FOREIGN KEY (game_id)
REFERENCES games (id);

ALTER TABLE games_platforms
ADD CONSTRAINT fk_games_platforms_platforms
FOREIGN KEY (platform_id)
REFERENCES platforms (id);

-- Adding primary keys to bridge tables

ALTER TABLE games_reviews
ADD CONSTRAINT pk_games_review_sites PRIMARY KEY (game_id, review_site_id);

-- Insert some sample data

INSERT INTO platforms (name)
VALUES ('Playstation 5'), ('Playstation 4'), ('Xbox Series X/S'), ('Xbox One'), ('Nintendo Switch');

INSERT INTO review_sites (name)
VALUES ('Opencritic'), ('Metacritic');

-- Elden Ring

INSERT INTO developers (name)
VALUES ('From Software');

INSERT INTO publishers (name)
VALUES ('Bandai Namco');

INSERT INTO games (name, genre, esrb_rating, release_date, multiplayer, developer_id, publisher_id)
VALUES ('Elden Ring', 'Action RPG', 'M', '2022-02-25', True, 1, 1);

INSERT INTO games_platforms (game_id, platform_id)
VALUES (1,1), (1,2), (1,3), (1,4);

INSERT INTO games_reviews (score, total_reviews, recommendation, game_id, review_site_id)
VALUES (95, 197, 98, 1, 1); -- Opencritic

INSERT INTO games_reviews (score, total_reviews, positive_reviews, game_id, review_site_id)
VALUES (96, 84, 84, 1, 2); -- Metacritic

-- Demons Souls

INSERT INTO developers (name)
VALUES ('Bluepoint Games');

INSERT INTO publishers (name)
VALUES ('Sony Interactive Entertainment');

INSERT INTO games (name, genre, release_date, multiplayer, developer_id, publisher_id)
VALUES ('Demons Souls', 'Action RPG', '2020-11-19', true, 2, 2);

INSERT INTO games_platforms (game_id, platform_id)
VALUES (2,1);

INSERT INTO games_reviews (score, total_reviews, recommendation, game_id, review_site_id)
VALUES (92, 119, 100, 2, 1); -- Opencritic

INSERT INTO games_reviews (score, total_reviews, positive_reviews, game_id, review_site_id)
VALUES (92, 100, 100, 2, 2) -- Metacritic

-- God Of War Ragnarok

INSERT INTO developers (name)
VALUES ('Santa Monica Studio');

INSERT INTO games (name, genre, esrb_rating, release_date, multiplayer, developer_id, publisher_id)
VALUES ('God Of War Ragnarok', 'Action Adventure', 'M', '2022-11-9', False, 3, 2);

INSERT INTO games_platforms (game_id, platform_id)
VALUES (3,1), (3,2);

INSERT INTO games_reviews (score, total_reviews, recommendation, game_id, review_site_id)
VALUES (94, 149, 98, 3, 1); -- Opencritic

INSERT INTO games_reviews (score, total_reviews, positive_reviews, game_id, review_site_id)
VALUES (94, 126, 126, 3, 2); -- Metacritic

-- Horizon Forbidden West

INSERT INTO developers (name)
VALUES ('Guerrilla Games');

INSERT INTO games (name, genre, esrb_rating, release_date, multiplayer, developer_id, publisher_id)
VALUES ('Horizon Forbidden West', 'Action RPG', 'T', '2022-02-18', False, 4, 2);

INSERT INTO games_platforms (game_id, platform_id)
VALUES (4,1), (4,2);

INSERT INTO games_reviews (score, total_reviews, recommendation, game_id, review_site_id)
VALUES (88, 185, 95, 4, 1); -- Opencritic

INSERT INTO games_reviews (score, total_reviews, positive_reviews, game_id, review_site_id)
VALUES (88, 126, 118, 4, 2); -- Metacritic

-- Try to search a meta score

WITH game_scores AS (
	SELECT
	g.name AS game_name,
	(gr.score * 0.5) + (((gr.no_reviews * 100)/200) * 0.3) + (gr.recommendation * 0.2) AS game_score
	FROM games_reviews gr
	JOIN games g
	ON g.id = gr.game_id
	WHERE review_site_id = 1
	UNION
	SELECT
	g.name AS game_name,
	(gr.score * 0.5) + (((gr.no_reviews * 100)/200) * 0.3) + (gr.recommendation * 0.2) AS game_score
	FROM games_reviews gr
	JOIN games g
	ON g.id = gr.game_id
	WHERE review_site_id = 2
)

SELECT game_name, AVG (game_score) AS meta_score
FROM game_scores
GROUP BY game_name
ORDER BY meta_score DESC

--

UPDATE games_reviews
SET recommendation = CAST((CAST (positive_reviews AS FLOAT)/CAST (no_reviews AS FLOAT)) * 100 AS INTEGER)
WHERE game_id = 3 AND review_site_id = 2;