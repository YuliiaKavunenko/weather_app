import os

def search_path(file_name):
    path = __file__.split("/")
    del path[-1]
    path = "/".join(path)
    path = os.path.join(path, file_name)
    return path