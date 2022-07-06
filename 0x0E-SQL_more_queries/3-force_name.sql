-- Creates the table force_name on your MySQL server.
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB;
