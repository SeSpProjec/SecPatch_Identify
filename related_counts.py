

import os

# 相关路径的设定
Count_path = "/mnt/server_share_file/PatchRNN/data/our2（contra）/security_patch/AST"

def count_files(path):
    """
    Counts the number of files in a given directory and its subdirectories.

    Args:
        path (str): The path to the directory to count files in.

    Returns:
        int: The total number of files in the directory and its subdirectories.
    """
    count = 0
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            count += count_files(file_path)
        else:
            count += 1
    return count

if __name__ == '__main__':
    print("当前路径 ",Count_path,"共有补丁数：",count_files(Count_path),"个")