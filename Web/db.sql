/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `project`;

/*Table structure for table `artist` */

DROP TABLE IF EXISTS `artist`;

CREATE TABLE `artist` (
  `artistid` int(100) NOT NULL AUTO_INCREMENT,
  `loginid` int(100) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`artistid`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `artist` */

insert  into `artist`(`artistid`,`loginid`,`firstname`,`lastname`,`email`,`gender`,`phone`,`place`,`qualification`) values 
(1,1,'sulu','soni','suyusoni@gmail.com','male','01234567890','ptb','PES MASTER'),
(2,3,'rashi','ridhu','ridhu@gmail.com','male','87654087654','tirur','MCA,MBBS');

/*Table structure for table `booking_child` */

DROP TABLE IF EXISTS `booking_child`;

CREATE TABLE `booking_child` (
  `bookingchildid` int(100) NOT NULL AUTO_INCREMENT,
  `bookingmasterid` int(100) DEFAULT NULL,
  `workid` int(100) DEFAULT NULL,
  `quantity` varchar(200) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bookingchildid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `booking_child` */

insert  into `booking_child`(`bookingchildid`,`bookingmasterid`,`workid`,`quantity`,`amount`,`status`) values 
(1,1,1,'2','200','pending'),
(2,1,1,'3','300','pending'),
(3,1,1,'3','300','pending');

/*Table structure for table `booking_master` */

DROP TABLE IF EXISTS `booking_master`;

CREATE TABLE `booking_master` (
  `bookingmasterid` int(100) NOT NULL AUTO_INCREMENT,
  `userid` int(100) DEFAULT NULL,
  `totalamount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bookingmasterid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `booking_master` */

insert  into `booking_master`(`bookingmasterid`,`userid`,`totalamount`,`date`,`status`) values 
(1,5,'800','2024-12-30','pending');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chatid` int(100) NOT NULL AUTO_INCREMENT,
  `senderid` int(100) DEFAULT NULL,
  `sendertype` varchar(100) DEFAULT NULL,
  `receiverid` int(100) DEFAULT NULL,
  `receivertype` varchar(100) DEFAULT NULL,
  `message` varchar(300) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chatid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaintid` int(100) NOT NULL AUTO_INCREMENT,
  `userid` int(100) DEFAULT NULL,
  `artistid` int(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaintid`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaintid`,`userid`,`artistid`,`title`,`description`,`reply`,`date`) values 
(1,1,1,'hhagsgs','hsbsbs','pending','2024-12-23'),
(13,8,2,'ddd','ddddddd','pending','2024-12-24'),
(9,8,1,'aaaaa','aaaaaaaaa','pending','2024-12-24'),
(10,8,1,'bbbbbb','bbbbb','pending','2024-12-24'),
(11,8,2,'ccc','cccccccc','pending','2024-12-24'),
(12,8,2,'ddd','ddddddd','pending','2024-12-24');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedbackid` int(100) NOT NULL AUTO_INCREMENT,
  `userid` int(100) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedbackid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedbackid`,`userid`,`feedback`,`date`) values 
(1,1,'Amazing','12-12-24'),
(2,8,'aaa','2024-12-30'),
(3,5,'hy','2024-12-30');

/*Table structure for table `guidance` */

DROP TABLE IF EXISTS `guidance`;

CREATE TABLE `guidance` (
  `guidanceid` int(100) NOT NULL AUTO_INCREMENT,
  `requestid` int(100) DEFAULT NULL,
  `path` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`guidanceid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `guidance` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`usertype`) values 
(1,'suluman','soni0017','artist'),
(2,'admin','admin','admin'),
(3,'a','a','artist'),
(4,'user1','user1','user'),
(5,'soni','1','user'),
(7,'xyzxyz','12345678','user'),
(8,'sonisulu','1','user');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `paymentid` int(100) NOT NULL AUTO_INCREMENT,
  `bookingmasterid` int(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`paymentid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `ratingid` int(100) NOT NULL AUTO_INCREMENT,
  `artistid` int(100) DEFAULT NULL,
  `userid` int(100) DEFAULT NULL,
  `rating` varchar(200) DEFAULT NULL,
  `review` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ratingid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `requestid` int(100) NOT NULL AUTO_INCREMENT,
  `artistid` int(100) DEFAULT NULL,
  `userid` int(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`requestid`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`requestid`,`artistid`,`userid`,`description`,`reply`,`date`,`status`,`amount`) values 
(1,2,8,'request....uuuuu','pending','2024-12-27','pending','pending'),
(2,1,8,'aaaaaaaa','pending','2024-12-27','pending','pending'),
(3,1,8,'aaaaaaaaa','pending','2024-12-27','pending','pending'),
(4,1,8,'aaaaaaaaa','pending','2024-12-27','pending','pending'),
(5,1,8,'bbbbbbb','pending','2024-12-27','pending','pending'),
(6,2,8,'sssss','pending','2024-12-27','pending','pending'),
(7,2,8,'64w64dutfjtxhdjtxit','pending','2024-12-27','pending','pending'),
(8,2,8,'ujtt','pending','2024-12-27','pending','pending'),
(9,2,8,'ujtt','pending','2024-12-27','pending','pending'),
(10,2,8,'ujtt','pending','2024-12-27','pending','pending'),
(11,2,8,'ujtt','pending','2024-12-27','pending','pending'),
(12,2,8,'xcb dgg','pending','2024-12-27','pending','pending'),
(13,1,8,'hfxjgcjg','pending','2024-12-27','pending','pending'),
(14,1,8,'fthuj','pending','2024-12-27','pending','pending'),
(15,1,8,'hwuwu18ur8e9e8e8eidhe8w','pending','2024-12-27','pending','pending');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `reviewid` int(100) NOT NULL AUTO_INCREMENT,
  `workid` int(100) DEFAULT NULL,
  `userid` int(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`reviewid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `review` */

/*Table structure for table `tutorials` */

DROP TABLE IF EXISTS `tutorials`;

CREATE TABLE `tutorials` (
  `tutorialid` int(100) NOT NULL AUTO_INCREMENT,
  `artistid` int(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `path` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`tutorialid`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tutorials` */

insert  into `tutorials`(`tutorialid`,`artistid`,`title`,`path`,`date`) values 
(1,2,'kkk','lll','2024-12-02'),
(2,1,'sss','222','2024-12-24');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userid` int(100) NOT NULL AUTO_INCREMENT,
  `loginid` int(100) DEFAULT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `place` varchar(200) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`userid`,`loginid`,`firstname`,`lastname`,`place`,`phone`,`email`,`gender`) values 
(1,10,'aaa','aaa','aaa','111','a1@g.com','male'),
(2,5,'qqq','aaa','zzz','111','m@gmail.com','male'),
(4,7,'xxx','yyy','zzz','222','xyz@gmail.com','other'),
(5,8,'soni','sulu','ptm','1234567890','s@gmail.com','female');

/*Table structure for table `works` */

DROP TABLE IF EXISTS `works`;

CREATE TABLE `works` (
  `workid` int(100) NOT NULL AUTO_INCREMENT,
  `artistid` int(100) DEFAULT NULL,
  `workname` varchar(100) DEFAULT NULL,
  `path` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`workid`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `works` */

insert  into `works`(`workid`,`artistid`,`workname`,`path`,`amount`,`status`) values 
(1,1,'asdfa','fasf','100','finished'),
(2,2,'worke2','dfasdf','200','finished');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
