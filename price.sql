USE cloud_project;
CREATE TABLE price (
	coin_name VARCHAR(10),
    time_stamp TIME,
    coin_price FLOAT,
    PRIMARY KEY (coin_name)
);