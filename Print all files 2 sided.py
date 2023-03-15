import glob
# import win32print 
# from win32printing import Printer
import os

os.chdir('E:\OneDrive - Greenfield Analytics\Development\PythonAnalytics\ChatGPT\County Resources')

# Path to the directory containing text files
text_files_dir = 'E:\OneDrive - Greenfield Analytics\Development\PythonAnalytics\ChatGPT\County Resources'

# Find all text files in the directory using glob
text_files = glob.glob(text_files_dir + '/*.txt')

# Print each text file double-sided on the default printer
for text_file in text_files:
    # Open the text file and read its contents
    with open(text_file, 'r') as f:
        #file_contents = f.read()
        os.startfile(text_file, "print")
 
