# import os
# import shutil

# def rename_m3u_files(root_folder):
#     for foldername, subfolders, filenames in os.walk(root_folder):
#         for filename in filenames:
#             if filename == "BeIn.m3u8":
#                 file_path = os.path.join(foldername, filename)
#                 new_filename = "BeIn.m3u"
#                 new_file_path = os.path.join(foldername, new_filename)
#                 shutil.move(file_path, new_file_path)
#                 print(f'Renamed: {file_path} -> {new_file_path}')

# def main():
#     # Replace 'your_root_folder' with the path to your root folder
#     root_folder = './'
#     rename_m3u_files(root_folder)

# if __name__ == "__main__":
#     main()

import os

def delete_make_file(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename == "make _file.py":
                file_path = os.path.join(foldername, filename)
                os.remove(file_path)
                print(f'Deleted: {file_path}')

def main():
    # Replace 'your_root_folder' with the path to your root folder
    root_folder = './'
    delete_make_file(root_folder)

if __name__ == "__main__":
    main()
