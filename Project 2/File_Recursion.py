import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    def suffix_file_helper(item, suffix, path):
        location = os.path.join(path, item)
        #if item.endswith(suffix):
        if os.path.isfile(location):
            return item
        if os.path.isdir(location):
            new_path = os.chdir(location)
            suffix_file_helper(item, suffix, new_path)
    
    
    files = os.listdir(path)
    suffix_file_list = []
    
    for file in files:
        #suffix_file_list.append(suffix_file_helper(file, suffix, path))
        print(file)
        x = os.path.join(path, file)
        print('is file?:', os.path.isfile(x))
        print('is dir?', os.path.isdir(x))
    
    #print(suffix_file_list)
    
    
    
def tests():
    path = r'C:\Users\Andrew\Downloads\testdir\testdir'
    suf = '.c'
    
    find_files(suf, path)
    
tests()