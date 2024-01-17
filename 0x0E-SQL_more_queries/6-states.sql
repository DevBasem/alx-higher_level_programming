-- Create the table states if it does not exist
CREATE TABLE IF NOT EXISTS `states` (
  `id` INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
  `name` VARCHAR(256) NOT NULL
);
