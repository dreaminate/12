from ultralytics import YOLO
model = YOLO('E:/ultralytics-main/runs/detect/train14/weights/best.pt')
validation_results = model.val(data= 'E:/ultralytics-main/B_my_data.yaml', imgsz=640, batch=4, conf=0.25, iou=0.6, device="0", workers=0)






