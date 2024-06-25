from config import *

import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

# def annotate_image_manual(image, results):
#     print(results)
#     for result in results:
#         if result.boxes:
#             for i in range(len(result.boxes)):
#                 box = result.boxes[i]
#                 index = int(box.cls.item())
#                 tensor = box.xyxy[0]
#                 x1 = int(tensor[0].to('cpu').item())
#                 y1 = int(tensor[1].to('cpu').item())
#                 x2 = int(tensor[2].to('cpu').item())
#                 y2 = int(tensor[3].to('cpu').item())
#                 cv2.rectangle(image,(x1,y1),(x2,y2),COLOR[index],1)
#     return image

def annotate_image(image, model):
    annotator = Annotator(image,
                          font_size=1,
                          )
    results = model.predict(image)
    for r in results:
        if r.boxes:
            for box in r.boxes:
                bbox = box.xyxy[0]
                class_names = model.names[int(box.cls)]
                annotator.box_label(bbox, class_names, color=(0, 0, 255), txt_color=(255, 255, 255))
    
    image = annotator.result() 
    return image

def read_image(image_path,
               model=None):
    image = cv2.imread(image_path)
    if model is not None:
        image = annotate_image(image, model)
    
    cv2.imshow(f"{image_path}", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_video(video_path,
               model=None):
    cap = cv2.VideoCapture(video_path)
    totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    
    # if myFrameNumber >= 0 & myFrameNumber <= totalFrames:
    #     # set frame position
    #     cap.set(cv2.CAP_PROP_POS_FRAMES,myFrameNumber)
    
    while True : 
        ret, frame = cap.read()     
        if model is not None : 
            frame = annotate_image(frame, model)
        cv2.imshow(f"{video_path}", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()
    