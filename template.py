import os
from pathlib import Path
import logging

#basic logging config log level is information
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:') #asctime is current timestamp,log message will be displayed


list_of_files = [
  "src/__init.py", 
  "src/helper.py", #all functionalities
  "src/prompt.py", #all prompts are written here
  "setup.py", #to install as local package
  "app.py",
  "research/trails.ipynb"
]


for filepath in list_of_files:
  filepath = Path(filepath)
  filedir , filename = os.path.split(filepath) #split as src and __init__


  #Folder exits
  if filedir != "":
    os.makedirs(filedir,exist_ok=True)
    logging.info(f"Creating directory; {filedir} for the file: {filename}")

  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath,"w") as f:
        pass
        logging.info(f"Creating empty file: {filepath}")

  else:
      logging.info(f"{filename} already exists")


    

