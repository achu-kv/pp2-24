import os

# task 1
def list_dirs(path):
    elems = os.listdir(path)
    for i in elems:        
        if os.path.isdir(os.path.join(path, i)):
            print(i)
    
def list_files(path):
    elems = os.listdir(path)
    for i in elems:
        if os.path.isfile(os.path.join(path, i)):
            print(i)

def list_everything(path):
    for i in os.listdir(path):
        print(i)

# task 2
def test_path(path):
    if not os.path.exists(path):
        print(f'Path {path} does not exist')
        return
    print(f'Path {path} exists!')
    rdbl = "yes" if os.access(path, os.R_OK) else "no"
    print(f'Readable: {rdbl}')

    wbtl = "yes" if os.access(path, os.W_OK) else "no"
    print(f'Writable: {wbtl}')

    exc = "yes" if os.access(path, os.EX_OK) else "no"
    print(f'Executable: {exc}')

# task 3
def exists(path):
    if not os.path.exists(path):
        print(f'Path {path} does not exist')
        return
    print(f'Path {path} exists')
    elems = os.path.split(path)
    print(f'Dirs: {elems[0]}, file: {elems[-1]}')

# task 4
def num_lines(path):
    if not os.path.isfile(path):
        print(f'Path {path} is not a file, aborting')
        return
    with open(path, 'r') as f:
        lines = f.readlines()
        print(f'File {path} has {len(lines)} lines')

# task 5
def write_list(lst, path):
    with open(path, 'w') as f:
        print(*lst, file=f)

# task 6
def a_z_files():
    for i in range(65, 91):
        open(f'{chr(i)}.txt', 'w')

# task 7
def copy_data(src, dest):
    with open(src, 'r') as f:
        data = f.readlines()
    with open(dest, 'w') as f:
        print("".join(data), file=f)

# task 8
def del_file(path):
    if not os.path.exists(path):
        print(f'Path does not exist, aborting')
        return
    try:
        os.remove(path)
    except BaseException:
        print(f'Unable to delete file {path}')
