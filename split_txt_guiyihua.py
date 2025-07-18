'''功能
        归一化并且将所有输出统一复制到一个文件夹下。
        便于随机划分，和保存源文件
'''
import os
def normalize_line(line, image_width, image_height):
    """
    归一化单行标签数据。
    
    参数:
    line (str): 从.txt文件中读取的一行数据。
    image_width (int): 图像的宽度。
    image_height (int): 图像的高度。
    
    返回:
    str: 归一化后的字符串，或者如果行格式不正确则返回None。
    """
    parts = line.strip().split(',')
    if len(parts) != 5:  # 确保行数据包含5个部分：类别ID，x中心，y中心，宽度，高度
        return None
    class_id, x_center, y_center, w, h = map(float, parts)  # 将字符串转换为浮点数
    # 归一化坐标和尺寸，类别ID保持为整数
    norm_x_center = x_center / image_width
    norm_y_center = y_center / image_height
    norm_w = w / image_width
    norm_h = h / image_height
    # 格式化归一化后的字符串，类别ID转换为整数
    return f"{int(class_id)} {norm_x_center:.6f} {norm_y_center:.6f} {norm_w:.6f} {norm_h:.6f}"
def process(input_folder, output_folder, image_width, image_height):
    """
    处理文件夹中的所有.txt文件，归一化标签数据，并保存到输出文件夹。
    
    参数:
    input_folder (str): 包含原始.txt文件的输入文件夹路径。
    output_folder (str): 归一化文件保存的输出文件夹路径。
    image_width (int): 图像的宽度。
    image_height (int): 图像的高度。
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # 如果输出文件夹不存在，则创建
    file_number = 1  # 初始化文件编号
    for root, dirs, files in os.walk(input_folder):  # 遍历输入文件夹
        for file in files:
            if file.endswith('.txt'):  # 筛选.txt文件
                file_path = os.path.join(root, file)  # 获取文件完整路径
                with open(file_path, 'r') as file:  # 打开文件读取
                    lines = file.readlines()  # 读取所有行
                normalized_lines = []  # 初始化归一化行列表
                for line in lines:
                    normalized_line = normalize_line(line, image_width, image_height)  # 归一化每行
                    if normalized_line:  # 如果归一化成功
                        normalized_lines.append(normalized_line)  # 添加到列表
                # 保存归一化后的数据到输出文件夹中的新文件
                output_file_name = f'file_{file_number}.txt'  # 格式化文件名
                output_file_path = os.path.join(output_folder, output_file_name)  # 获取输出文件路径
                with open(output_file_path, 'w') as file:  # 打开文件写入
                    file.writelines('\n'.join(normalized_lines))  # 写入归一化行
                file_number += 1  # 增加文件编号
# 设置输入输出文件夹路径和图像大小
input_folder = "E:/dataset/labels" 
output_folder = "E:/datasetguiyi/labels" 
image_width = 640
image_height = 480
# 调用函数处理数据
process(input_folder, output_folder, image_width, image_height)
print("归一化完成，归一化后的文件已保存到输出文件夹。")






    
                
                
                








    
    
   










