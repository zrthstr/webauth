CREATE TABLE user (
	id TEXT PRIMARY_KEY,
	name TEXT not NULL,
	email TEXT UNIQUE not NULL, 
	profile_pic TEXT not NULL
);
