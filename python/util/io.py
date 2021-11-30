
import pickle
from urllib.request import urlopen
# import dill as pickle  # use dill to help io model instance


def write_file(file, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(file, f)


def read_file(file_path):
    if file_path.startswith('http'):
        with urlopen(file_path,) as f:
            file = pickle.load(f)
    else:
        with open(file_path, 'rb') as f:
            file = pickle.load(f)
    return file
