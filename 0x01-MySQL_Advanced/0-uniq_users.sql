-- SQL script that creates a table users
--  Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application
CREATE TABLE If NOT EXISTS `users` (  
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `name` VARCHAR(255)
);
