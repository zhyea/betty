-- mysql


DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS icons;
DROP TABLE IF EXISTS links;

-- 用户表
CREATE TABLE user (
  id           INT UNIQUE         NOT NULL PRIMARY KEY               AUTO_INCREMENT,
  username     VARCHAR(32) UNIQUE NOT NULL,
  password     VARCHAR(32)        NOT NULL,
  display_name VARCHAR(32),
  status       INT                NOT NULL                           DEFAULT 1,
  add_time     DATE,
  operate_time TIMESTAMP          NOT NULL                           DEFAULT current_timestamp
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8;

-- 分类表
CREATE TABLE category (
  id           INT UNIQUE         NOT NULL PRIMARY KEY      AUTO_INCREMENT,
  parent       INT,
  name         VARCHAR(32)        NOT NULL,
  slug         VARCHAR(32)        NOT NULL,
  user_id      INT                NOT NULL,
  add_time     DATE,
  operate_time TIMESTAMP          NOT NULL                  DEFAULT current_timestamp
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8;

-- 链接表
CREATE TABLE links (
  id           INT UNIQUE         NOT NULL PRIMARY KEY        AUTO_INCREMENT,
  name         VARCHAR(32)        NOT NULL,
  url          VARCHAR(128)       NOT NULL,
  remark       VARCHAR(256)       NOT NULL,
  cat_id       INT                NOT NULL,
  ico_id       INT,
  user_id      INT                NOT NULL,
  add_time     DATE,
  operate_time TIMESTAMP          NOT NULL                    DEFAULT current_timestamp
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8;

-- 图标表
CREATE TABLE icons (
  id           INT UNIQUE         NOT NULL PRIMARY KEY        AUTO_INCREMENT,
  path         VARCHAR(128)       NOT NULL,
  remark       VARCHAR(128)       NOT NULL,
  user_id      INT                NOT NULL,
  add_time     DATE,
  operate_time TIMESTAMP          NOT NULL                    DEFAULT current_timestamp
)
  ENGINE = MyISAM
  DEFAULT CHARSET = utf8;