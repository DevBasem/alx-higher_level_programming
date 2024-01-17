-- Use the database
USE `hbtn_0d_usa`;

-- Select cities with corresponding state names using a subquery
SELECT
    `city`.`id` AS `city_id`,
    `city`.`name` AS `city_name`,
    `state`.`name` AS `state_name`
FROM
    `cities` AS `city`
    INNER JOIN `states` AS `state` ON `city`.`state_id` = `state`.`id`
ORDER BY
    `city`.`id`;
