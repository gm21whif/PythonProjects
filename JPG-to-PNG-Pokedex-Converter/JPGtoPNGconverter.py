import sys  #command line arguments
import os  #file path
from PIL import Image #image manipulation

#Done -grab first and second argument
#Done -check if new/ exists
#Done -if not create
#-for loop through Pokedex (the starting directory)
#-convert images to png (uses image library)
#-save to new folder (write file)

#sys to grab 1st and 2nd argument
#OS grab path write it to new file
#pil model to convert to png

#grab first and second argument
#Pokedex/
starting_directory = sys.argv[1]
#starting_directory = "Pokedex/"
#New/
destination_directory = sys.argv[2]
#destination_directory = "New/"

#check is new/ exists, if not create
if os.path.exists(destination_directory) is False:
  os.mkdir(destination_directory)

#-for loop through Pokedex (the starting directory)
for file_name in os.listdir(starting_directory):
  print(os.path.splitext(file_name))
  file_name_no_ext, extension = os.path.splitext(file_name)
  new_file_name = file_name_no_ext + ".png"
  if file_name != new_file_name:
    try:
      with Image.open(starting_directory + file_name) as from_jpg_to_png_image:
        from_jpg_to_png_image.save(destination_directory + new_file_name,
                                   "png")
    except OSError:
      print("cannot convert ", file_name)

  #-convert images to png (uses image library)
  #-save to new folder (write file)

#OS grab path write it to new file

#(function) def listdir(path: StrPath | None = None) -> list[str]

#pip3 install Pillow
#python3 JPGtoPNGconverter.py Pokedex/ New/
