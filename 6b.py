from zipfile import ZipFile
import os

with ZipFile('G:\\cse_file.zip','w') as zip_object:
    zip_object.write('G:\\cse_file.zip\\file1.txt')
    zip_object.write('G:\\cse_file.zip\\file2.txt')
if os.path.exists('G:\\cse_file.zip'):
    print("zip file created")
else:
    print("zip file is not created")