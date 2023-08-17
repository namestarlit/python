-- Create database, new user, set password, and permissions.
-- Create a test database
CREATE DATABASE IF NOT EXISTS app_test_db;

CREATE USER IF NOT EXISTS 'app_test'@'localhost' IDENTIFIED BY 'app_test_pwd';
GRANT ALL PRIVILEGES ON app_test_db . * TO 'app_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'app_test'@'localhost';
FLUSH PRIVILEGES;
