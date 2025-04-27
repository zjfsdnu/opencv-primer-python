from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 加载预训练模型
# results = model("../boat.jpg")  # 预测
# results = model("lqd.jpg")  # 预测
results = model("fz.jpg")  # 预测
results[0].show()  # 显示结果
