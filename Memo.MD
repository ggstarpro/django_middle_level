# 下記テーブルを作成してください

CREATE TABLE `base_item` (
  `id` varchar(22) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` int(10) unsigned NOT NULL,
  `stock` int(10) unsigned NOT NULL,
  `description` longtext NOT NULL,
  `sold_count` int(10) unsigned NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `image` varchar(100) NOT NULL,
  `category_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_item_category_id_4e814b7e_fk_base_category_slug` (`category_id`),
  CONSTRAINT `base_item_category_id_4e814b7e_fk_base_category_slug` FOREIGN KEY (`category_id`) REFERENCES `base_category` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `base_category` (
  `slug` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `base_tag` (
  `slug` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `base_item_tags` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `item_id` varchar(22) NOT NULL,
  `tag_id` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_item_tags_item_id_tag_id_3e8a01e4_uniq` (`item_id`,`tag_id`),
  KEY `base_item_tags_tag_id_7a331bcc_fk_base_tag_slug` (`tag_id`),
  CONSTRAINT `base_item_tags_item_id_d87136b4_fk_base_item_id` FOREIGN KEY (`item_id`) REFERENCES `base_item` (`id`),
  CONSTRAINT `base_item_tags_tag_id_7a331bcc_fk_base_tag_slug` FOREIGN KEY (`tag_id`) REFERENCES `base_tag` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8