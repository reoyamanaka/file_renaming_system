import os

dir_path = os.path.dirname(os.path.realpath(__file__))
imagesFolder = f'{dir_path}/images'
included_extensions = ['JPG']

file_names = [fn for fn in os.listdir(imagesFolder)
              if any(fn.endswith(ext) for ext in included_extensions)]

for file in file_names:
    file_number = int(''.join(i for i in file if i.isdigit())) - 1
    new_image_name = str(file_number) + ".JPG"
    os.rename("images/"+file, "images/"+new_image_name)





    


