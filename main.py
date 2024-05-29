from pdf2image import convert_from_path
import os
import re

path = os.getcwd()
input = os.path.join(path, 'Files')
if not os.path.exists(input):
    os.mkdir(input)
output = os.path.join(path, 'Result')
if not os.path.exists(output):
    os.mkdir(output)
doc_aux = os.listdir(input)
for i, file in enumerate(doc_aux):
    doc = convert_from_path(os.path.join(input, file))
    for i, page in enumerate(doc):
        file_name = re.split("\.", file)
        image_name = f"{file_name[0]}_page{i+1}.jpg"
        output_folder = os.path.join(output, file_name[0])
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        output_path = os.path.join(output_folder, image_name)
        page.save(output_path, 'JPEG')
    os.remove(os.path.join(input, file))
        
print('Arquivos Separados!')