
import os

root = "testdir"


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
    if (os.path.isdir(path) or os.path.isfile(path)) is not True:
        return None

    data = os.listdir(path=path)

    result = []

    for val in data:
        url = os.path.join(path, val)
        if os.path.isfile(url):
            if url.endswith(suffix):
                result.append(url)
        else:
            result += find_files(suffix, url)
    return result


print(find_files(".c", root))
print(find_files(".h", root))
print(find_files(".txt", root))
print(find_files(".txt", "asd"))