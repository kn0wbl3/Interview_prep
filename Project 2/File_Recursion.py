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
    
    def suffix_file_helper(item, suffix, location):   
        if os.path.isfile(location):
            if item.endswith(suffix):
                suffix_file_list.append(item)
        if os.path.isdir(location):
            new_path = os.listdir(location)
            for new_file in new_path:
                new_location = os.path.join(location, new_file)
                suffix_file_helper(new_file, suffix, new_location)
    
    files = os.listdir(path)
    suffix_file_list = []
    
    for file in files:
        location = os.path.join(path, file)
        suffix_file_helper(file, suffix, location)
    
    print(suffix_file_list)
    
    
    
def tests():
    path = r'C:\Users\amanuele2\AppData\Local\Temp\Bloomberg\data\testdir' #need to change this to your directory for it to work
    suf = '.c'
    
    find_files(suf, path)
    
#tests()
