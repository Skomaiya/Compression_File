# File Compression Python Program

## Introduction
This Python program allows users to compress files and folders to various compressed file types, such as .zip, .tar, and .tgz. The program prompts the user to select a folder to compress and then displays a list of available compression types. Once the user selects a compression type, the program compresses the folder using the chosen type.

## How to Run the Program
1. Ensure you have Python installed on your system.
2. Download the `compress_files.py` file from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the `compress_files.py` file.
5. Run the following command to execute the program:
6. Follow the prompts to select the folder to compress and choose the compression type.

## Group Members
- Komaiya Samuel

## Explanation of the Code
1. The program prompts the user to enter the path of the folder to compress.
2. It then displays a list of available compression types (zip, tar, tgz).
3. The user selects a compression type from the list.
4. The program compresses the folder using the selected compression type and saves the compressed file with a name based on the folder name and the current date.
5. It provides feedback to the user indicating whether the compression was successful or if there was an error.
6. The program handles various compression types using the `zipfile` and `tarfile` libraries in Python.
