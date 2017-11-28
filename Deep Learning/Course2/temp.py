import shutil
import os

cwd = os.getcwd()

zip_name = 'test' # Name of .zip
directory_name = cwd # Current working dir where .zip downloads to

# Create 'path\to\test.zip'
shutil.make_archive(zip_name, 'zip', directory_name)c