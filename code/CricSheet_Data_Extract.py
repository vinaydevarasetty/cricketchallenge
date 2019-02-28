#!/usr/bin/env python
# coding: utf-8

# In[141]:
'''''
Below Script is used for processing the csv data downloaded from the cricsheet website.
(https://cricsheet.org/downloads/odi_csv_male.zip)

Note:
Each csv file data is in the below format :
1)Info Section:Details for a Match like Venue,Winner,Ground,Date Played etc.,
2)Ball Wise Details:All the detailed information like ball wise 

Pre-requisite: 
1) Data Downloaded needs to be unzipped in the source folder
2) 2 Folders which hold the Ballwise Details and Information corresponding to each Match 
   like Venue,Winner,Ground,Date Played etc., needs to be created.

Functionality::
This script process the entire data present in the source location.
and generate the data corresponding to the matches played between India and Australia 
alone between 2009 and 2017.

Processed files are available in the folder information specified in the variables:
a)ballwise_details_folder
b)info_details_folder
'''

import os
#load pandas
import pandas as pd


# In[142]:
source_folder=input("Enter the Source Folder Details:\n")
info_details_folder=input("Enter the Folder Details Under which Match Information needs to be saved:\n")
ballwise_details_folder=input("Enter the Folder Details Under Which Ball wise Details of each Match needs to be saved:\n")
print("Processing has started...............\n\n\n")
cnt=0
'''listing file names in directory'''
list_of_files =[]
#Change the path as applicable
for path,subdirs, files in os.walk(source_folder):
    for filename in files:
        #Processing csv files alone
        if filename.endswith(".csv"):
            list_of_files.append((filename + os.linesep).strip("\r\n")) 


# In[143]:


for a in range(len(list_of_files)):
    #Counter
    cnt = cnt + 1;
    if cnt == int(len(list_of_files)/4):
        print("25% processing completed")
    elif cnt == 2*int(len(list_of_files)/4):
        print("50% processing completed")
    elif cnt == 3*int(len(list_of_files)/4):
        print("75% processing completed")
    #Change the path as applicable
    #folder_ballwise='C:/Users/vdevarasetty/Desktop/Learnings/Java/Hackathon/CSV_Data/subset/ballbyball/'
    data = pd.read_csv(source_folder+list_of_files[a],encoding='cp1252',names=list('abcdefghijk'),skiprows=1,header=None)
    is_info=(data["a"]=='info')
    non_info=(data["a"]!='info')
    # Splitting the input data to separate excels which have info and ball by ball details 
    data_info=data[is_info]
    data_non_info=data[non_info]
    # Extracting date_played 
    date_info= pd.DataFrame(data_info.iloc[[4]])
    date_played=date_info.iloc[0,2]
    # converting date to integer
    date_played_int=int(date_played[0:4]+date_played[5:7]+date_played[8:10])
    # Extracting teams played information 
    team_info=data_info.loc[0:1]
    text = ''
    for value in team_info["c"]:
        if text=='':
            text=text+value
    else:
        text=text+'_'+value	
    # Processing Data corresponding to Matches played after 2009 alone
    if date_played_int > 20081231 and (text =='Australia_India' or text == 'India_Australia'):
        # add teams played and date played
        data_info['teams_playing']=text
        data_non_info['teams_playing']=text
        data_info['date_played']=date_played
        data_non_info['date_played']=date_played
        data_non_info.to_csv(ballwise_details_folder+list_of_files[a])
        data_info.to_csv(info_details_folder+"info_"+list_of_files[a])

print("\n\nProcessing is completed.\nProcessed Files are available in the below folders:\n"+ "\n1.Information corresponding to ball wise details can be found inside the folder:"+ballwise_details_folder+"\n2.Information corresponding to each Match like Venue,Winner,Ground,Date Played etc., can be found inside the folder:"+info_details_folder)
