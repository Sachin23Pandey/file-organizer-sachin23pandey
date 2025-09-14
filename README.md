
# file-organizer-sachin23pandey
##### This is a file organizer designed to assist users in managing their directories more visually and intuitively

## Overview
`file-organizer-sachin23pandey` package is a simple and lightweight Python package to organize files by extension and perform basic file and folder management operations (create, delete, rename).

Currently, it includes functions to organize files by extension, create files/folders, delete files/folders, and rename them.

Developed by `Sachin Pandey` (c) 2025

## Installation
You can install it from TestPyPI (for now):
```python
pip install file-organizer-sachin23pandey
```
## Usage 

### 1. Importing
```python
from file_organizer_sachin23pandey import file_organizer 
```

### 2. Organize Files by Extension
Organize all files in a folder into subfolders based on their file extensions.
```python 
from file_organizer_sachin23pandey import file_organizer

file_organizer.organize_file("C:\\Users\\Radha\\Downloads")
```
### 📂 Example:
If your folder has image.jpg, document.pdf, and notes.txt,
it will create folders jpg, pdf, txt and move files into them.

### 3. Create Files and Folders
```python 
from file_organizer_sachin23pandey import file_organizer

file_organizer.create_file("C:\\NewT", "example.txt")     # Creates an empty file
file_organizer.create_folder("C:\\NewT", "MyFolder")     # Creates a folder

```
### 4. Delete Files and Folders
```python 
from file_organizer_sachin23pandey import file_organizer

file_organizer.delete_file("C:\\NewT", "example.txt")
file_organizer.delete_folder("C:\\NewT", "MyFolder")

```
### 5. Rename Files and Folders
``` python 
from file_organizer_sachin23pandey import file_organizer

file_organizer.rename_file("C:\\NewT", "old.txt", "new.txt")
file_organizer.rename_folder("C:\\NewT", "OldFolder", "NewFolder")

```
### 6. Description about functions

| Function                                  | Description                                       |
| ----------------------------------------- | ------------------------------------------------- |
| `file_organizer(path)`                    | Organizes files in the given folder by extension. |
| `create_file(path, filename)`             | Creates an empty file if it does not exist.       |
| `create_folder(path, foldername)`         | Creates a folder if it does not exist.            |
| `delete_file(path, filename)`             | Deletes a file if it exists.                      |
| `delete_folder(path, foldername)`         | Deletes a folder (and its contents) if it exists. |
| `rename_file(path, old_name, new_name)`   | Renames an existing file.                         |
| `rename_folder(path, old_name, new_name)` | Renames an existing folder.                       |


## Project Url 
