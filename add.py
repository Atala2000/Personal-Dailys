#!/usr/bin/env python3
import pyperclip, os, json

with open("/home/atala/movies/movie.json", "r") as file_obj:
    movie = json.load(file_obj)

# * Gets the user input
print(f"Available files are: ")
for key in movie.keys():
    print(f"{key}")
genre = input("Where would you like to store the movie: ")

if genre in movie.keys():
    if genre == "best":
        file_path = "/mnt/c/Users/User/Downloads"
    else:
        file_path = "/mnt/c/Users/User/Desktop/Movies"
    file_path = os.path.join(file_path, movie[genre])
    with open(file_path, "a") as file_obj:
        movie_name = pyperclip.paste()
        tmp = movie_name
        print(f"Adding {tmp.rstrip()} to the file {genre}")
        movie_name = movie_name.replace("\n", "")
        file_obj.write(movie_name + "\n")

else:
    prompt = input("File doesn't exist, would you like to create it(type y or n): ")
    if prompt == "y":
        prompt = input("What would you like to name the file: ")
        prompt = prompt.lower()
        movie[prompt] = prompt + ".txt"

with open("/home/atala/movies/movie.json", "w") as file_obj:
    json.dump(movie, file_obj)
