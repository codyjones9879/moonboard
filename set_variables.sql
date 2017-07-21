ALTER DATABASE climbingholdsape CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE moonboard CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;
SET character_set_server = utf8mb4;
REPAIR TABLE table_name;
OPTIMIZE TABLE table_name;
SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';