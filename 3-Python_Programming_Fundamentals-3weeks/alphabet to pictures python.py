
# This script takes in user input and converts it into pictures in the folder "userinput"
# upper and lowercase letters give the same images, spaces and dots are supported.
# if you type any other character that character won't be converted

import shutil
import string
import os
import requests
import zipfile
import io

owner = 'mouda4d'
repo = 'Alphabets'
branch = 'main'
folder = 'MESSAGE'
# get my github repo that contains the alphabets images
git_url = f'https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip'
response = requests.get(git_url)

dict = {}
i = 1

# Check if the request was successful
if response.status_code == 200:
    # extract and save the files into memory instead of disk for efficiency
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip:
        zip.extractall()
    print("images retrieved successfully")
else:
    print("request failed")

#loop over lower and uppercase methods and map them to numbers
for char in string.ascii_lowercase + string.ascii_uppercase:
    if char == 'A':
        i -= 26
    dict[char] = i
    i += 1

#adding space and dot
dict['.'] = i
dict[' '] = i+1

#getting user input
text = input("Please enter the text you would like to convert to images: ")
try:
    shutil.rmtree(folder)
except:
    print(f"Creating folder: {folder}")
os.makedirs(folder, exist_ok=True)

unmatched = []
i = 1
# loop over each character in userinput, convert to an image, rename it then copy it to the folder
for char in text:
    try:
        source = os.path.join(os.getcwd(), f'{repo}-{branch}/{dict[char]}.jpg')
        renamed = os.path.join(os.getcwd(), f'{folder}/{i}.jpg')
        shutil.copy(source, renamed)
        i+=1
    # this message will be displayed whenever a character isnt matched
    except:
        # only display this message once per unmatched character
        if char not in unmatched:
            print(f"{char} does not have a matching image, and was skipped.")
        unmatched.append(char)
