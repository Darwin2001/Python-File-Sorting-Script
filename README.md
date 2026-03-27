# Python File Sorting Script 
This is a short Python script I made in order to help me declutter the dreaded downloads folder on my PC! This script targets common file extension types and sorts them into Microsoft's predetermined directories, mainly pictures and documents. This script runs on absolute paths as that was the easiest and most efficient implementation, meaning if you wish to use this script for yourself just make sure to use your absolute path to each of the folders mentioned in the dictionary. 

# Technology Used 
For this script I used Python and its built-in libraries. For pathing I used pathlib, file movement I used shutil, and finally for file deletion I used the OS library.

# Lessons Learned
This taught the basics about Python automation and the foresight required when planning these automated flows. I learned  about the built-in libraries with Python and the types of functions they can cover on a computer, and got to tussle with some dictionaries and lists as a nice refresher. 

# Optimizations
Currently this program runs in O(n) which is fine for the small scale I am using it for. I plan to add more support for Windows other predetermined files like libraries and a function to delete empty directories and look through them for those same type of files as well. 
