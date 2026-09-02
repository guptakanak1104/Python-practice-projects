import os
import shutil

#Folder path you want to organize
FOLDER_PATH = os.getcwd() # current working directory

#File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".md"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".js", ".html", ".css", ".php"],
}

#create folders if they don't exist
for folder in FILE_TYPES.keys(): # Creates folders for each file type 
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file in os.listdir(FOLDER_PATH): # Loops through all files in the folder
    file_path = os.path.join(FOLDER_PATH, file)

    #skip directories/folders
    if os.path.isdir(file_path):
        continue

    #get file extension
    #print(os.path.splitext(file_path))
    file_ext = os.path.splitext(file_path)[1].lower() # Get the file extension and convert it to lowercase

    for folder, extensions in FILE_TYPES.items(): # Loops through the file types and their extensions
        if file_ext in extensions: # If the file extension matches one of the extensions in the list
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file)) # Move the old file path to this new folder
            break

print("Files organized successfully!") 