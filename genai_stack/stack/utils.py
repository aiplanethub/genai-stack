import os


def is_dir_exists(path:str) -> bool:
    if os.path.isdir(path):
        return True
    else:
        return False
    
def create_dir(path:str) -> str:
    return os.mkdir(path)