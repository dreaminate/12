'''功能：
        1.数据集划分: 按照比例8:1:1
        2.图片复制，保留源文件，便于之后其他训练
        3.标签文件处理：清楚无效输出，保留有效输出，比如若输出不符合预期格式，则忽略
        4.随机性控制，保留复原结果的可能，或者其他用途
        5.功能函数化,更换环境出现bug方便修改
        '''
import os
import shutil
import random
def split_dataset(images_folder, labels_folder, output_folder, train_ratio, test_ratio, val_ratio):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg')]
    label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]
    assert set([f.split('.')[0] for f in image_files]) == set([f.split('.')[0] for f in label_files]), "Images and labels do not match"
    total_files = len(image_files)
    train_size = int(total_files * train_ratio)
    test_size = int(total_files * test_ratio)
    val_size = total_files - train_size - test_size
    random.seed(10656)  
    random.shuffle(image_files)
    train_images = image_files[:train_size]
    test_images = image_files[train_size:train_size + test_size]
    val_images = image_files[train_size + test_size:]
    for subset in ['train', 'test', 'val']:
        os.makedirs(os.path.join(output_folder, 'images', subset), exist_ok=True)
        os.makedirs(os.path.join(output_folder, 'labels', subset), exist_ok=True)
    for image_list, subset in [(train_images, 'train'), (test_images, 'test'), (val_images, 'val')]:
        for image_name in image_list:
            # 复制图片
            image_src = os.path.join(images_folder, image_name)
            image_dst = os.path.join(output_folder, 'images', subset, image_name)
            shutil.copy(image_src, image_dst)
            # 复制标签
            label_name = image_name.replace('.jpg', '.txt')
            label_src = os.path.join(labels_folder, label_name)
            label_dst = os.path.join(output_folder, 'labels', subset, label_name)
            shutil.copy(label_src, label_dst)
input_images_folder = "E:/datasetguiyi/images" 
input_labels_folder = "E:/datasetguiyi/labels"  
output_folder = "E:/ultralytics-main/data2" 
# 分割比例
train_ratio = 0.8
test_ratio = 0.1
val_ratio = 0.1
split_dataset(input_images_folder, input_labels_folder, output_folder, train_ratio, test_ratio, val_ratio)
print("数据集分割完成，训练集、测试集和验证集已保存到输出文件夹。")

    
    
    
    
    
    
            





            

   
        
            
            

   
    
    
    
    
    
   
    
   
    
    
   



    
    
    
            
            
            


