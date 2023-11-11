import os
import shutil

def copy_folders(source_folder, target_folder, folder_name):
    count = 0
    for root, dirs, _ in os.walk(source_folder):
        if folder_name in dirs:
            source_path = os.path.join(root, folder_name)
            target_path = os.path.join(target_folder, f"{folder_name}_{count}")
            if os.path.exists(target_path):
                shutil.rmtree(target_path)
            shutil.copytree(source_path, target_path)
    print(f'{count+1} Folders copied')

# Replace 'source_path' with the folder to searched
# Replace 'target_path' with the folder to be copied into
# Replace 'folder_name' with the name of the folders needing to be copied
copy_folders('source_path', 'target_path', 'folder_name',)