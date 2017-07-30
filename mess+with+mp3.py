
# coding: utf-8

# In[1]:

#!pip install mutagen


# In[3]:

# dependencies
import os


# In[27]:

# for help on mutagen, see https://mutagen.readthedocs.io/en/latest/user/id3.html
from mutagen.easyid3 import EasyID3
valid_keys = EasyID3.valid_keys.keys()
print(valid_keys)   


# In[36]:

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


# In[34]:

folder_to_use = input("please select root folder: ")


# In[ ]:

#get the folder name, which is the same as the album name
os.chdir(folder_to_use)
current_working_directory = os.getcwd()
current_working_directory_list = current_working_directory.split("\\")
folder_name = current_working_directory_list[-1]
album_name = folder_name 

#all of the above as a one-liner:
album_name2 = str(os.getcwd()).split("\\")[-1]

print(album_name)
#print(album_name2)


# In[40]:

mp3_files = list()
for root, subdirs, files in os.walk(folder_to_use):
    print("--\nroot = "+root)
    print(subdirs)
    print(files)
    for file in files:
        if file.endswith(".mp3"):
            try:
                change_mp3_file(root, file, "kjasdlkalfd", "")
            except NameError:
                print("*** Invalid value to change, script will now exit ***")
                break
print("Finished!")

