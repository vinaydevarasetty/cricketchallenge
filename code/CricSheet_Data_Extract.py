import os
# load pandas
import pandas as pd

#listing file names in directory 
list_of_files =[]
for path, subdirs, files in os.walk(r'C:/Users/vdevarasetty/Desktop/Learnings/Java/Hackathon/CSV_Data/odi_csv_male/test'):
    for filename in files:
        list_of_files.append((filename + os.linesep).strip("\r\n")) 
  
for a in range(len(list_of_files)):
    b_info='C:/Users/vdevarasetty/Desktop/Learnings/Java/Hackathon/CSV_Data/odi_csv_male/test/subset/info/info_'+list_of_files[a]
    b_ballwise='C:/Users/vdevarasetty/Desktop/Learnings/Java/Hackathon/CSV_Data/odi_csv_male/test/subset/ballbyball/'+list_of_files[a]
    data = pd.read_csv('C:/Users/vdevarasetty/Desktop/Learnings/Java/Hackathon/CSV_Data/odi_csv_male/test/'+list_of_files[a],encoding='cp1252',names=list('abcdefghijk'),skiprows=1,header=None)
    is_info=(data["a"]=='info')
    non_info=(data["a"]!='info')
	#separate data
    data_info=data[is_info]
    data_non_info=data[non_info]
	##date_played
    date_info=pd.DataFrame(data_info.iloc[[4]])
    #print(date_info)
    date_played=date_info.iloc[0,2]
    #print(type(date_played)) 
	#converting date to intger
    date_played_int=int(date_played[0:4]+date_played[5:7]+date_played[8:10])
    #print(type(date_played_int))
	##teams played
    team_info=data_info.loc[0:1]
    #print(team_info)
    text=''
    for value in team_info["c"]:
        if text=='':
	         text=text+value
        else:
             text=text+'_'+value	
    if date_played_int > 20081231 and (text =='Australia_India' or text == 'India_Australia'):
        print("processing in progress.....")
        data_info.to_csv(b_info)
		#add teams played and date played
        data_info['teams_playing']=text
        data_non_info['teams_playing']=text
        data_info['date_played']=date_played
        data_non_info['date_played']=date_played
        data_non_info.to_csv(b_ballwise)
        data_info.to_csv(b_info)
		
	

	
	
	
