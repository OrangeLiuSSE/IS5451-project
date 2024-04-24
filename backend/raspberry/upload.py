import requests

def upload_image(image_path):
    url = 'http://172.20.10.4:5010/uploadImage'
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    print(response.text)
    
def upload_environment_data(humidity, temperature, pressure, ph, light):
    url = 'http://172.20.10.4:5010/putNewData/?humidity={}&temperature={}&pressure={}&ph={}&light={}'.format(humidity, temperature, pressure, ph, light)
    response = requests.post(url)
    print(response.text)