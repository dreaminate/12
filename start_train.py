import time
from ultralytics import YOLO

model = YOLO('E:/ultralytics-main/runs/detect/train15/weights/last.pt') 
results = model.train(data='E:/ultralytics-main/A_my_data.yaml', epochs=10, imgsz=640, device=[0,], workers=0, batch=32, cache=True)  
time.sleep(10)                                                   


