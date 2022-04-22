CREATE TABLE USERS (
	user_id INTEGER PRIMARY KEY,
	name VARCHAR(32) NOT NULL,
    hashed_password VARCHAR(32) NOT NULL,
    line_token VARCHAR(64)
);

CREATE TABLE HOUSEWORKS (
	housework_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES USERS(user_id) ON DELETE RESTRICT,
	name VARCHAR(32) NOT NULL,
    interval_day INTEGER NOT NULL,
    last_notification_day DATE
);