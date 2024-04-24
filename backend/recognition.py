import torch
from torchvision import transforms
from PIL import Image


def get_plant_condition(image_path):
    label = ['bacteria', 'fungi', 'healthy', 'pests', 'virus']
    model = torch.load('recognition/model_recognition.pth')
    model.eval()
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(image_path)
    img_tensor = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        output = model(img_tensor)
        _, pred = torch.max(output, 1)
    
    return label[pred.item()]


if __name__ == "__main__":
    print(get_plant_condition("data/image_1441.jpg"))