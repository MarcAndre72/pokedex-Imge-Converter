import sys
import os
from PIL import Image, ImageFilter # Added ImageFilter

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)
    
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  
  # Add blur effect for Charmander
  if clean_name.lower() == 'charmander':
      img = img.filter(ImageFilter.BLUR)
      print('Charmander image has been blurred!')
  img.save(f'{directory}/{clean_name}.png', 'png')
print('All images have been converted successfully!')
