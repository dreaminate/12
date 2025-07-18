'''

确定有多少个类别，防止bug
'''
import os
def collect_distinct_labels(label_directory):
    """
    从指定的标签目录中收集所有.txt文件的第一个数字，并返回一个不重复的数字集合。
    参数:
    label_directory (str): 包含标签的目录路径。
    返回:
    set: 包含所有唯一数字的集合。
    """
    distinct_labels = set()  # 使用set来存储唯一的标签
    # 遍历标签目录中的所有子目录和文件
    for directory_name in os.listdir(label_directory):
        directory_path = os.path.join(label_directory, directory_name)
        if os.path.isdir(directory_path):  # 确保是目录
            for file_name in os.listdir(directory_path):
                if file_name.endswith('.txt'):  # 筛选.txt文件
                    file_full_path = os.path.join(directory_path, file_name)
                    with open(file_full_path, 'r') as label_file:
                        for label_line in label_file:
                            line_parts = label_line.strip().split(',')
                            if line_parts and line_parts[0].isdigit():  # 检查第一个元素是否为数字
                                distinct_labels.add(int(line_parts[0]))  # 添加到集合中
                                break  # 找到第一个数字后即跳出循环
    return distinct_labels
labels_path = "E:/dataset/labels"  
all_labels = collect_distinct_labels(labels_path)
print("从.txt文件中提取的唯一标签:")
for label in sorted(all_labels):
    print(label)









    
   
        
            
                            
                                







