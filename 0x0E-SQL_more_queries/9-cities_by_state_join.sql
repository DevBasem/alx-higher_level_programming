-- Use the database
USE `hbtn_0d_usa`;

-- Select cities with corresponding state names using a subquery
SELECT
    `cities`.`id`,
    `cities`.`name`,
    (SELECT `states`.`name` FROM `states` WHERE `states`.`id` = `cities`.`state_id`) AS `state_name`
FROM
    `cities`
ORDER BY
    `cities`.`id`;
