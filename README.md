# ZipSlip Exploit Helper

This Python script creates a malicious ZIP file designed to exploit a Zip Slip vulnerability in CTF challenges. The script allows you to craft ZIP files containing files with paths like `../../../file.jsp`, which may allow directory traversal attacks during extraction.

## Features
- Create a ZIP file with a specified name.
- Include a file in the ZIP with a crafted directory traversal path.
- Simple and flexible command-line arguments.

---

## Requirements
- Python 3.x
- Ensure Python is properly installed and added to your system's PATH.

---

## Installation
1. Clone this repository or copy the script:

```
   git clone https://github.com/MuzamilSheikh09/Zip-Slip.git
   cd Zip-Slip
   
```



## Usage

Run the script using the following syntax:

```
python3 Zip-slip.py -n <zip_name> -p <file_path> -z <crafted_path>

python3 Zip-slip.py -n poc.zip -p ./file.jsp -z '../'

```
## Arguments

```
    -n: Name of the ZIP file to create (e.g., poc.zip).
    -p: Path to the file you want to include in the ZIP (e.g., ./file.jsp).
    -z: Directory traversal path for the file (e.g., ../../../../).

```


## Explanation

This script takes advantage of the Zip Slip vulnerability, which occurs when file extraction processes fail to sanitize file paths within ZIP archives. By crafting a malicious path, you can potentially overwrite critical system files if the target system is vulnerable.
Notes


**Educational Use Only:** This script is intended for ethical hacking and CTF challenges. Do not use it for illegal activities.
    Ensure you have permission before testing on any system.
