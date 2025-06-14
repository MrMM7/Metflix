import json
import os

movies_folder = 'static/movies'
thumbnail_folder = 'static/thumbnail'
default_thumbnail = 'image-not-found.png'

all_movies = os.listdir(movies_folder)
all_thumbnails = os.listdir(thumbnail_folder)

json_path = 'db.json'
json_file_data = []

if os.path.getsize(json_path) > 0:
    with open(json_path, 'r') as f:
        json_file_data = list(json.load(f))
        

# adds a new object to the db.json file
def add_object(movie: str, thumbnail: str):
    # the object placed inside the JSON file will look like this
    # also you cannot change the formatting here its forced unfortunately
    dict_like = f" \"{len(json_file_data)}\": {{\"id\": {len(json_file_data)}, \"m\": \"{movie.split('.')[0]}\", \"ms\": \"{movie}\", \"mc\": \"{thumbnail}\", \"d\": \"awesome parser did this!\"}}" 
    json_file_data.append(dict_like)

def find_thumbnail (movie_name: str):
    clean_name = movie_name.split('.')[0]

    # the reason for .split('.')[0] is to remove .mp4, .jpg, .jpeg, ... etc
    for i in range(len(all_thumbnails)):
        if clean_name == all_thumbnails[i].split('.')[0]:
            return all_thumbnails[i] # the thumbnail that matches the movie name
        
    return default_thumbnail

# returns a boolean value if a selected thumbnail exists
def thumbnail_exists (thumbnail:str):
    for i in range(len(all_thumbnails)):
        if all_thumbnails[i].split('.')[0] == thumbnail: # if the selected thumbnail matches the one requested
            return True
    return False

# inserts every object found inside json_file_data into db.json
def insert_into_json():
    with open(json_path, 'w') as f:
        f.write("{\n")
        for line in range(len(json_file_data)):
            if line < len(json_file_data) - 1: f.write(json_file_data[line] + ',\n')
            else: f.write(json_file_data[line] + '\n}')
            
# adds all of the thumbnails/movies found inside their directorys into json_file_data
for i in range(len(all_movies) - 1):
    thumbnail = find_thumbnail(all_movies[i])
    add_object(all_movies[i], thumbnail)
    
        
insert_into_json() # inserts every object found inside 'json_file_data' into the db.json file