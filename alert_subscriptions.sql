USE cloud_project;
CREATE TABLE alert_subscriptions (
	email VARCHAR(128),
    coin_name VARCHAR(10),
    differencepercentage INT,
    PRIMARY KEY (email),
    FOREIGN KEY (coin_name) REFERENCES price (coin_name)
);