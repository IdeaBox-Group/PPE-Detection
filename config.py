import torch
from ultralytics import YOLO

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MODEL_PATH = f'models\model-06-24-17-56_Roboflow APD Detection.pt'
COLOR = {
      0 : (0, 0, 0),
      1 : (255, 0, 0),
      2 : (0, 255, 0),
      3 : (0, 0, 255),
      4 : (255, 255, 0),
      5 : (255, 0 , 255),
      6 : (0, 255, 255),
      7 : (255, 255, 255)
  }

def get_model():
    model = YOLO(MODEL_PATH)
    model.to(DEVICE)
    return model