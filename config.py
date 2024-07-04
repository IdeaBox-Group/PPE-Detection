import torch
from ultralytics import YOLO

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MODEL_PATH = f'models\model-06-24-17-56_Roboflow APD Detection.pt'
VIDEO_TEST_PATH = 'datasets\\test_video.mp4'
IMAGE_TEST_PATH = 'datasets\\test_image.jpg'

def get_model():
    model = YOLO(MODEL_PATH)
    model.to(DEVICE)
    return model
