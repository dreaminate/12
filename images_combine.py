'''

更改图片名，使其与输出文件名对应，
并输出到另一文件夹，保存原文件，方便后续操作

'''

import os
import shutil
def duplicate_and_rename_images(source_directory, target_directory):
    """
    将源目录中的所有JPEG图片复制到目标目录，并按顺序重命名为'图片_N.jpg'，其中N是递增的整数。

    参数：
    source_directory (str)：包含原始JPEG文件的源目录路径。
    target_directory (str)：复制和重命名后的文件保存的目标目录路径。
    """
    # 如果目标目录不存在，则创建目标目录
    os.makedirs(target_directory, exist_ok=True)
    # 初始化文件计数器，用于生成新的文件名
    file_counter = 1
    # 遍历源目录中的每个子目录
    for directory_name in os.listdir(source_directory):
        directory_path = os.path.join(source_directory, directory_name)
        # 检查路径是否为目录
        if os.path.isdir(directory_path):
            # 在目录中查找所有以.jpg结尾的文件
            jpeg_files = [file for file in os.listdir(directory_path) if file.lower().endswith('.jpg')]
            for jpeg_file in jpeg_files:
                # 构造新的文件名，并带有递增的索引
                formatted_filename = f'图片_{file_counter}.jpg'
                destination_file_path = os.path.join(target_directory, formatted_filename)
                # 将JPEG文件从源目录复制到目标目录，并使用新名称
                shutil.copy(os.path.join(directory_path, jpeg_file), destination_file_path)
                # 为下一个文件递增文件计数器
                file_counter += 1
# 定义源目录和目标目录的路径
source_dir = "E:/dataset/images"
target_dir = "E:/datasetguiyi/images"
# 执行函数复制和重命名图片
duplicate_and_rename_images(source_dir, target_dir)
print("图片复制和重命名完成；文件已保存在目标文件夹。")


    
    
        
            
                
                



    








    

    
        
           
            
                
                
               





