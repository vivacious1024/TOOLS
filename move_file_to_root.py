import os
import shutil

def move_files_to_root(root_folder):
    """
    将指定大文件夹下所有子文件夹中的非文件夹文件移动到大文件夹根目录。
    
    :param root_folder: 大文件夹的路径
    """
    # 遍历大文件夹及其所有子文件夹
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # 如果当前路径是根文件夹，跳过
        if dirpath == root_folder:
            continue
        
        # 遍历当前文件夹中的所有文件
        for filename in filenames:
            # 构造原始文件路径
            file_path = os.path.join(dirpath, filename)
            
            # 构造目标文件路径
            dest_path = os.path.join(root_folder, filename)
            
            # 如果目标文件已存在，避免覆盖，通过添加后缀区分
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(filename)
                count = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(root_folder, f"{base}_{count}{ext}")
                    count += 1
            
            # 移动文件到目标路径
            shutil.move(file_path, dest_path)
            print(f"Moved: {file_path} -> {dest_path}")
    
    print("文件整理完成！")


def remove_empty_folders(folder):
    """
    删除空文件夹，可选项
    """
    for dirpath, dirnames, _ in os.walk(folder, topdown=False):
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            if not os.listdir(dir_to_check):  # 如果文件夹为空
                os.rmdir(dir_to_check)       # 删除空文件夹
                print(f"Removed empty folder: {dir_to_check}")


def main():
    # 示例：使用该函数
    root_folder_path = "F:\认知科学初探作业汇总 - 副本"  # 替换为你的大文件夹路径
    move_files_to_root(root_folder_path)
    remove_empty_folders(root_folder_path)


if __name__ == "__main__":
    main()
