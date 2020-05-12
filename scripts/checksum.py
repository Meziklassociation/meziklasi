import hashlib
import os
import json

SAVE_FILE_PATH = "checksum_save.json"

def generate_checksum(file_name):
    hash_sha256 = hashlib.sha256()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def get_list_of_files():
    os.chdir(os.path.join("..", "_site"))
    return [
        os.path.join(root, name)[2:].replace("\\", "/")
        for root, dirs, files in os.walk(".")
        for name in files
    ]

def global_checksum():
    return {f: generate_checksum(f) for f in get_list_of_files()}

def save(data):
    json.dump(data, open(SAVE_FILE_PATH, 'w'))

def load():
    return json.load(open(SAVE_FILE_PATH))

def download_old_save():
    pass # some ftp magic

old_checksum = download_old_save()
new_checksum = global_checksum()

def should_be_uploaded(file_path):
    if file_path in old_checksum.keys():
        return old_checksum[file_path] == new_checksum[file_path]
    else:
        return True
