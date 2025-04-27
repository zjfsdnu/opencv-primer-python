from ultralytics import YOLO
import cv2

# 加载预训练模型（YOLOv8n 是 Nano 版本，速度最快）
model = YOLO("yolov8n.pt")  # 可选: yolov8s.pt, yolov8m.pt 等

# 打开视频文件或摄像头
# video_path = "nice.mp4"  # 替换为你的视频路径
video_path = "ppp.mp4"  # 替换为你的视频路径
cap = cv2.VideoCapture(video_path)  # 用 0 替换为摄像头（如 cap = cv2.VideoCapture(0)）

# 获取视频属性（用于保存结果）
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 保存检测结果（可选）
output_path = "output_video2.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编码格式
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# 逐帧处理视频
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv8 检测（结果直接绘制在帧上）
    results = model.predict(frame, conf=0.5)  # conf 是置信度阈值
    annotated_frame = results[0].plot()  # 自动绘制检测框

    # 显示实时结果
    cv2.imshow("YOLOv8 Video Detection", annotated_frame)

    # 保存结果（可选）
    out.write(annotated_frame)

    # 按 'q' 退出
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
print(f"检测完成！结果已保存到: {output_path}")