CREATE DATABASE `656project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE 656project;

CREATE TABLE `basic_info` (
  `id` varchar(20) NOT NULL,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `listing_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `neighborhood_overview` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `picture_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `license` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `instant_bookable` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `calculated_host_listing_count` (
  `id` varchar(20) NOT NULL,
  `total_homes` varchar(20) DEFAULT NULL,
  `entire_homes` varchar(20) DEFAULT NULL,
  `private_rooms` varchar(20) DEFAULT NULL,
  `shared_rooms` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `calendar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `listing_id` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `avaliable` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `adjusted_price` varchar(45) DEFAULT NULL,
  `minimum_nights` varchar(45) DEFAULT NULL,
  `maximum_nights` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1048576 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `calendar_listing` (
  `id` varchar(20) NOT NULL,
  `updated` varchar(45) DEFAULT NULL,
  `has_availability` varchar(5) DEFAULT NULL,
  `availability_30` varchar(5) DEFAULT NULL,
  `availability_60` varchar(5) DEFAULT NULL,
  `availability_90` varchar(5) DEFAULT NULL,
  `availability_365` varchar(45) DEFAULT NULL,
  `calendar_last_scraped` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `host` (
  `id` varchar(20) NOT NULL,
  `url` text,
  `name` varchar(45) DEFAULT NULL,
  `since` varchar(20) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `about` text,
  `response_time` varchar(45) DEFAULT NULL,
  `response_rate` varchar(45) DEFAULT NULL,
  `acceptance_rate` varchar(45) DEFAULT NULL,
  `is_superhost` varchar(5) DEFAULT NULL,
  `thumbnail_url` text,
  `picture_url` text,
  `neighborhood` varchar(45) DEFAULT NULL,
  `listing_count` varchar(20) DEFAULT NULL,
  `total_listing_count` varchar(20) DEFAULT NULL,
  `verifications` varchar(45) DEFAULT NULL,
  `has_profile_pic` varchar(5) DEFAULT NULL,
  `identity_verified` varchar(5) DEFAULT NULL,
  `host_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `hosting` (
  `id` int NOT NULL,
  `hostid` int NOT NULL,
  PRIMARY KEY (`id`,`hostid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `neighborhood` (
  `id` varchar(20) NOT NULL,
  `cleansed` varchar(45) DEFAULT NULL,
  `group_cleansed` varchar(45) DEFAULT NULL,
  `latitude` varchar(45) DEFAULT NULL,
  `longitude` varchar(45) DEFAULT NULL,
  `property_type` varchar(45) DEFAULT NULL,
  `detail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `rent_history` (
  `id` varchar(20) NOT NULL,
  `price` varchar(20) DEFAULT NULL,
  `minimum_nights` varchar(20) DEFAULT NULL,
  `maximum_nights` varchar(20) DEFAULT NULL,
  `minimum_minimum_nights` varchar(20) DEFAULT NULL,
  `maximum_minimum_nights` varchar(20) DEFAULT NULL,
  `minimum_maximum_nights` varchar(20) DEFAULT NULL,
  `maximum_maximum_nights` varchar(20) DEFAULT NULL,
  `minimum_nights_avg_ntm` varchar(20) DEFAULT NULL,
  `maximum_nights_avg_ntm` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `reviews` (
  `id` varchar(20) NOT NULL,
  `listing_id` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `reviewer_id` varchar(20) DEFAULT NULL,
  `reviewer_name` varchar(20) DEFAULT NULL,
  `comments` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `reviews_listing` (
  `id` varchar(20) NOT NULL,
  `number_of_reviews` varchar(20) DEFAULT NULL,
  `number_of_reviews_ltm` varchar(20) DEFAULT NULL,
  `number_of_reviews_l30d` varchar(20) DEFAULT NULL,
  `first_review` varchar(20) DEFAULT NULL,
  `last_review` varchar(20) DEFAULT NULL,
  `review_scores_rating` varchar(20) DEFAULT NULL,
  `review_scores_accuracy` varchar(20) DEFAULT NULL,
  `review_scores_cleanliness` varchar(20) DEFAULT NULL,
  `review_scores_checkin` varchar(20) DEFAULT NULL,
  `review_scores_communication` varchar(20) DEFAULT NULL,
  `review_scores_location` varchar(20) DEFAULT NULL,
  `review_scores_value` varchar(20) DEFAULT NULL,
  `reviews_per_month` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `rooms` (
  `id` varchar(20) NOT NULL,
  `room_type` varchar(45) DEFAULT NULL,
  `accommodates` varchar(20) DEFAULT NULL,
  `bathrooms` varchar(45) DEFAULT NULL,
  `bathroom_text` varchar(45) DEFAULT NULL,
  `bedrooms` varchar(20) DEFAULT NULL,
  `beds` varchar(20) DEFAULT NULL,
  `amenities` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `scrape_info` (
  `id` varchar(20) NOT NULL,
  `scrape_id` varchar(45) DEFAULT NULL,
  `last_scraped` varchar(20) DEFAULT NULL,
  `source` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
