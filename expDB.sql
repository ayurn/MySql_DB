-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: sqlOperations
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CONTACT`
--

DROP TABLE IF EXISTS `CONTACT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CONTACT` (
  `ID` int NOT NULL,
  `EMAIL` char(20) NOT NULL,
  `PHONE` mediumtext,
  `CITY` char(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONTACT`
--

LOCK TABLES `CONTACT` WRITE;
/*!40000 ALTER TABLE `CONTACT` DISABLE KEYS */;
INSERT INTO `CONTACT` VALUES (101,'Krishna@mymail.com',NULL,'Hyderabad'),(102,'Raja@mymail.com',NULL,'Vishakhapatnam'),(103,'Krishna@mymail.com',NULL,'Pune'),(104,'Raja@mymail.com',NULL,'Mumbai');
/*!40000 ALTER TABLE `CONTACT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customers` (
  `CustomerID` int NOT NULL,
  `CustomerName` varchar(250) NOT NULL,
  `ContactName` varchar(250) DEFAULT NULL,
  `Address` varchar(250) DEFAULT NULL,
  `City` varchar(200) DEFAULT NULL,
  `PostalCode` varchar(220) DEFAULT NULL,
  `Country` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1,'Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway'),(2,'Ericc','Thomas B. Eric','street 32','Polacc','4087','Germany'),(3,'Jabby','Karl thomson','Skagen B2','New york','7485','USA'),(4,'Aachara','Aachara kirk','Street c2','LosAngalis','7474','USA'),(5,'Puchi','Samantha bell','Street B4','LosAngalis','7485','USA'),(6,'shwan','Adolf shwar','Street 748','berlin','7426','Germany');
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `EMPLOYEE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EMPLOYEE` (
  `FIRST_NAME` char(20) NOT NULL,
  `LAST_NAME` char(20) DEFAULT NULL,
  `AGE` int DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `INCOME` float DEFAULT NULL,
  `CONTACT_ID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE`
--

LOCK TABLES `EMPLOYEE` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE` DISABLE KEYS */;
INSERT INTO `EMPLOYEE` VALUES ('Ramya','Rama Priya',27,'F',9000,101),('Vinay','Bhattacharya',20,'M',6000,102),('Sharukh','Sheik',25,'M',9000,103),('Sarmista','Sharma',26,'F',10000,104),('Trupthi','Mishra',24,'F',6000,105);
/*!40000 ALTER TABLE `EMPLOYEE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `basic_pays`
--

DROP TABLE IF EXISTS `basic_pays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `basic_pays` (
  `employee_name` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `salary` int NOT NULL,
  PRIMARY KEY (`employee_name`,`department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basic_pays`
--

LOCK TABLES `basic_pays` WRITE;
/*!40000 ALTER TABLE `basic_pays` DISABLE KEYS */;
INSERT INTO `basic_pays` VALUES ('Anthony Bow','Accounting',6627),('Barry Jones','SCM',10586),('Diane Murphy','Accounting',8435),('Foon Yue Tseng','Sales',6660),('George Vanauf','Sales',10563),('Gerard Bondur','Accounting',11472),('Gerard Hernandez','SCM',6949),('Jeff Firrelli','Accounting',8992),('Julie Firrelli','Sales',9181),('Larry Bott','SCM',11798),('Leslie Jennings','IT',8113),('Leslie Thompson','IT',5186),('Loui Bondur','SCM',10449),('Mary Patterson','Accounting',9998),('Pamela Castillo','SCM',11303),('Steve Patterson','Sales',9441),('William Patterson','Accounting',8870);
/*!40000 ALTER TABLE `basic_pays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_id` int NOT NULL,
  `name` varchar(35) DEFAULT NULL,
  `occupation` varchar(25) DEFAULT NULL,
  `age` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (101,'Peter','Engineer',32),(102,'Joseph','Developer',30),(103,'John','Leader',28),(104,'Stephen','Scientist',45),(105,'Suzi','Carpenter',26),(106,'Bob','Actor',25),(107,NULL,NULL,NULL);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `employee_info`
--

DROP TABLE IF EXISTS `employee_info`;
/*!50001 DROP VIEW IF EXISTS `employee_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `employee_info` AS SELECT 
 1 AS `AGE`,
 1 AS `FIRST_NAME`,
 1 AS `INCOME`,
 1 AS `CONTACT_ID`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL,
  `cust_id` int DEFAULT NULL,
  `prod_name` varchar(45) DEFAULT NULL,
  `order_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,101,'Laptop','2020-01-10'),(2,103,'Desktop','2020-02-12'),(3,106,'Iphone','2020-02-15'),(4,104,'Mobile','2020-03-05'),(5,102,'TV','2020-03-20');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overtime`
--

DROP TABLE IF EXISTS `overtime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overtime` (
  `employee_name` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `hours` int NOT NULL,
  PRIMARY KEY (`employee_name`,`department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overtime`
--

LOCK TABLES `overtime` WRITE;
/*!40000 ALTER TABLE `overtime` DISABLE KEYS */;
INSERT INTO `overtime` VALUES ('Anthony Bow','Finance',66),('Barry Jones','SCM',65),('Diane Murphy','Accounting',37),('Foon Yue Tseng','Sales',65),('George Vanauf','Marketing',89),('Gerard Bondur','Finance',47),('Gerard Hernandez','Marketing',66),('Jeff Firrelli','Accounting',40),('Julie Firrelli','Sales',81),('Larry Bott','SCM',100),('Leslie Jennings','IT',90),('Leslie Thompson','IT',88),('Loui Bondur','Marketing',49),('Mary Patterson','Accounting',74),('Pamela Castillo','SCM',96),('Steve Patterson','Sales',29),('William Patterson','Finance',58);
/*!40000 ALTER TABLE `overtime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `sales_employee` varchar(50) NOT NULL,
  `fiscal_year` int NOT NULL,
  `sale` decimal(14,2) NOT NULL,
  PRIMARY KEY (`sales_employee`,`fiscal_year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES ('Alice',2016,150.00),('Alice',2017,100.00),('Alice',2018,200.00),('Bob',2016,100.00),('Bob',2017,150.00),('Bob',2018,200.00),('John',2016,200.00),('John',2017,150.00),('John',2018,250.00);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scores`
--

DROP TABLE IF EXISTS `scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scores` (
  `name` varchar(20) NOT NULL,
  `score` int NOT NULL,
  `subjects` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores`
--

LOCK TABLES `scores` WRITE;
/*!40000 ALTER TABLE `scores` DISABLE KEYS */;
INSERT INTO `scores` VALUES ('Brown',62,NULL),('Davies',84,NULL),('Evans',87,NULL),('Johnson',100,NULL),('Jones',55,NULL),('Smith',81,NULL),('Taylor',62,NULL),('Thomas',72,NULL),('Williams',55,NULL),('Wilson',72,NULL);
/*!40000 ALTER TABLE `scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `roll` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `marks` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Ayur',80),(2,'Shubham',89),(3,'Anuj',90);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `studentInfo`
--

DROP TABLE IF EXISTS `studentInfo`;
/*!50001 DROP VIEW IF EXISTS `studentInfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `studentInfo` AS SELECT 
 1 AS `name`,
 1 AS `marks`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `employee_info`
--

/*!50001 DROP VIEW IF EXISTS `employee_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `employee_info` AS select `EMPLOYEE`.`AGE` AS `AGE`,`EMPLOYEE`.`FIRST_NAME` AS `FIRST_NAME`,`EMPLOYEE`.`INCOME` AS `INCOME`,`EMPLOYEE`.`CONTACT_ID` AS `CONTACT_ID` from `EMPLOYEE` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `studentInfo`
--

/*!50001 DROP VIEW IF EXISTS `studentInfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `studentInfo` AS select `student`.`name` AS `name`,`student`.`marks` AS `marks` from `student` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-23 21:04:23
