-- Use the database
USE `hbtn_0d_usa`;

-- Select cities with corresponding state names using a subquery
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
