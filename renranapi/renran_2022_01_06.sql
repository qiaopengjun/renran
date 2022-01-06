-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: renran
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 用户信息',6,'add_user'),(22,'Can change 用户信息',6,'change_user'),(23,'Can delete 用户信息',6,'delete_user'),(24,'Can view 用户信息',6,'view_user'),(25,'Can add 第三方社交账号登录用户数据',7,'add_oauthuser'),(26,'Can change 第三方社交账号登录用户数据',7,'change_oauthuser'),(27,'Can delete 第三方社交账号登录用户数据',7,'delete_oauthuser'),(28,'Can view 第三方社交账号登录用户数据',7,'view_oauthuser'),(29,'Can add 轮播图',8,'add_banner'),(30,'Can change 轮播图',8,'change_banner'),(31,'Can delete 轮播图',8,'delete_banner'),(32,'Can view 轮播图',8,'view_banner'),(33,'Can add 导航菜单',9,'add_nav'),(34,'Can change 导航菜单',9,'change_nav'),(35,'Can delete 导航菜单',9,'delete_nav'),(36,'Can view 导航菜单',9,'view_nav'),(37,'Can add 文章图片',10,'add_articleimage'),(38,'Can change 文章图片',10,'change_articleimage'),(39,'Can delete 文章图片',10,'delete_articleimage'),(40,'Can view 文章图片',10,'view_articleimage'),(41,'Can add 专题管理员',11,'add_specialmanager'),(42,'Can change 专题管理员',11,'change_specialmanager'),(43,'Can delete 专题管理员',11,'delete_specialmanager'),(44,'Can view 专题管理员',11,'view_specialmanager'),(45,'Can add 专题的文章',12,'add_articlepostspecial'),(46,'Can change 专题的文章',12,'change_articlepostspecial'),(47,'Can delete 专题的文章',12,'delete_articlepostspecial'),(48,'Can view 专题的文章',12,'view_articlepostspecial'),(49,'Can add 文集',13,'add_articlecollection'),(50,'Can change 文集',13,'change_articlecollection'),(51,'Can delete 文集',13,'delete_articlecollection'),(52,'Can view 文集',13,'view_articlecollection'),(53,'Can add 专题',14,'add_articlespecial'),(54,'Can change 专题',14,'change_articlespecial'),(55,'Can delete 专题',14,'delete_articlespecial'),(56,'Can view 专题',14,'view_articlespecial'),(57,'Can add 专题粉丝',15,'add_specialfocus'),(58,'Can change 专题粉丝',15,'change_specialfocus'),(59,'Can delete 专题粉丝',15,'delete_specialfocus'),(60,'Can view 专题粉丝',15,'view_specialfocus'),(61,'Can add 文章',16,'add_article'),(62,'Can change 文章',16,'change_article'),(63,'Can delete 文章',16,'delete_article'),(64,'Can view 文章',16,'view_article'),(65,'Can add 打赏记录',17,'add_reward'),(66,'Can change 打赏记录',17,'change_reward'),(67,'Can delete 打赏记录',17,'delete_reward'),(68,'Can view 打赏记录',17,'view_reward');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_rr_users_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-12-26 13:17:58.472193','1','第一张图片',1,'[{\"added\": {}}]',8,1),(2,'2021-12-26 14:07:39.893686','2','第二张图片',1,'[{\"added\": {}}]',8,1),(3,'2021-12-26 14:13:19.523150','3','第三张图片',1,'[{\"added\": {}}]',8,1),(4,'2021-12-26 15:29:08.593532','1','第一张图片',2,'[{\"changed\": {\"fields\": [\"\\u8f6e\\u64ad\\u56fe\\u5e7f\\u544a\\u5730\\u5740\", \"\\u662f\\u5426\\u7ad9\\u5916\\u5730\\u5740\"]}}]',8,1),(5,'2021-12-27 12:54:19.157142','1','关注',1,'[{\"added\": {}}]',9,1),(6,'2021-12-27 14:10:45.180174','2','消息',2,'[{\"changed\": {\"fields\": [\"\\u662f\\u5426\\u663e\\u793a\"]}}]',9,1),(7,'2021-12-27 14:10:59.438629','2','消息',2,'[{\"changed\": {\"fields\": [\"\\u662f\\u5426\\u663e\\u793a\"]}}]',9,1),(8,'2021-12-27 15:02:06.298150','12','关于荏苒',1,'[{\"added\": {}}]',9,1),(9,'2021-12-28 14:59:54.886297','1','第一张图片',2,'[{\"changed\": {\"fields\": [\"\\u8f6e\\u64ad\\u56fe\"]}}]',8,1),(10,'2021-12-28 15:07:47.136804','3','第三张图片',2,'[{\"changed\": {\"fields\": [\"\\u8f6e\\u64ad\\u56fe\"]}}]',8,1),(11,'2021-12-28 15:08:35.747779','2','第二张图片',2,'[{\"changed\": {\"fields\": [\"\\u8f6e\\u64ad\\u56fe\"]}}]',8,1),(12,'2021-12-29 14:16:10.966461','1','ArticleCollection object (1)',1,'[{\"added\": {}}]',13,1),(13,'2021-12-29 14:16:41.483801','2','ArticleCollection object (2)',1,'[{\"added\": {}}]',13,1),(14,'2021-12-29 14:17:03.092462','3','ArticleCollection object (3)',1,'[{\"added\": {}}]',13,1),(15,'2021-12-29 14:43:03.318678','1','我的散文',2,'[{\"changed\": {\"fields\": [\"\\u7528\\u6237\"]}}]',13,1),(16,'2021-12-29 14:43:10.697869','2','我的诗歌',2,'[{\"changed\": {\"fields\": [\"\\u7528\\u6237\"]}}]',13,1),(17,'2021-12-29 15:13:15.923269','2','我的诗歌',2,'[{\"changed\": {\"fields\": [\"\\u7528\\u6237\"]}}]',13,1),(18,'2021-12-30 12:21:33.962151','3','测试文集',2,'[{\"changed\": {\"fields\": [\"\\u7528\\u6237\"]}}]',13,1),(19,'2021-12-30 13:19:56.162014','1','２０２１－１２－３０－日记',1,'[{\"added\": {}}]',16,1),(20,'2021-12-30 14:17:24.327945','2','２０２１－１0－３０－日记',1,'[{\"added\": {}}]',16,1),(21,'2021-12-30 14:34:34.705099','3','２０２１－１1－３０－日记',1,'[{\"added\": {}}]',16,1),(22,'2021-12-30 14:44:31.552187','4','２０２１－１1－1０－日记',1,'[{\"added\": {}}]',16,1),(23,'2021-12-31 12:46:55.262878','4','日记本',2,'[{\"changed\": {\"fields\": [\"\\u662f\\u5426\\u5220\\u9664\"]}}]',13,1),(24,'2022-01-01 09:59:58.302864','1','第一张图片',2,'[{\"changed\": {\"fields\": [\"\\u4e0b\\u67b6\\u65f6\\u95f4\"]}}]',8,1),(25,'2022-01-01 10:00:19.815231','2','第二张图片',2,'[{\"changed\": {\"fields\": [\"\\u4e0b\\u67b6\\u65f6\\u95f4\"]}}]',8,1),(26,'2022-01-01 10:00:36.704986','3','第三张图片',2,'[{\"changed\": {\"fields\": [\"\\u4e0b\\u67b6\\u65f6\\u95f4\"]}}]',8,1),(27,'2022-01-01 14:27:40.813079','1','相亲',2,'[{\"changed\": {\"fields\": [\"\\u5c01\\u9762\\u56fe\\u7247\"]}}]',14,1),(28,'2022-01-01 14:27:50.677746','2','相爱',2,'[]',14,1),(29,'2022-01-01 14:27:59.980405','2','相爱',2,'[{\"changed\": {\"fields\": [\"\\u5c01\\u9762\\u56fe\\u7247\"]}}]',14,1),(30,'2022-01-01 14:28:11.495701','3','篮球',2,'[{\"changed\": {\"fields\": [\"\\u5c01\\u9762\\u56fe\\u7247\"]}}]',14,1),(31,'2022-01-01 14:28:21.244108','4','旅游',2,'[{\"changed\": {\"fields\": [\"\\u5c01\\u9762\\u56fe\\u7247\"]}}]',14,1),(32,'2022-01-01 15:33:01.548627','1','root',2,'[{\"changed\": {\"fields\": [\"\\u5934\\u50cf\"]}}]',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(16,'article','article'),(13,'article','articlecollection'),(10,'article','articleimage'),(12,'article','articlepostspecial'),(14,'article','articlespecial'),(15,'article','specialfocus'),(11,'article','specialmanager'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(8,'home','banner'),(9,'home','nav'),(7,'oauth','oauthuser'),(17,'payments','reward'),(5,'sessions','session'),(6,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-12-19 11:36:04.933849'),(2,'contenttypes','0002_remove_content_type_name','2021-12-19 11:36:05.061979'),(3,'auth','0001_initial','2021-12-19 11:36:05.494597'),(4,'auth','0002_alter_permission_name_max_length','2021-12-19 11:36:05.575144'),(5,'auth','0003_alter_user_email_max_length','2021-12-19 11:36:05.588028'),(6,'auth','0004_alter_user_username_opts','2021-12-19 11:36:05.602720'),(7,'auth','0005_alter_user_last_login_null','2021-12-19 11:36:05.616559'),(8,'auth','0006_require_contenttypes_0002','2021-12-19 11:36:05.623099'),(9,'auth','0007_alter_validators_add_error_messages','2021-12-19 11:36:05.636024'),(10,'auth','0008_alter_user_username_max_length','2021-12-19 11:36:05.649119'),(11,'auth','0009_alter_user_last_name_max_length','2021-12-19 11:36:05.665644'),(12,'auth','0010_alter_group_name_max_length','2021-12-19 11:36:05.697986'),(13,'auth','0011_update_proxy_permissions','2021-12-19 11:36:05.712206'),(14,'auth','0012_alter_user_first_name_max_length','2021-12-19 11:36:05.727964'),(15,'users','0001_initial','2021-12-19 11:36:06.224812'),(16,'admin','0001_initial','2021-12-19 11:36:06.395858'),(17,'admin','0002_logentry_remove_auto_add','2021-12-19 11:36:06.412274'),(18,'admin','0003_logentry_add_action_flag_choices','2021-12-19 11:36:06.433797'),(19,'sessions','0001_initial','2021-12-19 11:36:06.551105'),(20,'users','0002_user_nickname','2021-12-20 15:44:28.136941'),(21,'oauth','0001_initial','2021-12-24 11:20:40.981704'),(22,'home','0001_initial','2021-12-26 11:09:56.778855'),(23,'home','0002_nav','2021-12-27 12:36:06.353646'),(24,'article','0001_initial','2021-12-28 16:00:30.730089'),(25,'home','0003_alter_banner_info','2021-12-29 11:30:10.945013'),(26,'article','0002_auto_20211231_0010','2021-12-30 16:10:47.867634'),(27,'article','0003_articlepostspecial_post_time','2022-01-01 08:54:31.049830'),(28,'article','0004_auto_20220101_2224','2022-01-01 14:24:32.334828'),(29,'payments','0001_initial','2022-01-02 07:56:49.338011'),(30,'users','0003_user_money','2022-01-02 09:23:02.908153');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('uy4uj7fbd1l2lf2ifcr94unepghsa4uv','.eJxVjMEOwiAQRP-FsyFSssB69O43kF0WpGpoUtqT8d9tkx70Npn3Zt4q0rrUuPY8x1HURRl1-u2Y0jO3HciD2n3SaWrLPLLeFX3Qrm-T5Nf1cP8OKvW6rQHJeeaAZBIAi3G45ZwHsQkooLcEDhOHs6FiBTCngqGARTF-8KQ-X-5aOCc:1mzIhA:l4pihgLjf2-4fS7yb00DANJ3oeLzaGRWrN5du67ouTU','2022-01-03 13:27:16.104543');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_article`
--

DROP TABLE IF EXISTS `rr_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_article` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `title` varchar(150) NOT NULL,
  `content` longtext,
  `html_content` longtext,
  `pub_date` datetime(6) DEFAULT NULL,
  `access_pwd` varchar(15) DEFAULT NULL,
  `read_count` int DEFAULT NULL,
  `like_count` int DEFAULT NULL,
  `collect_count` int DEFAULT NULL,
  `comment_count` int DEFAULT NULL,
  `reward_count` int DEFAULT NULL,
  `is_public` tinyint(1) NOT NULL,
  `collection_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rr_article_collection_id_dd1e8119_fk_rr_article_collection_id` (`collection_id`),
  KEY `rr_article_user_id_cb59392d_fk_rr_users_id` (`user_id`),
  KEY `rr_article_title_db41b11d` (`title`),
  CONSTRAINT `rr_article_collection_id_dd1e8119_fk_rr_article_collection_id` FOREIGN KEY (`collection_id`) REFERENCES `rr_article_collection` (`id`),
  CONSTRAINT `rr_article_user_id_cb59392d_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_article`
--

LOCK TABLES `rr_article` WRITE;
/*!40000 ALTER TABLE `rr_article` DISABLE KEYS */;
INSERT INTO `rr_article` VALUES (1,1,1,0,'2021-12-30 13:19:56.153126','2022-01-01 10:15:32.038264','２０２１－１２－３０－日记','今天广东和吉林比赛，预计广东赢了','<p>今天广东和吉林比赛，预计广东赢了</p>\n',NULL,NULL,0,0,0,0,0,1,4,1),(2,0,1,0,'2021-12-30 14:17:24.296390','2022-01-01 07:20:24.577936','２０２１－１0－３０－日记','查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程。','<p>今天是2022年1月1日星期六。新年第一天</p>\n',NULL,NULL,0,0,0,0,0,1,4,1),(3,0,1,0,'2021-12-30 14:34:34.679669','2022-01-03 14:26:41.073185','２０２１－１1－３０－日记','排序就是将一组\"无序\"的记录调整为\"有序\"的记录序列。','<p>排序就是将一组&quot;无序&quot;的记录调整为&quot;有序&quot;的记录序列。</p>\n',NULL,NULL,0,0,0,0,0,1,2,1),(4,0,1,0,'2021-12-30 14:44:31.525268','2021-12-31 13:49:37.344531','２０２１－１1－1０－日记','顺序查找(Linear Search): 也叫线性查找，从列表第一个元素开始，顺序的进行搜索，直到找到元素或者搜索到列表最后一个元素为止。','顺序查找(Linear Search): 也叫线性查找，从列表第一个元素开始，顺序的进行搜索，直到找到元素或者搜索到列表最后一个元素为止。',NULL,NULL,0,0,0,0,0,0,9,1),(5,-5,1,0,'2021-12-30 16:21:54.970417','2022-01-04 02:56:00.080926','2022年1月1日新年第一天','今天是2022年1月1日星期六。新年第一天,浙江广厦和天津比赛半节42：37。值得期待下半场!!![3.jpg](1)','<p>今天是2022年1月1日星期六。新年第一天,浙江广厦和天津比赛半节42：37。值得期待下半场!!<img src=\"1\" alt=\"3.jpg\" /></p>\n',NULL,NULL,0,0,0,0,2,1,2,1),(6,0,1,0,'2021-12-30 16:21:58.149215','2021-12-30 16:21:58.149247','2021-12-30',NULL,NULL,NULL,NULL,0,0,0,0,0,0,2,1),(7,-7,1,0,'2021-12-30 16:22:45.061427','2021-12-31 13:49:22.861648','2021-12-30',NULL,NULL,NULL,NULL,0,0,0,0,0,0,5,1),(8,-8,1,0,'2022-01-03 14:09:25.315571','2022-01-05 01:33:41.478742','2022-01-03','2022年1月3日，那些年一起看球的日子你还记得吗？','<p>2022年1月3日，那些年一起看球的日子你还记得吗？</p>\n',NULL,NULL,0,0,0,0,0,1,11,7),(9,0,1,0,'2022-01-04 01:35:51.952037','2022-01-04 02:23:14.549790','2022-01-04','今天下午上课','<p>今天下午上课</p>\n',NULL,NULL,0,0,0,0,0,1,11,7),(10,0,1,0,'2022-01-04 02:27:56.710439','2022-01-05 13:14:53.575420','2022-01-04','陕西发布疫情期间群众就医指南','<p>陕西发布疫情期间群众就医指南</p>\n',NULL,NULL,0,0,0,0,0,0,1,2),(11,0,1,0,'2022-01-04 11:04:41.438805','2022-01-04 14:28:27.171792','2022-01-04','Tailwind CSS 是一个功能类优先的 CSS 框架，它集成了诸如 flex, pt-4, text-center 和 rotate-90 这样的的类，它们能直接在脚本标记语言中组合起来，构建出任何设计。','<p>Tailwind CSS 是一个功能类优先的 CSS 框架，它集成了诸如 flex, pt-4, text-center 和 rotate-90 这样的的类，它们能直接在脚本标记语言中组合起来，构建出任何设计。</p>\n',NULL,NULL,0,0,0,0,0,1,13,3),(12,0,1,0,'2022-01-04 11:07:40.925376','2022-01-04 13:31:30.115530','2022-01-04安装','学习如何在您的工程中使用 Tailwind CSS','<p>学习如何在您的工程中使用 Tailwind CSS</p>\n',NULL,NULL,0,0,0,0,0,1,13,3),(13,0,1,0,'2022-01-04 11:08:31.625190','2022-01-04 12:26:11.098647','FastAPI','FastAPI 框架，高性能，易于学习，高效编码，生产可用','<p>FastAPI 框架，高性能，易于学习，高效编码，生产可用</p>\n',NULL,NULL,0,0,0,0,0,1,13,3),(14,0,1,0,'2022-01-04 11:09:11.589053','2022-01-04 14:27:30.650571','2022-01-04','FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。','<p>FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。</p>\n',NULL,NULL,0,0,0,0,0,1,14,3),(15,0,1,0,'2022-01-04 13:13:06.868957','2022-01-04 13:18:00.432098','模式','「模式」是对事物的一种定义或描述。它并非具体的实现代码，而只是抽象的描述。','<p>「模式」是对事物的一种定义或描述。它并非具体的实现代码，而只是抽象的描述。</p>\n',NULL,NULL,0,0,0,0,0,1,13,3),(16,0,1,0,'2022-01-04 14:22:56.862549','2022-01-04 14:23:23.746221','OpenAPI 和 JSON Schema','OpenAPI 为你的 API 定义 API 模式。该模式中包含了你的 API 发送和接收的数据的定义（或称为「模式」），这些定义通过 JSON 数据模式标准 JSON Schema 所生成。','<p>OpenAPI 为你的 API 定义 API 模式。该模式中包含了你的 API 发送和接收的数据的定义（或称为「模式」），这些定义通过 JSON 数据模式标准 JSON Schema 所生成。</p>\n',NULL,NULL,0,0,0,0,0,1,15,2),(17,0,1,0,'2022-01-04 14:27:51.477463','2022-01-04 14:28:22.135660','路径','开发 API 时，「路径」是用来分离「关注点」和「资源」的主要手段。','<p>开发 API 时，「路径」是用来分离「关注点」和「资源」的主要手段。</p>\n',NULL,NULL,0,0,0,0,0,1,13,3);
/*!40000 ALTER TABLE `rr_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_article_collection`
--

DROP TABLE IF EXISTS `rr_article_collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_article_collection` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(150) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rr_article_collection_user_id_f7f0d914_fk_rr_users_id` (`user_id`),
  KEY `rr_article_collection_name_c1ada454` (`name`),
  CONSTRAINT `rr_article_collection_user_id_f7f0d914_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_article_collection`
--

LOCK TABLES `rr_article_collection` WRITE;
/*!40000 ALTER TABLE `rr_article_collection` DISABLE KEYS */;
INSERT INTO `rr_article_collection` VALUES (1,0,1,0,'2021-12-29 14:16:10.935661','2021-12-29 14:43:03.309728','我的散文',2),(2,0,1,0,'2021-12-29 14:16:41.475654','2021-12-29 15:13:15.902573','我的诗歌',1),(3,0,1,1,'2021-12-29 14:17:03.087613','2021-12-30 12:22:26.365701','测试文集',1),(4,0,1,0,'2021-12-29 14:43:16.527599','2021-12-31 12:46:55.258543','日记本',1),(5,0,1,0,'2021-12-29 14:43:16.534209','2021-12-29 14:43:16.534282','随笔',1),(6,0,1,0,'2021-12-29 16:30:04.341244','2021-12-29 16:30:04.341313','西游记',1),(9,0,1,0,'2021-12-30 12:56:10.429461','2021-12-30 12:56:43.404276','我的散文集',1),(10,0,1,0,'2021-12-31 12:46:29.559654','2021-12-31 12:46:29.559722','我的小说',1),(11,0,1,0,'2022-01-03 14:09:15.916058','2022-01-03 14:09:15.916155','日记本',7),(12,0,1,0,'2022-01-03 14:09:15.971481','2022-01-03 14:09:15.971629','随笔',7),(13,0,1,0,'2022-01-04 11:03:48.747896','2022-01-04 11:03:48.747939','日记本',3),(14,0,1,0,'2022-01-04 11:03:48.887277','2022-01-04 11:03:48.887355','随笔',3),(15,0,1,0,'2022-01-04 14:22:20.215052','2022-01-04 14:22:20.215112','日记',2),(16,0,1,0,'2022-01-04 14:27:45.421035','2022-01-04 14:27:45.421101','我的小说',3);
/*!40000 ALTER TABLE `rr_article_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_article_image`
--

DROP TABLE IF EXISTS `rr_article_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_article_image` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `group` varchar(15) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `sha1_files` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_article_image`
--

LOCK TABLES `rr_article_image` WRITE;
/*!40000 ALTER TABLE `rr_article_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `rr_article_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_article_post_special`
--

DROP TABLE IF EXISTS `rr_article_post_special`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_article_post_special` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `status` smallint NOT NULL,
  `article_id` bigint NOT NULL,
  `special_id` bigint NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `post_time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rr_article_post_special_article_id_82b11fef_fk_rr_article_id` (`article_id`),
  KEY `rr_article_post_spec_special_id_aaae7798_fk_rr_articl` (`special_id`),
  KEY `rr_article_post_special_user_id_7abc645d_fk_rr_users_id` (`user_id`),
  CONSTRAINT `rr_article_post_spec_special_id_aaae7798_fk_rr_articl` FOREIGN KEY (`special_id`) REFERENCES `rr_article_special` (`id`),
  CONSTRAINT `rr_article_post_special_article_id_82b11fef_fk_rr_article_id` FOREIGN KEY (`article_id`) REFERENCES `rr_article` (`id`),
  CONSTRAINT `rr_article_post_special_user_id_7abc645d_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_article_post_special`
--

LOCK TABLES `rr_article_post_special` WRITE;
/*!40000 ALTER TABLE `rr_article_post_special` DISABLE KEYS */;
INSERT INTO `rr_article_post_special` VALUES (8,0,1,0,'2022-01-01 13:55:18.507058','2022-01-01 13:55:18.523383',2,5,1,NULL,'2022-01-01 13:55:18.506102'),(9,0,1,0,'2022-01-01 13:55:20.961110','2022-01-01 13:55:20.972837',2,5,2,NULL,'2022-01-01 13:55:20.960397');
/*!40000 ALTER TABLE `rr_article_post_special` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_article_special`
--

DROP TABLE IF EXISTS `rr_article_special`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_article_special` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `notice` longtext,
  `article_count` int DEFAULT NULL,
  `follow_count` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `rr_article_special_user_id_222f8703_fk_rr_users_id` (`user_id`),
  CONSTRAINT `rr_article_special_user_id_222f8703_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_article_special`
--

LOCK TABLES `rr_article_special` WRITE;
/*!40000 ALTER TABLE `rr_article_special` DISABLE KEYS */;
INSERT INTO `rr_article_special` VALUES (1,0,1,0,'2022-01-01 08:27:39.044094','2022-01-01 14:27:40.801808','group1/M00/00/00/wKi2g2HQZNyAAnazAAAYQrHhbAc3506355','相亲相爱',0,0,1,'相亲'),(2,1,1,0,'2022-01-01 08:29:15.513292','2022-01-01 14:27:59.972485','group1/M00/00/00/wKi2g2HQZO-AT2hTAAAchwx86tI4835400','相亲相爱',0,0,1,'相爱'),(3,2,1,0,'2022-01-01 08:29:15.513292','2022-01-01 14:28:11.485490','group1/M00/00/00/wKi2g2HQZPuAWL4iAAAYQrHhbAc7746982','篮球',0,0,1,'篮球'),(4,2,1,0,'2022-01-01 08:29:15.513292','2022-01-01 14:28:21.235284','group1/M00/00/00/wKi2g2HQZQWAVsJHAAAchwx86tI1442177','旅游',0,0,2,'旅游');
/*!40000 ALTER TABLE `rr_article_special` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_banner`
--

DROP TABLE IF EXISTS `rr_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_banner` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(150) NOT NULL,
  `info` longtext,
  `link` varchar(150) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `is_http` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_banner`
--

LOCK TABLES `rr_banner` WRITE;
/*!40000 ALTER TABLE `rr_banner` DISABLE KEYS */;
INSERT INTO `rr_banner` VALUES (1,0,1,0,'2021-12-26 13:17:58.454833','2022-01-01 09:59:58.296151','第一张图片','','/user/login','group1/M00/00/00/wKi2g2HLJmqAD1gBAAERbEdqJA02806526','2021-12-26 13:16:28.000000','2022-03-01 13:16:35.000000',0),(2,0,1,0,'2021-12-26 14:07:39.854254','2022-01-01 10:00:19.810315','第二张图片','李老板：15012345686','http://www.baidu.com','group1/M00/00/00/wKi2g2HLKHOAQaESAABe3svUh6Y1983027','2021-12-26 14:07:37.000000','2022-03-01 14:07:34.000000',1),(3,0,1,0,'2021-12-26 14:13:19.511477','2022-01-01 10:00:36.699991','第三张图片','马老师：13012345673','http://www.tmall.com','group1/M00/00/00/wKi2g2HLKEOASdxnAC4IreETzig2273805','2021-12-26 14:12:50.000000','2022-03-01 14:12:53.000000',1);
/*!40000 ALTER TABLE `rr_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_nav`
--

DROP TABLE IF EXISTS `rr_nav`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_nav` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(150) NOT NULL,
  `icon` varchar(150) NOT NULL,
  `link` varchar(150) DEFAULT NULL,
  `position` int NOT NULL,
  `is_http` tinyint(1) NOT NULL,
  `pid_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rr_nav_pid_id_f4276f79_fk_rr_nav_id` (`pid_id`),
  CONSTRAINT `rr_nav_pid_id_f4276f79_fk_rr_nav_id` FOREIGN KEY (`pid_id`) REFERENCES `rr_nav` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_nav`
--

LOCK TABLES `rr_nav` WRITE;
/*!40000 ALTER TABLE `rr_nav` DISABLE KEYS */;
INSERT INTO `rr_nav` VALUES (1,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.153052','关注','ic-chats','http://www.baidu.com',1,1,NULL),(2,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 14:10:59.433085','消息','ic-navigation-notification','http://www.baidu.com',1,1,NULL),(3,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149463','评论','ic-comments','http://www.baidu.com',1,1,1),(4,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149663','收藏','ic-chats','http://www.baidu.com',1,1,1),(5,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149468','简信','ic-requests','http://www.baidu.com',1,1,1),(6,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149463','投稿','ic-likes','http://www.baidu.com',1,1,1),(7,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149463','喜欢','ic-follows','http://www.baidu.com',1,1,1),(8,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149463','关注','ic-money','http://www.baidu.com',1,1,1),(9,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149463','赞赏','ic-others','http://www.baidu.com',1,1,2),(10,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149463','路飞学城','','http://www.luffycity.com',2,1,NULL),(11,0,1,0,'2021-12-27 12:54:19.149463','2021-12-27 12:54:19.149463','百度','','http://www.baidu.com',2,1,NULL),(12,0,1,0,'2021-12-27 15:02:06.266992','2021-12-27 15:02:06.267077','关于荏苒','ic-chats','/about',2,0,NULL);
/*!40000 ALTER TABLE `rr_nav` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_oauth_user`
--

DROP TABLE IF EXISTS `rr_oauth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_oauth_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `openid` varchar(64) NOT NULL,
  `name` int NOT NULL,
  `access_token` varchar(500) NOT NULL,
  `refresh_token` varchar(500) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `openid` (`openid`),
  KEY `rr_oauth_user_user_id_b539273d_fk_rr_users_id` (`user_id`),
  CONSTRAINT `rr_oauth_user_user_id_b539273d_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_oauth_user`
--

LOCK TABLES `rr_oauth_user` WRITE;
/*!40000 ALTER TABLE `rr_oauth_user` DISABLE KEYS */;
INSERT INTO `rr_oauth_user` VALUES (1,NULL,1,0,'2021-12-25 21:16:44.000000','2021-12-25 21:17:06.000000','5AA16A7315CBB11295F01FB2A3D8F413',1,'bbb','aaa',1),(2,0,1,0,'2021-12-26 07:04:41.011800','2021-12-26 07:04:41.011845','',1,'17C7E3DFE13DF5487908A0E459893673','816214081C91E24A00F389ADEC874095',7),(3,0,1,0,'2021-12-26 08:13:19.323637','2021-12-26 08:13:19.323689','5AA16A7311CBB11295F01FB2A3D8F413',1,'16B8B9EB90509A508B8DE786BD434D3D','07DAA5C04D825053B76C84C6785723BA',8);
/*!40000 ALTER TABLE `rr_oauth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_special_focus`
--

DROP TABLE IF EXISTS `rr_special_focus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_special_focus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `special_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rr_special_focus_special_id_2898586a_fk_rr_article_special_id` (`special_id`),
  KEY `rr_special_focus_user_id_ce74c41a_fk_rr_users_id` (`user_id`),
  CONSTRAINT `rr_special_focus_special_id_2898586a_fk_rr_article_special_id` FOREIGN KEY (`special_id`) REFERENCES `rr_article_special` (`id`),
  CONSTRAINT `rr_special_focus_user_id_ce74c41a_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_special_focus`
--

LOCK TABLES `rr_special_focus` WRITE;
/*!40000 ALTER TABLE `rr_special_focus` DISABLE KEYS */;
/*!40000 ALTER TABLE `rr_special_focus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_special_manager`
--

DROP TABLE IF EXISTS `rr_special_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_special_manager` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `special_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rr_special_manager_special_id_30a3bd3a_fk_rr_article_special_id` (`special_id`),
  KEY `rr_special_manager_user_id_afae71a9_fk_rr_users_id` (`user_id`),
  CONSTRAINT `rr_special_manager_special_id_30a3bd3a_fk_rr_article_special_id` FOREIGN KEY (`special_id`) REFERENCES `rr_article_special` (`id`),
  CONSTRAINT `rr_special_manager_user_id_afae71a9_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_special_manager`
--

LOCK TABLES `rr_special_manager` WRITE;
/*!40000 ALTER TABLE `rr_special_manager` DISABLE KEYS */;
INSERT INTO `rr_special_manager` VALUES (1,0,1,0,'2022-01-01 08:35:28.645931','2022-01-01 08:35:28.645962',1,1),(2,0,1,0,'2022-01-01 08:35:33.216625','2022-01-01 08:35:33.216656',2,1),(3,0,1,0,'2022-01-01 08:35:37.345065','2022-01-01 08:35:37.345094',3,1);
/*!40000 ALTER TABLE `rr_special_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_user_reward`
--

DROP TABLE IF EXISTS `rr_user_reward`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_user_reward` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `money` decimal(6,2) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `reward_type` int NOT NULL,
  `message` longtext,
  `trade_no` varchar(255) DEFAULT NULL,
  `out_trade_no` varchar(255) DEFAULT NULL,
  `article_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rr_user_reward_article_id_a09b9fa2_fk_rr_article_id` (`article_id`),
  KEY `rr_user_reward_user_id_13ab46df_fk_rr_users_id` (`user_id`),
  CONSTRAINT `rr_user_reward_article_id_a09b9fa2_fk_rr_article_id` FOREIGN KEY (`article_id`) REFERENCES `rr_article` (`id`),
  CONSTRAINT `rr_user_reward_user_id_13ab46df_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_user_reward`
--

LOCK TABLES `rr_user_reward` WRITE;
/*!40000 ALTER TABLE `rr_user_reward` DISABLE KEYS */;
INSERT INTO `rr_user_reward` VALUES (1,0,1,0,'2022-01-02 08:29:27.023545','2022-01-02 08:29:27.023601',5.00,0,1,'加油','20220102082927000001474383',NULL,5,1),(2,0,1,0,'2022-01-02 10:25:16.446536','2022-01-02 10:25:16.447072',5.00,0,1,'加油',NULL,'20220102102516000001530489',5,1),(3,0,1,0,'2022-01-02 10:26:34.768071','2022-01-02 10:26:34.768138',5.00,0,1,'',NULL,'20220102102634000001567753',3,1),(4,0,1,0,'2022-01-02 10:30:02.735519','2022-01-02 10:30:02.735562',2.00,0,1,'',NULL,'20220102103002000001504685',5,1),(5,0,1,0,'2022-01-02 10:37:14.712001','2022-01-02 10:37:14.712156',2.00,0,1,'',NULL,'20220102103714000001046999',5,1),(6,0,1,0,'2022-01-02 10:57:15.134311','2022-01-02 10:58:00.603685',2.00,1,1,'','2022010222001484150502356648','20220102105715000001019189',5,1),(7,0,1,0,'2022-01-02 11:16:00.166056','2022-01-02 11:16:00.166102',5.00,0,1,'',NULL,'20220102111600000001481414',5,1),(8,0,1,0,'2022-01-02 11:27:39.064604','2022-01-02 11:27:39.064782',10.00,0,1,'',NULL,'20220102112739000001583444',5,1),(9,0,1,0,'2022-01-02 11:53:16.008715','2022-01-02 11:53:16.008807',5.00,0,1,'',NULL,'20220102115316000001453529',5,1),(10,0,1,0,'2022-01-02 12:08:24.648425','2022-01-02 12:08:24.648495',5.00,0,1,'',NULL,'20220102120824000001105113',5,1),(11,0,1,0,'2022-01-02 12:10:24.829079','2022-01-02 12:10:24.829125',5.00,0,1,'',NULL,'20220102121024000001590267',3,1),(12,0,1,0,'2022-01-02 12:17:13.290555','2022-01-02 12:17:13.290611',2.00,0,1,'',NULL,'20220102121713000001830146',3,1),(13,0,1,0,'2022-01-02 12:21:57.987244','2022-01-02 12:21:57.987292',2.00,0,1,'',NULL,'20220102122157000001855578',3,1),(14,0,1,0,'2022-01-02 12:27:00.615856','2022-01-02 12:27:00.615988',2.00,0,1,'',NULL,'20220102122700000001754683',5,1),(15,0,1,0,'2022-01-02 13:11:36.318797','2022-01-02 13:12:34.545808',2.00,1,1,'','2022010222001484150502356764','20220102131136000001914245',5,1),(16,0,1,0,'2022-01-02 14:20:23.576942','2022-01-02 14:20:23.577013',10.00,1,1,'',NULL,'20220102142023000001633302',3,1),(17,0,1,0,'2022-01-03 12:06:33.883718','2022-01-03 12:06:33.883786',10.00,1,1,'',NULL,'20220103120633000001951584',5,1);
/*!40000 ALTER TABLE `rr_user_reward` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_users`
--

DROP TABLE IF EXISTS `rr_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `wechat` varchar(100) DEFAULT NULL,
  `alipay` varchar(100) DEFAULT NULL,
  `qq_number` varchar(11) DEFAULT NULL,
  `nickname` varchar(20) DEFAULT NULL,
  `money` decimal(8,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `wechat` (`wechat`),
  UNIQUE KEY `alipay` (`alipay`),
  UNIQUE KEY `qq_number` (`qq_number`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_users`
--

LOCK TABLES `rr_users` WRITE;
/*!40000 ALTER TABLE `rr_users` DISABLE KEYS */;
INSERT INTO `rr_users` VALUES (1,'pbkdf2_sha256$260000$xl4lKvDGJajvGDmgYeqbf6$Fd5h98w8jjw62puNr6425J0L/o3tvHGqVgoac+V/FxA=','2021-12-29 14:42:44.000000',1,'root','','','1746259122@qq.com',1,1,'2021-12-19 14:55:46.000000','17260808699','group1/M00/00/00/wKi2g2HQdC2AMNzlAAAchwx86tI0423073',NULL,NULL,NULL,NULL,4.00),(2,'pbkdf2_sha256$260000$89RYE9vlLrzbmZLPOu7r4C$29VlG2iXU9WF333ZUdULYPXQMoxYvF6Edk7KxGI3aTw=',NULL,0,'13772823138','','','1746259155@qq.com',0,1,'2021-12-20 16:11:52.016843','13772823138','',NULL,NULL,NULL,'小兵',0.00),(3,'pbkdf2_sha256$260000$1HDDUQBgzd0tygd4tJXRn8$hYZgmcNpb1cG69qY4Cgy/Y4JChKKKCW3v5TQEMWKycg=',NULL,0,'15009282073','','','1746259165@qq.com',0,1,'2021-12-22 14:09:50.953811','15009282073','',NULL,NULL,NULL,'小白',0.00),(4,'pbkdf2_sha256$260000$mxkdpVfymsQ9VK6gpJBVqw$09dY7u1RelYOZEtYp8ZnaGriOnQNMAp/ymiEejH+Y/E=',NULL,0,'17260808688','','','1746259455@qq.com',0,1,'2021-12-22 16:17:53.956914','17260808697','',NULL,NULL,NULL,'小乔',0.00),(7,'pbkdf2_sha256$260000$Q5riVeDt6MxB2aLeGoSDVm$offVj6nd2ZNFb2t97z2G06G9RugU9m1dxfcOxtgWQtk=',NULL,0,'17260808693','','','qpj20219999@163.com',0,1,'2021-12-23 15:17:48.737659','17260808696','',NULL,NULL,NULL,'哈哈',0.00),(8,'pbkdf2_sha256$260000$t6hQnyJoH4vWizaRvHkv9a$zBXARRwIz/prnwwVdj2bPcsJHQH65OmcmrzjhBZen5U=',NULL,0,'13778899223','','','',0,1,'2021-12-26 08:13:19.006741','13778899223','',NULL,NULL,NULL,'小鱼',0.00);
/*!40000 ALTER TABLE `rr_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_users_groups`
--

DROP TABLE IF EXISTS `rr_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_users_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rr_users_groups_user_id_group_id_0c585a2c_uniq` (`user_id`,`group_id`),
  KEY `rr_users_groups_group_id_806137b1_fk_auth_group_id` (`group_id`),
  CONSTRAINT `rr_users_groups_group_id_806137b1_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `rr_users_groups_user_id_5a8f3a96_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_users_groups`
--

LOCK TABLES `rr_users_groups` WRITE;
/*!40000 ALTER TABLE `rr_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `rr_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rr_users_user_permissions`
--

DROP TABLE IF EXISTS `rr_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rr_users_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rr_users_user_permissions_user_id_permission_id_0ea21531_uniq` (`user_id`,`permission_id`),
  KEY `rr_users_user_permis_permission_id_1ffb272b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `rr_users_user_permis_permission_id_1ffb272b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `rr_users_user_permissions_user_id_6a96e898_fk_rr_users_id` FOREIGN KEY (`user_id`) REFERENCES `rr_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rr_users_user_permissions`
--

LOCK TABLES `rr_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `rr_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `rr_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-06 11:20:26
