/*Dismissal Types*/
SELECT DISTINCT Mode_Of_Dismissal FROM AusInd_ODI_Data;

/* 
--output--
bowled
caught
caught and bowled
lbw
run out
stumped
*/

/*Batsman available in two teams*/
SELECT DISTINCT Batsman,Country FROM AusInd_ODI_Data; 

/*Runs Scored by Each Batsman who are playing in the current series from all the list of players available in the data */
SELECT Batsman,Country,Date_Played,Inns,SUM(Runs) AS Runs FROM AusInd_ODI_Data 
WHERE Batsman in 
('GJ Maxwell',
'SE Marsh',
'NM Coulter-Nile',
'AJ Finch',
'Mohammed Shami',
'MS Dhoni',
'AT Rayudu',
'RG Sharma',
'S Dhawan',
'V Kohli')
GROUP BY Batsman,Country,Date_Played,Inns
ORDER BY Batsman,Date_Played DESC;


/*Bowling Data*/
SELECT BOWLER,Country,Date_Played,Inns,COUNT(*) AS Wickets FROM AusInd_ODI_Data
WHERE Mode_Of_Dismissal IN 
('bowled',
'caught',
'caught and bowled',
'lbw')
GROUP BY BOWLER,Country,Date_Played,Inns
ORDER BY Bowler,date_played DESC


