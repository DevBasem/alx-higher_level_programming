-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Use the database
USE `hbtn_0d_2`;

-- Creates the table force_name if it does not exist.
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
);
