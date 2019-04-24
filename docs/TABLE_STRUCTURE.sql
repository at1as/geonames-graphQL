-- Use this to create Geonames database tables

-- CREATE DATABASE

CREATE DATABASE geonames;
USE geonames;


-- CREATE TABLES

-- Tables contents from Geonames Open Source dataset
-- Source: http://download.geonames.org/export/dump/

CREATE TABLE `admin1_codes` (
  code          CHAR(12)  NOT NULL,
  name          TEXT      DEFAULT NULL,
  asciiname     TEXT      DEFAULT NULL,
  geoname_id    INT(11)   NOT NULL,
  KEY `code` (`code`),
  FOREIGN KEY (`geoname_id`) REFERENCES geoname(geoname_id) ON DELETE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `admin2_codes` (
  code          CHAR(30)  NOT NULL,
  name          TEXT      DEFAULT NULL,
  asciiname     TEXT      DEFAULT NULL,
  geoname_id    INT(11)   NOT NULL,
  KEY `code` (`code`),
  KEY `name` (`name`(80)),
  KEY `asciiname` (`asciiname`(80)),
  FOREIGN KEY (`geoname_id`) REFERENCES geoname(geoname_id) ON DELETE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `admin5_codes` (
  geoname_id    INT(11)       NOT NULL,
  admin5_code   VARCHAR(40)   NOT NULL,
  FOREIGN KEY (`geoname_id`)  REFERENCES geoname(geoname_id) ON DELETE CASCADE
) CHARACTER SET utf8mb4;

-- Remark : the field 'alternatenames' in the table 'geoname' is a short version of the 'alternatenames' table without links and postal codes but with ascii transliterations. You probably don't need both. 
-- If you don't need to know the language of a name variant, the field 'alternatenames' will be sufficient. If you need to know the language
-- of a name variant, then you will need to load the table 'alternatenames' and you can drop the column in the geoname table.

CREATE TABLE `alternatenames` (
  alternatename_id    INT(11)       NOT NULL        COMMENT "the id of this alternate name, int", 
  geoname_id          INT(11)       NOT NULL        COMMENT "geonameId referring to id in table 'geoname', int",
  iso_language        VARCHAR(7)                    COMMENT "iso 639 language code 2- or 3-characters; 4-characters 'post' for postal codes and 'iata','icao' and faac for airport codes, fr_1793 for French Revolution names,  abbr for abbreviation, link to a website (mostly to wikipedia), wkdt for the wikidataid, varchar(7)",
  alternatename       VARCHAR(400),                 COMMENT "alternate name or name variant"
  is_preferred_name   CHAR(1)                       COMMENT "'1', if this alternate name is an official/preferred name",
  is_shortname        CHAR(1)                       COMMENT "'1', if this is a short name like 'California' for 'State of California'",
  is_colloquial       CHAR(1)                       COMMENT "'1', if this alternate name is a colloquial or slang term",
  is_historic         CHAR(1)                       COMMENT "'1', if this alternate name is historic and was used in the past",
  from                DATE          DEFAULT NULL    COMMENT "from period when the name was used",
  to                  DATE          DEFAULT NULL    COMMENT "to period when the name was used"
  PRIMARY KEY(`alternatename_id`),
  KEY `iso_anguage` (`iso_language`),
  KEY `alternatename` (`alternatename`),
  FOREIGN KEY (`geoname_id`)        REFERENCES geoname(geoname_id) ON DELETE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `boundaries` (
  geoname_id        INT(11)           NOT NULL,
  geoJson           VARCHAR(1000000)  COMMENT "The boundary in geoJson format (max length in dataset: 466,527). This can be JSON type in MySQL 5.7.8+",
  FOREIGN KEY (`geoname_id`)          REFERENCES geoname(geoname_id) ON DELETE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `continent_codes` (
  `code`        CHAR(2)       NOT NULL,
  `name`        VARCHAR(20)   NOT NULL,
  `geoname_id`  INT(11)       NOT NULL,
  KEY `code` (`code`),
  KEY `name` (`name`),
  FOREIGN KEY (`geoname_id`)  REFERENCES geoname(geoname_id) ON DELETE CASCADE
) CHARACTER SET utf8mb4;

CREATE TABLE `country_info` (
  `iso_alpha2`            CHAR(2)       NOT NULL,
  `iso_alpha3`            CHAR(3)       NOT NULL,
  `iso_numeric`           INT(11)       DEFAULT NULL,
  `fips_code`             VARCHAR(3)    DEFAULT NULL,
  `name`                  VARCHAR(200)  DEFAULT NULL,
  `capital`               VARCHAR(200)  DEFAULT NULL,
  `area_in_sq_km`         DOUBLE        DEFAULT NULL,
  `population`            INT(11)       DEFAULT NULL,
  `continent`             CHAR(2)       DEFAULT NULL,
  `tld`                   VARCHAR(3)    DEFAULT NULL,
  `currency`              CHAR(3)       DEFAULT NULL,
  `currency_name`         VARCHAR(20)   DEFAULT NULL,
  `phone`                 VARCHAR(20)   DEFAULT NULL,
  `postal_code_format`    VARCHAR(100)  DEFAULT NULL,
  `postal_code_regex`     VARCHAR(255)  DEFAULT NULL,
  `languages`             VARCHAR(200)  DEFAULT NULL,
  `geoname_id`            INT(11)       DEFAULT NULL,
  `neighbours`            VARCHAR(100)  DEFAULT NULL,
  `equivalent_fips_code`  VARCHAR(10)   DEFAULT NULL,
  KEY `iso_alpha2`  (`iso_alpha2`),
  KEY `iso_alpha3`  (`iso_alpha3`),
  KEY `iso_numeric` (`iso_numeric`),
  KEY `fips_code`   (`fips_code`),
  KEY `geoname_id`  (`geoname_id`),
  KEY `name`        (`name`)
) CHARACTER SET utf8mb4;

-- feature classes:
-- A: country, state, region,...
-- H: stream, lake, ...
-- L: parks,area, ...
-- P: city, village,...
-- R: road, railroad 
-- S: spot, building, farm
-- T: mountain,hill,rock,... 
-- U: undersea
-- V: forest,heath,...
CREATE TABLE `feature_codes` (
  code        VARCHAR(7)    NOT NULL,
  name        VARCHAR(200)  NOT NULL,
  description TEXT
) CHARACTER SET utf8mb4;

CREATE TABLE `geoname` (
  geoname_id        INT(11) NOT NULL          COMMENT "integer id of record in geonames database",
  name              VARCHAR(200) NOT NULL     COMMENT "name of geographical point (utf8) VARCHAR(200)",
  asciiname         VARCHAR(200)              COMMENT "name of geographical point in plain ascii characters, VARCHAR(200)",
  alternatenames    VARCHAR(10000)            COMMENT "alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, VARCHAR(10000)",
  latitude          DECIMAL(8,5)              COMMENT "latitude in decimal degrees (wgs84)",
  longitude         DECIMAL(8,5)              COMMENT "longitude in decimal degrees (wgs84)",
  feature_class     CHAR(1) NOT NULL          COMMENT "see http://www.geonames.org/export/codes.html",
  feature_code      VARCHAR(10) NOT NULL      COMMENT "see http://www.geonames.org/export/codes.html",
  country_code      CHAR(2) NOT NULL          COMMENT "ISO-3166 2-letter country code, 2 characters",
  cc2               VARCHAR(200)              COMMENT "alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters",
  admin1_code       VARCHAR(20)               COMMENT "fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; VARCHAR(20)",
  admin2_code       VARCHAR(80)               COMMENT "code for the second administrative division, a county in the US, see file admin2Codes.txt; VARCHAR(80) ",
  admin3_code       VARCHAR(20)               COMMENT "code for third level administrative division, VARCHAR(20)",
  admin4_code       VARCHAR(20)               COMMENT "code for fourth level administrative division, VARCHAR(20)",
  population        DECIMAL(11,0)             COMMENT "bigint (8 byte int) ",
  elevation         VARCHAR(10)               COMMENT "in meters, integer",
  dem               BIGINT                    COMMENT "digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.",
  timezone          VARCHAR(40)               COMMENT "the timezone id (see file timeZone.txt) VARCHAR(40)",
  modification_date DATE                      COMMENT "date of last modification in yyyy-MM-dd format",
  PRIMARY KEY(geoname_id),
  KEY `admin1_code` (`admin1_code`),
  KEY `admin2_code` (`admin2_code`),
  KEY `admin3_code` (`admin3_code`),
  KEY `admin4_code` (`admin4_code`),
  KEY `asciiname` (`asciiname`),
  KEY `country_code` (`country_code`),
  KEY `feature_class` (`feature_class`),
  KEY `feature_code` (`feature_code`),
  KEY `latitude`  (`latitude`),
  KEY `longitude` (`longitude`),
  KEY `name` (`name`),
  KEY `population` (`population`)
) CHARACTER SET utf8mb4;

CREATE TABLE `hierarchy` (
  `parent_id`   INT(11)       NOT NULL,
  `child_id`    INT(11)       NOT NULL,
  `type`        VARCHAR(50)   DEFAULT NULL,
  FOREIGN KEY (`parent_id`)   REFERENCES geoname(geoname_id) ON DELETE CASCADE,
  FOREIGN KEY (`child_id`)    REFERENCES geoname(geoname_id) ON DELETE CASCADE,
  KEY `type` (`type`)
) CHARACTER SET utf8mb4;

CREATE TABLE `iso_language_codes` (
  `iso_639_3`     CHAR(3)         NOT NULL,
  `iso_639_2`     VARCHAR(50)     DEFAULT NULL,
  `iso_639_1`     VARCHAR(10)     DEFAULT NULL,
  `language_name` VARCHAR(100)    DEFAULT NULL
) CHARACTER SET utf8mb4;

-- For many countries lat/lng are determined with an algorithm that searches the place names in the main geonames database 
-- using administrative divisions and numerical vicinity of the postal codes as factors in the disambiguation of place names. 
-- For postal codes and place name for which no corresponding toponym in the main geonames database could be found an average 
-- lat/lng of 'neighbouring' postal codes is calculated.
-- Source: http://download.geonames.org/export/zip/

CREATE TABLE `postal_codes` (
  country_code    CHAR(2)         COMMENT "iso country code, 2 characters",
  postal_code     VARCHAR(20),
  place_name      VARCHAR(180),
  admin_name1     VARCHAR(100)    COMMENT "1st order subdivision (state)",
  admin_code1     VARCHAR(20)     COMMENT "1st order subdivision (state)",
  admin_name2     VARCHAR(100)    COMMENT "2nd order subdivision (county/province)",
  admin_code2     VARCHAR(20)     COMMENT "2nd order subdivision (county/province)",
  admin_name3     VARCHAR(100)    COMMENT "3rd order subdivision (community)",
  admin_code3     VARCHAR(20)     COMMENT "3rd order subdivision (community)",
  latitude        DECIMAL(8,5)    COMMENT "estimated latitude (wgs84)",
  longitude       DECIMAL(8,5)    COMMENT "estimated longitude (wgs84)",
  accuracy        CHAR(2)         COMMENT "accuracy of lat/lng from 1=estimated to 6=centroid",
  KEY `country_code`  (`country_code`),
  KEY `postal_code`   (`postal_code`),
  KEY `place_name`    (`place_name`),
  KEY `admin_code1`   (`admin_code1`),
  KEY `admin_code2`   (`admin_code2`),
  KEY `admin_code3`   (`admin_code3`)
) CHARACTER SET utf8mb4;

CREATE TABLE `timezones` (
  `country_code`  CHAR(2)         NOT NULL,
  `timezone_id`   VARCHAR(200)    NOT NULL,
  `GMT_offset`    DECIMAL(3,1)    DEFAULT NULL,
  `DST_offset`    DECIMAL(3,1)    DEFAULT NULL,
  `raw_offset`    DECIMAL(3,1)    DEFAULT NULL
) CHARACTER SET utf8mb4;

CREATE TABLE `usertags` (
  geoname_id      INT(11)         NOT NULL,
  tag             VARCHAR(100),
  FOREIGN KEY (`geoname_id`)      REFERENCES geoname(geoname_id) ON DELETE CASCADE
) CHARACTER SET utf8mb4;

