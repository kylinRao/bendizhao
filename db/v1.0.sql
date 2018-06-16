-- DROP TABLE IF EXISTS phone;
-- CREATE TABLE phone(
-- -- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- updateTime DATETIME,
-- phone  TEXT UNIQUE --   使用者的电话号码，方便管理者联系到使用者
--
-- );
DROP TABLE IF EXISTS inviteRelationship;
CREATE TABLE inviteRelationship(
phone  TEXT  UNIQUE ,--   使用者的电话号码，方便管理者联系到使用者
inviteByCode TEXT, -- 使用哪个邀请码的
invitedTime DATE ,--被邀请的时间
lastUseDay DATE --上一次使用时间
);
CREATE INDEX inviteRelationship_phone
ON inviteRelationship (phone);