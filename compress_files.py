import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    # Get the folder name
    folder_name = os.path.basename(folder_path)
    
    # Get the current date
    current_date = datetime.now().strftime("%Y_%m_%d")
    
    # Define the compressed file name
    compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"
    
    try:
        # Create a compressed file based on the chosen compression type
        if compress_type == "zip":
            with zipfile.ZipFile(compressed_file_name, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file))
        
        elif compress_type == "tar":
            with tarfile.open(compressed_file_name, 'w') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
        
        elif compress_type == "tgz":
            with tarfile.open(compressed_file_name, 'w:gz') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
        
        else:
            print("Unsupported compression type.")
            return
        
        print(f"Compression successful. Compressed file saved as '{compressed_file_name}'")
        
    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    compress_type = input("Enter the compression type (zip, tar, tgz): ").lower()
    
    compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()
