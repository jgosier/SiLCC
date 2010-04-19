DROP TABLE IF EXISTS `places`;
CREATE TABLE `places` (
  `id` mediumint(9) NOT NULL auto_increment,
  `name` varchar(128) NOT NULL,
  `name_ascii` varchar(128) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
