from pathlib import Path
import shutil
import os 

#This puts us into the Downloads folder 
downloads = Path.home() / "Downloads"

#Creating the table of file extentsions for Sorting 
extension_dict = {
    ".png" :"C:\\Users\\Darwi.THEBOX\\OneDrive\\Pictures\\",
    ".jpg" :"C:\\Users\\Darwi.THEBOX\\OneDrive\\Pictures\\",
    ".docx":"C:\\Users\\Darwi.THEBOX\\OneDrive\\Documents\\",
    ".pdf" :"C:\\Users\\Darwi.THEBOX\\OneDrive\\Documents\\", 
}

# This list contains extensions that should be deleted
# Make sure to add or remove extenstions based on your preferences
# Make sure that this list is 100% good before running program   
deleting_list = [".exe" , ".zip" , ".jar", ".msi", ".iso"]


for file in downloads.iterdir():
    if file.suffix in extension_dict:
        newDestination = extension_dict[file.suffix]
        shutil.move(str(file), (newDestination + file.name))
    if file.suffix in deleting_list:
        os.remove(file)

