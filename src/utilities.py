import os
IMAGE_DIRECTORY = "img"
def get_path_img():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), IMAGE_DIRECTORY)

def add_path_file(path,file):
    return os.path.join(path,file)