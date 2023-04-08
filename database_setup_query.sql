CREATE DATABASE `656project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE 656project;

CREATE TABLE `basic_info` (
  `house_id` bigint NOT NULL,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `instant_bookable` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `price` int DEFAULT NULL,
  `availability` int DEFAULT NULL,
  `room_type` varchar(20) DEFAULT NULL,
  `bathrooms` varchar(20) DEFAULT NULL,
  `bedrooms` int DEFAULT NULL,
  `beds` int DEFAULT NULL,
  `amenities` text,
  `numbers_of_reviews` int DEFAULT NULL,
  `review_score` float DEFAULT NULL,
  `host_id` bigint DEFAULT NULL,
  `neighborhood_id` bigint DEFAULT NULL,
  `property` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`house_id`),
  KEY `host_id_idx` (`host_id`),
  KEY `neighborhood_id_idx` (`neighborhood_id`),
  CONSTRAINT `host_id` FOREIGN KEY (`host_id`) REFERENCES `host` (`host_id`),
  CONSTRAINT `neighborhood_id` FOREIGN KEY (`neighborhood_id`) REFERENCES `neighborhood` (`neighborhood_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `calendar` (
  `calendar_id` int NOT NULL AUTO_INCREMENT,
  `house_id` bigint DEFAULT NULL,
  `date` date DEFAULT NULL,
  `available` varchar(5) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `adjusted_price` int DEFAULT NULL,
  `minimum_nights` int DEFAULT NULL,
  `maximum_nights` int DEFAULT NULL,
  PRIMARY KEY (`calendar_id`),
  KEY `house_id_idx` (`house_id`),
  CONSTRAINT `_house_id` FOREIGN KEY (`house_id`) REFERENCES `basic_info` (`house_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3014511 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `host` (
  `host_id` bigint NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `since` date DEFAULT NULL,
  `about` text,
  `response_time` varchar(45) DEFAULT NULL,
  `response_rate` varchar(45) DEFAULT NULL,
  `acceptance_rate` varchar(45) DEFAULT NULL,
  `identity_verified` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`host_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `neighborhood` (
  `neighborhood_id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`neighborhood_id`)
) ENGINE=InnoDB AUTO_INCREMENT=418 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `reviews` (
  `review_id` bigint NOT NULL,
  `house_id` bigint DEFAULT NULL,
  `date` date DEFAULT NULL,
  `reviewer_name` varchar(20) DEFAULT NULL,
  `comments` text,
  PRIMARY KEY (`review_id`),
  KEY `house_id_idx` (`house_id`),
  CONSTRAINT `house_id` FOREIGN KEY (`house_id`) REFERENCES `basic_info` (`house_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
