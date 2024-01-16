-- Convert hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0
-- Convert first_table table and the name field to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
