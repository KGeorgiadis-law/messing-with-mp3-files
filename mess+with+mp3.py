
# coding: utf-8

#!pip install mutagen


# dependencies
import os

# with thanks to ThemisB https://github.com/ThemisB/grecka
from grecka import *




# for help on mutagen, see https://mutagen.readthedocs.io/en/latest/user/id3.html
from mutagen.easyid3 import EasyID3
valid_keys = list(EasyID3.valid_keys.keys())
valid_keys.sort()
valid_keys_str = ", ".join(valid_keys)
print(valid_keys_str)

# functions to use
def change_mp3_file(mp3_file_folder, mp3_file_name, key_to_change, new_value):
    # join the folder name and the file name to find the absolute path
    mp3_file_path = os.path.join(mp3_file_folder, mp3_file_name)
    # initialise mutagen
    current_track = EasyID3(mp3_file_path)
    if key_to_change in valid_keys:
        current_track[key_to_change] = new_value
        print("changing {} for '{}' to '{}'".format(key_to_change, mp3_file_name, new_value))
        current_track.save()
    else:
        raise NameError("You doofus! '{}' is not one of the available keys! You can see the available keys by using print(available_keys)".format(key_to_change))

def get_mp3_information(mp3_file_folder, mp3_file_name, key_to_take):
    mp3_file_path = os.path.join(mp3_file_folder, mp3_file_name)
    current_track = EasyID3(mp3_file_path)
    return current_track[key_to_take]

def mass_renamer(root, original_file, new_name):
    original_file_path = os.path.join(root, original_file)
    new_file_path = os.path.join(root, new_name)
    print("Renaming '{}' to '{}'...".format(original_file, new_name))
    os.rename(original_file_path, new_file_path)
    print("finished!")


folder_to_use = input("please select root folder: ")

# test for mass_renamer

# for file in os.listdir(folder_to_use):
#     if file.endswith(".mp3"):
#         new_name = file[27:]
#         print("renaming {} to {}...".format(file, new_name))
#         mass_renamer(folder_to_use, file, new_name)
        
        
# original_file = "amazon.txt"
# new_name = "amazon_ip_code.txt"
# mass_renamer(root_test, original_file, new_name)




# #get the folder name, which is the same as the album name
# os.chdir(folder_to_use)
# current_working_directory = os.getcwd()
# current_working_directory_list = current_working_directory.split("\\")
# folder_name = current_working_directory_list[-1]
# album_name = folder_name 

# #all of the above as a one-liner:
# album_name2 = str(os.getcwd()).split("\\")[-1]

# print(album_name)
# #print(album_name2)


# get input from external file, here titles and artists from titles.txt, where titles and artists are delimited with ,
# title_file = "titles.txt"

# with open(os.path.join(folder_to_use, title_file), "r") as titles:
#     contents = titles.read()
#     properties_list = contents.split("\n")
#     all_properties = list()
#     track_number = 1
#     for record in properties_list:
#         properties_per_song = record.split(",")
#         all_properties.append(properties_per_song)
#     print(all_properties)
#         #print(i, ": ", titles_list[i])


# main action - changing mp3 files' metadata
mp3_files = list()
for root, subdirs, files in os.walk(folder_to_use):
 print("--\nroot = "+root)
 print(subdirs)
 print(files)
 title_counter = 0
 for file in files:
     if file.endswith(".mp3"):
##         title = all_properties[title_counter][0]
##         artist = all_properties[title_counter][1]
##         change_mp3_file(root, file, "album", "To Paixnidi Paizetai")
         change_mp3_file(root, file, "album", "SFENTONA Live")
     title_counter += 1
print("Finished!")




# get the titles of all mp3 files in folder
# for file in os.listdir(folder_to_use):
#     if file.endswith(".mp3"):
#         title = get_mp3_information(folder_to_use, file, "title")
#         print(title[0])




# renaming files based on the title name

### mp3_files = list()
##counter = 1
##for file in os.listdir(folder_to_use):
##    if file.endswith(".mp3"):
##        title = get_mp3_information(folder_to_use, file, "title")
##        mass_renamer(folder_to_use, file, "%02d - %s.mp3" % (counter, title[0]))
##        counter += 1

# the opposite : setting the titles in accordance with the file name

##for file in os.listdir(folder_to_use):
##    if file.endswith(".mp3"):
##        title = file[3:-4]  
##        print(title)
##        # convert to Greeklish (for encoding issues)
###         title = Grecka.toGreeklish(title)
###         print(title)
##        change_mp3_file(folder_to_use, file, "title", title)
##        change_mp3_file(folder_to_use, file, "artist", ARTIST_NAME)
##        change_mp3_file(folder_to_use, file, "album", ALBUM_NAME)
##print("finished!")

