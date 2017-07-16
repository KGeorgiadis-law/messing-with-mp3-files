
# coding: utf-8

# In[1]:

#!pip install mutagen


# In[2]:

# dependencies
import os


# In[3]:

# for help on mutagen, see https://mutagen.readthedocs.io/en/latest/user/id3.html
from mutagen.easyid3 import EasyID3
print(EasyID3.valid_keys.keys())


# In[ ]:

folder_to_use = input("please select folder:")


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


# In[ ]:

# list to save all mp3 files in folder
tracks = list()

# get all mp3 tracks in file and add them to the 'tracks' list
for file in os.listdir():
    if file.endswith(".mp3"):
        tracks.append(file)

#print(tracks)


# In[ ]:

# change the album to the folder name
for track in tracks:
    current_track = EasyID3(track)
    current_track["album"] = album_name
    print("changing album for ", track)
    current_track.save()

print("Finished!")


# In[ ]:



