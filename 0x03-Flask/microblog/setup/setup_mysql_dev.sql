-- Create database, new user, set password, and permissions.
-- Creates a development database
CREATE DATABASE IF NOT EXISTS app_dev_db;

CREATE USER IF NOT EXISTS 'app_dev'@'localhost' IDENTIFIED BY 'App_dev_v0.1';
GRANT ALL PRIVILEGES ON app_dev_db . * TO 'app_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'app_dev'@'localhost';
FLUSH PRIVILEGES;
