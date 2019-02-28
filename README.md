# UpGrad Cricket Challenge
## Project Report
#### Submitted By Vinay Devarasetty & Venkatesh Jagannathan



### Data Selection

- Sources: https://cricsheet.org/, http://www.espncricinfo.com/
- Format: CSV
- Match Type: ODI
- Time Period: 2009-2019
- Data: Batting, Bowling, Summary

### Data Cleansing

Filtering Criterion: -

* Players going to be part of Ind Vs Aus ODI 2019
* All ODI Innings between India & Australia
* Required Aggregates
  * Batting - Runs, 4s, 6s, etc.
  * Bowling - Dismissal, Runs Conceded etc.

### Data Processing

1. Prefiltering data using python script to have suitable structure for consumption
  1. Ball By Ball
  1. Match & Innings Info
1. Aggregated 2009 to 2017 from cricsheet using Hive
1. Merged aggregate result with available 2018-2019 data from espncricinfo


### Data Visualization

1. Loaded final data results into google sheets
1. Generate Data Charts for on the fly flexible analysis using *Google Data Analytics*

### Prediction Results

#### Winner of the Series
India

#### Series Outcome
Match | Date | Location | Winner
ODI 1 | 02 Mar | Hyderabad | India
ODI 2 | 05 Mar | Nagpur |  India
ODI 3 | 08 Mar | Ranchi |  Aus
ODI 4 | 10 Mar | Mohali |  Aus
ODI 5 | 13 Mar | Delhi |  India

*correlation between win loss ratio on each ground and overall team players experience*

##### Highest Run Scorer

1. Virat Kohli
1. Aaron Finch
1. MS Dhoni

#### Highest Wicket Takers
1. Bhuvaneswar Kumar
1. Nathan Coulter-Nile
1. Mohammed Shami

#### Maximum Sixes By
1. Virat Kohli
1. Aaron Finch
1. MS Dhoni

#### Maximum Fours By
1. Virat Kohli
1. Aaron Finch
1. MS Dhoni


### Technology Stack
1. Python - Cleansing
1. Hive - Data Aggregation
1. Google Data Studio - Visualization

Notes: 
1. Data insufficient for some new players who have performed very well recently 
1. Prediction can be improved if other formats can be included and weighted
1. Reliable Historical Weather Data of matches could not be found to include in prediction analysis




