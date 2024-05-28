import fitz
import os
import re
import shutil

path = os.getcwd()
input = os.path.join(path, 'Arquivo')
output = os.path.join(path, 'Resultado')
doc_aux = os.listdir(input)
for i, file in enumerate(doc_aux):
    doc = fitz.open(input + ('/%s'% file))
    for page in doc:
        file_name = re.split("\.", file)
        pix = page.get_pixmap()
        image_name = ('%s_page-%i.png'%(file_name[0], page.number))
        pix.save(image_name)
        path_aux = os.path.join(path, image_name)
        output_aux = os.path.join(output, image_name)
        shutil.move(path_aux, output_aux)
print('Arquivo Separado!')