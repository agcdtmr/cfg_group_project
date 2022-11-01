CREATE DATABASE job_search;
USE job_search;

CREATE TABLE users
(ID INT AUTO_INCREMENT PRIMARY KEY,
surname VARCHAR(50),
first_name VARCHAR(50),
 email VARCHAR(100) UNIQUE,
 password VARCHAR(100));

CREATE TABLE saved_jobs
(ID INT PRIMARY KEY,
user_id INT,
FOREIGN KEY (user_id) REFERENCES users(ID),
 job_title VARCHAR(100),
 company_name VARCHAR(100),
 salary INT,
 location VARCHAR(100),
 link VARCHAR(100),
 applied_for_job VARCHAR(3));