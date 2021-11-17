__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


from pathlib import Path
import zipfile
import os
import fileinput


def clean_cache():
    cache_path = Path("../files/cache")
    if not cache_path.exists():
        cache_path.mkdir(parents=True)
    else:
        for child in cache_path.iterdir():
            if cache_path.is_file:
                child.unlink()
            elif cache_path.is_dir:
                child.unlink()


def cache_zip(z_file_path, dir_path):
    clean_cache()
    z = zipfile.ZipFile(z_file_path)
    z.extractall(dir_path)


def cached_files():
    path_list = []
    cache_path = Path("./cache")
    for child in cache_path.iterdir():
        path_list.append(os.path.abspath(child))
    return path_list


def find_password(file_list):
    for file_name in file_list:
        for line in fileinput.input(file_name):
            if "password" in line:
                return line[line.index(" ") + 1:].strip()
