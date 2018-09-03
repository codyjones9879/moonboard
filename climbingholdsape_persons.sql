CREATE DATABASE  IF NOT EXISTS `climbingholdsape` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `climbingholdsape`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: climbingholdsape
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `persons`
--

DROP TABLE IF EXISTS `persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persons` (
  `PersonID` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `LastName` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `FirstName` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `Address` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `City` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DateAdded` datetime NOT NULL,
  `DateUpdated` datetime NOT NULL,
  PRIMARY KEY (`FirstName`,`LastName`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persons`
--

LOCK TABLES `persons` WRITE;
/*!40000 ALTER TABLE `persons` DISABLE KEYS */;
INSERT INTO `persons` VALUES ('1','Jones','Cody','788 Taylor Ln','Stoughton','0000-00-00 00:00:00','0000-00-00 00:00:00'),('2','Jonesy','Cody','788 Taylor Ln','Stoughton','0000-00-00 00:00:00','0000-00-00 00:00:00'),('1','Wayne','Bruce','Space','Mars','2017-08-24 08:34:31','2017-08-24 10:34:38'),('1','Jones','Bruce','Space','Mars','2017-08-24 10:24:02','2017-08-24 10:34:10');
/*!40000 ALTER TABLE `persons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-03 12:53:02
