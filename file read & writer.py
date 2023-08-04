#!/usr/bin/env python3

import os , pyperclip

dictionary_path = input('Enter the full path of the dictionary:\n')
file_name = input('Enter the file name you want to create:\n')
def answer_files(path):
    files =[]
    for file in sorted(os.listdir(path)):
        if file.endswith('.py'):
            files.append(file)
    return files

files = answer_files(dictionary_path)

def answer_writer(path,files):
    for file in files:
        with open(os.path.join(path,file),'r') as answer:
            answer = answer.read()
            pyperclip.copy(answer)
        with open(os.path.join(path,file_name),'a') as solution:
            solution.write(f'\t\t{file}' + '\n' + pyperclip.paste() + '\n\n')


if os.path.exists(dictionary_path):
    answer_writer(dictionary_path,files)
    print(f'{file_name} file created successfully ' )
else:
    print('Please enter a valid dictionary path')
