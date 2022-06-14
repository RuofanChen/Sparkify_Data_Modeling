# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

user_table_create = ("""
create table if not exists users
(user_id int,
 first_name varchar(255),
 last_name varchar(255), 
 gender char(1),
 level char(4),
 primary key (user_id));
""")


artist_table_create = ("""
create table if not exists artists
 (artist_id varchar(255),
  name varchar(255) NOT NULL,
  location varchar(255),
  latitude double precision,
  longitude double precision,
  primary key (artist_id));
""")


song_table_create = ("""
create table if not exists songs
(song_id varchar(255),
title varchar(255) NOT NULL,
artist_id varchar(255),
year int,
duration numeric NOT NULL,
primary key (song_id),
constraint song_ar foreign key (artist_id) references artists(artist_id) on delete cascade);
""")


time_table_create = ("""
create table if not exists time
(start_time timestamp,
 hour int,
 day int,
 week int,
 month int,
 year int,
 weekday varchar(10),
 primary key (start_time));
""")


songplay_table_create = ("""
create table if not exists songplays 
(songplay_id serial, 
 start_time timestamp NOT NULL, 
 user_id int NOT NULL, 
 level char(4) NOT NULL, 
 song_id varchar(255), 
 artist_id varchar(255),
 session_id int,
 location varchar(255),
 user_agent varchar(255),
 primary key (songplay_id),
 constraint sp_time foreign key (start_time) references time (start_time) on delete cascade,
 constraint sp_user foreign key (user_id) references users (user_id) on delete cascade,
 constraint sp_song foreign key (song_id) references songs (song_id) on delete cascade,
 constraint sp_artist foreign key (artist_id) references artists (artist_id) on delete cascade
 );
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (start_time,user_id, level, song_id, artist_id, session_id, location,user_agent) values (%s,%s,%s,%s,%s,%s,%s,%s) on conflict do nothing;
""")

user_table_insert = ("""insert into users values (%s,%s,%s,%s,%s) on conflict (user_id) do update set level = excluded.level;
""")

song_table_insert = ("""insert into songs values (%s,%s,%s,%s,%s) on conflict do nothing;
""")

artist_table_insert = ("""insert into artists values (%s,%s,%s,%s,%s) on conflict (artist_id) do update
set location = excluded.location,latitude = excluded.latitude,longitude = excluded.longitude;
""")


time_table_insert = ("""insert into time values (%s,%s,%s,%s,%s,%s,%s) on conflict do nothing;
""")

# FIND SONGS
# find the song ID and artist ID based on the title, artist name, and duration of a song.
song_select = (""" select songs.song_id, songs.artist_id from
songs join artists on songs.artist_id = artists.artist_id
where title = %s and
name = %s and 
duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]