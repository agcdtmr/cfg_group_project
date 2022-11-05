CREATE DATABASE job_search;

USE job_search;

CREATE TABLE users(user_ID INT UNIQUE PRIMARY KEY AUTO_INCREMENT, surname VARCHAR(50), first_name VARCHAR(50),
username VARCHAR(100) UNIQUE, email VARCHAR(100) UNIQUE, password VARCHAR(100));


 CREATE TABLE saved_jobs(saved_job_ID INT UNIQUE PRIMARY KEY AUTO_INCREMENT, user_id INT, employerID INT, employerName VARCHAR(100),
 expirationDate VARCHAR(100), jobDescription VARCHAR(10000), jobID INT, jobTitle VARCHAR(100), jobURL VARCHAR(1000),
 locationName VARCHAR(100), maximumSalary INT, minimumSalary INT, applied_for_job VARCHAR(3),
 FOREIGN KEY(user_ID) REFERENCES users(user_ID));