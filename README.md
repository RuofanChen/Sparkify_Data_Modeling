# Introduction
This Postgres database is designed for a startup company Sparkify to analyze what songs users are listening to based on data collected on songs and user activity on their new music streaming app. 

A star schema including a fact table (songplays) and 4 dimension tables (users, songs, artists, time) was created for optimizing queries on song play analysis. The original logs of user activity and metadata on the songs in their app, which are in JSON format, were broken into useful forms to store in the multiple tables.  

# Run Python Scripts
In the terminal, follow the sequence to run:  

python create_table.py  

python etl.py

# Explanation of files
1.test.ipynb  

displays the first few rows of each table to let you check database.  

2.create_tables.py  

drops and creates tables. Run this file to reset tables before each time run ETL scripts.  

3.etl.ipynb  

reads and processes a single file from song_data and log_data and loads the data into tables. This notebook contains detailed instructions on the ETL process for each of the tables.  

4.etl.py  

reads and processes files from song_data and log_data and loads them into tables.   

5.sql_queries.py  

contains all sql queries, and is imported into the last three files above.

# Tables 
Fact Table:  

1.songplays - records in log data associated with song plays i.e. records with page NextSong  
              columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id,  
              location, user_agent
Dimension Tables:  

1.users - users in the app  
          columns: user_id, first_name, last_name, gender, level  
          
2.songs - songs in music database  
          columns: song_id, title, artist_id, year, duration  

3.artists - artists in music database  
          columns: artist_id, name, location, latitude, longitude  

4.time - timestamps of records in songplays broken down into specific units  
          columns: start_time, hour, day, week, month, year, weekday

# ETL Process  

Process song files, extract related columns from song file, insert into artists table and songs table.  

Process log files, extract related columns from log file, insert into time table, users table and songplays table.  

Get all files in a list and iterate over to execute the above process (functions).