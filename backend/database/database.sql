-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` varchar(55) COLLATE utf8mb3_bin NOT NULL,
  `book_name` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `book_year` int DEFAULT NULL,
  `book_genre` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('6d8a4e1b-9c3f-4b8a-b1e6-0f7d2e5a3c4b','The Godfather',1969,'Crime'),('6d8e4e1b-9c3f-4b8a-b1e6-0f7d2e5a3c4b','The Hobbit',1937,'Fantasy'),('6d8e4e1b-9c3f-4b8a-b1e6-0f7d2e5a3c4c','The Road',2006,'Drama'),('9c1b8e7d-3b4a-4d6c-b2e3-7f1d8e2a7b4a','To Kill a Mockingbird',1960,'Science Fiction');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like_books`
--

DROP TABLE IF EXISTS `like_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_books` (
  `user_id` varchar(55) COLLATE utf8mb3_bin DEFAULT NULL,
  `book_id` varchar(55) COLLATE utf8mb3_bin DEFAULT NULL,
  KEY `fk_user_id_books` (`user_id`),
  KEY `fk_books` (`book_id`),
  CONSTRAINT `fk_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_id_books` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_books`
--

LOCK TABLES `like_books` WRITE;
/*!40000 ALTER TABLE `like_books` DISABLE KEYS */;
INSERT INTO `like_books` VALUES ('63dc2be6-045c-46b4-addb-058fb25ae29d','6d8e4e1b-9c3f-4b8a-b1e6-0f7d2e5a3c4c');
/*!40000 ALTER TABLE `like_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like_movie`
--

DROP TABLE IF EXISTS `like_movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_movie` (
  `user_id` varchar(55) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `movie_id` varchar(55) COLLATE utf8mb3_bin DEFAULT NULL,
  KEY `fk_movie_id` (`movie_id`),
  KEY `fk_user_id_movie` (`user_id`),
  CONSTRAINT `fk_movie_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_id_movie` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_movie`
--

LOCK TABLES `like_movie` WRITE;
/*!40000 ALTER TABLE `like_movie` DISABLE KEYS */;
INSERT INTO `like_movie` VALUES ('63dc2be6-045c-46b4-addb-058fb25ae29d','1c4a1e26-8c6f-4c6d-b78e-8d6ed2e1e0bc'),('63dc2be6-045c-46b4-addb-058fb25ae29d','1c4a1e26-8c6f-4c6d-b78e-8e6ed2e1e0bc');
/*!40000 ALTER TABLE `like_movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like_tvshow`
--

DROP TABLE IF EXISTS `like_tvshow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_tvshow` (
  `user_id` varchar(55) COLLATE utf8mb3_bin DEFAULT NULL,
  `tvshow_id` varchar(55) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  KEY `fk_user_id` (`user_id`),
  KEY `fk_tvshow_id` (`tvshow_id`),
  CONSTRAINT `fk_tvshow_id` FOREIGN KEY (`tvshow_id`) REFERENCES `tv_shows` (`tvshow_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_tvshow`
--

LOCK TABLES `like_tvshow` WRITE;
/*!40000 ALTER TABLE `like_tvshow` DISABLE KEYS */;
INSERT INTO `like_tvshow` VALUES ('63dc2be6-045c-46b4-addb-058fb25ae29d','4a1c7e2d-d0ab-4e98-828b-0d8c6f7e2c56');
/*!40000 ALTER TABLE `like_tvshow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `user_id` varchar(55) COLLATE utf8mb3_bin NOT NULL,
  `media_id` varchar(55) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `movie_id` varchar(55) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `movie_name` varchar(55) COLLATE utf8mb3_bin DEFAULT NULL,
  `movie_year` int DEFAULT NULL,
  `movie_genre` varchar(55) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES ('1c4a1e26-8c6f-4c6d-b78e-8d6ed2e1e0bc','The Shawshank Redemption',1994,'Drama'),('1c4a1e26-8c6f-4c6d-b78e-8e6ed2e1e0bc','The Godfather',1972,'Crime'),('3e9fbe7c-1458-456b-9e4f-1bcd5d0a3ed8','Pulp Fiction',1994,'Crime'),('6f12a6e9-9a4d-4c5b-8d7f-bc3a2cb1e92b','Forrest Gump',1994,'Drama'),('7c2b4a23-2a4e-4e6d-bdb7-c08f7b737c6e','The Matrix',1999,'Action'),('9d4d1e15-d0c7-47bb-bad5-9c2ec52a624e','The Dark Knight',2008,'Action'),('a7d39b6e-56ab-4b3f-832d-0e7d0c9056b8','Inception',2010,'Science Fiction'),('c2f0e6b8-9b6f-4ac1-8b4e-5d4a3b2e8d59','Avatar',2009,'Fantasy');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_shows`
--

DROP TABLE IF EXISTS `tv_shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tv_shows` (
  `tvshow_id` varchar(55) COLLATE utf8mb3_bin NOT NULL,
  `tvshow_name` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `tvshow_year` int DEFAULT NULL,
  `tvshow_genre` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`tvshow_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_shows`
--

LOCK TABLES `tv_shows` WRITE;
/*!40000 ALTER TABLE `tv_shows` DISABLE KEYS */;
INSERT INTO `tv_shows` VALUES ('1d6c7b18-ec6f-42d5-a74b-8e7f1b90a5c9','Game of Thrones',2011,'Fantasy'),('4a1c7e2d-d0ab-4e98-828b-0d8c6f7e2c56','The Office',2005,'Comedy'),('5d8e4b1f-0c4a-4e3d-832b-7d6a3c5b0a76','Sherlock',2010,'Crime'),('8f0e2a3d-6b7e-4e57-b1a3-2c8d0e9c6f4d','Friends',1994,'Comedy'),('a3b2f4e2-16d2-4b9e-bd68-8db989e8c1a5','Stranger Things',2016,'Science Fiction'),('f6a2e0c5-0b63-464f-8f67-bc0d77a8e945','Breaking Bad',2008,'Drama');
/*!40000 ALTER TABLE `tv_shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` varchar(55) COLLATE utf8mb3_bin NOT NULL,
  `user_email` varchar(45) COLLATE utf8mb3_bin DEFAULT NULL,
  `user_password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin DEFAULT NULL,
  `user_created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('63dc2be6-045c-46b4-addb-058fb25ae29d','istra@opgmirko.hr','$2a$12$MQGdSIKbAmCmB.FWEjRTue6d4ieZMrfoGHxPXGXsdUYp4l82YPhBq','2024-08-24 20:51:34'),('d10dbbaa-203b-4b97-b7c0-4ad7c41e728a','frfr@gmail.com','$2a$12$Xtch2BD34Oq6/BKK79yhauK238Dm.zj54u.6T2KbWym9DrRQJ8JZK','2024-08-25 11:17:50'),('ec4519a2-512f-45a5-8171-06e2cc90bb8f','alanismirko@gmail.com','$2a$12$sVvnU9N4nKd6Pi0r4HxE8ugoTm.hiAKXNktt0VYPB3f61FenrU/S.','2024-08-24 20:42:38');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-25 16:45:29
