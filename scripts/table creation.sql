--Transfer the files(ball by ball data) generated using Python to hdfs from Local

--Hive External Table Created
create external table if not exists AusInd_ODI_Data
(
SNO int,
Ball_Description Varchar(100),
Inns int,
Ball_Number double,
Country Varchar(100),
Batsman Varchar(100),
Non_Striker_Batsman Varchar(100),
Bowler Varchar(100),
Runs int,
Extras int,
Mode_Of_Dismissal Varchar(100),
Player_Dismissed Varchar(100),
Teams_Involved Varchar(100),
Date_Played Varchar(12)
)
Row format delimited fields terminated by ','
location 'hdfs://quickstart.cloudera:8020/user/cloudera/Hackathon/Aus_Ind_ODI_Data/'
TBLPROPERTIES('skip.header.line.count'='1');