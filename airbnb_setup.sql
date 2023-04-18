CREATE DATABASE IF NOT EXISTS `airbnb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE airbnb;

DROP TABLE IF EXISTS `amenities`;
CREATE TABLE `amenities` (
  `AmenityID` varchar(10) NOT NULL,
  `AmenityDescription` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`AmenityID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `bedtype`;
CREATE TABLE `bedtype` (
  `BedTypeID` varchar(10) NOT NULL,
  `BedType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`BedTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `booking`;
CREATE TABLE `booking` (
  `ListingID` int NOT NULL,
  `date` date DEFAULT NULL,
  `AvailablilityStatus` char(1) NOT NULL,
  `Price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ListingID`),
  CONSTRAINT `fk_Booking_Listing1` FOREIGN KEY (`ListingID`) REFERENCES `listing` (`ListingID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `host`;
CREATE TABLE `host` (
  `HostID` int NOT NULL,
  `HostName` varchar(45) DEFAULT NULL,
  `HostSince` date DEFAULT NULL,
  `HostCity` varchar(45) DEFAULT NULL,
  `HostNeighborhood` varchar(45) DEFAULT NULL,
  `HostState` varchar(45) DEFAULT NULL,
  `HostIdentityVerified` char(1) DEFAULT NULL,
  PRIMARY KEY (`HostID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `host_has_listing`;
CREATE TABLE `host_has_listing` (
  `ListingID` int NOT NULL,
  `HostID` int NOT NULL,
  `daily_price` int DEFAULT NULL,
  `number_of_reviews` int DEFAULT NULL,
  `review_scores_rating` int DEFAULT NULL,
  PRIMARY KEY (`ListingID`,`HostID`),
  KEY `fk_Host_has_Listing_Host1_idx` (`HostID`),
  KEY `fk_Host_has_Listing_Listing1_idx` (`ListingID`),
  CONSTRAINT `fk_Host_has_Listing_Host1` FOREIGN KEY (`HostID`) REFERENCES `host` (`HostID`),
  CONSTRAINT `fk_Host_has_Listing_Listing1` FOREIGN KEY (`ListingID`) REFERENCES `listing` (`ListingID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `listing`;
CREATE TABLE `listing` (
  `ListingID` int NOT NULL,
  `ListingName` varchar(50) DEFAULT NULL,
  `Street` varchar(100) DEFAULT NULL,
  `neighborhood` varchar(100) DEFAULT NULL,
  `City` varchar(45) DEFAULT NULL,
  `State` varchar(45) DEFAULT NULL,
  `Zipcode` varchar(10) DEFAULT NULL,
  `bathrooms` decimal(10,2) DEFAULT NULL,
  `bedrooms` decimal(10,2) DEFAULT NULL,
  `beds` decimal(10,2) DEFAULT NULL,
  `instant_bookable` char(2) DEFAULT NULL,
  `BedTypeID` varchar(10) NOT NULL,
  `RoomTypeID` varchar(10) NOT NULL,
  `PropertyTypeID` varchar(10) NOT NULL,
  PRIMARY KEY (`ListingID`,`BedTypeID`,`RoomTypeID`,`PropertyTypeID`),
  KEY `fk_Listing_Bed Type1_idx` (`BedTypeID`),
  KEY `fk_Listing_Room Type1_idx` (`RoomTypeID`),
  KEY `fk_Listing_Property Type1_idx` (`PropertyTypeID`),
  CONSTRAINT `fk_Listing_Bed Type1` FOREIGN KEY (`BedTypeID`) REFERENCES `bedtype` (`BedTypeID`),
  CONSTRAINT `fk_Listing_Property Type1` FOREIGN KEY (`PropertyTypeID`) REFERENCES `propertytype` (`PropertyTypeID`),
  CONSTRAINT `fk_Listing_Room Type1` FOREIGN KEY (`RoomTypeID`) REFERENCES `roomtype` (`RoomTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `listing_has_amenities`;
CREATE TABLE `listing_has_amenities` (
  `ListingID` int NOT NULL,
  `AmenityID` varchar(10) NOT NULL,
  PRIMARY KEY (`ListingID`,`AmenityID`),
  KEY `fk_Listing_has_Amenities_Amenities1_idx` (`AmenityID`),
  KEY `fk_Listing_has_Amenities_Listing1_idx` (`ListingID`),
  CONSTRAINT `fk_Listing_has_Amenities_Amenities1` FOREIGN KEY (`AmenityID`) REFERENCES `amenities` (`AmenityID`),
  CONSTRAINT `fk_Listing_has_Amenities_Listing1` FOREIGN KEY (`ListingID`) REFERENCES `listing` (`ListingID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `propertytype`;
CREATE TABLE `propertytype` (
  `PropertyTypeID` varchar(10) NOT NULL,
  `Property_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PropertyTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `reviewer`;
CREATE TABLE `reviewer` (
  `reviewerID` int NOT NULL,
  `ReviewerName` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`reviewerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `reviews`;
CREATE TABLE `reviews` (
  `ReviewID` int NOT NULL,
  `date` date DEFAULT NULL,
  `ReviewerID` int NOT NULL,
  `ListingID` int NOT NULL,
  PRIMARY KEY (`ReviewID`,`ReviewerID`,`ListingID`),
  KEY `fk_Reviews_Reviewer1_idx` (`ReviewerID`),
  KEY `fk_Reviews_Listing1_idx` (`ListingID`),
  CONSTRAINT `fk_Reviews_Listing1` FOREIGN KEY (`ListingID`) REFERENCES `listing` (`ListingID`),
  CONSTRAINT `fk_Reviews_Reviewer1` FOREIGN KEY (`ReviewerID`) REFERENCES `reviewer` (`reviewerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `roomtype`;
CREATE TABLE `roomtype` (
  `RoomTypeID` varchar(10) NOT NULL,
  `room_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`RoomTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
