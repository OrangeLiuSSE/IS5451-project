from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from data_operator import insert_env_data, user_login, user_register
import os
from recognition import get_plant_condition
from get_cluster import get_humidity_cluster, get_light_cluster

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/putNewData')
def putEnvironmentData():
   humidity = request.args.get('humidity')
   temperature = request.args.get('temperature')
   pressure = request.args.get('pressure')
   ph = request.args.get('ph')
   light = request.args.get('light')
   insert_env_data(humidity, temperature, pressure, ph, light)
   return f"Environment Information: H:{humidity}, T:{temperature}, P:{pressure}, PH:{ph}, L:{light}", 200
 
@app.route('/uploadImage', methods=['POST'])
def upload_file():
   if 'file' not in request.files:
      return 'No file', 400
   file = request.files['file']
   if file.filename == '':
      return 'No selected file', 400
   if file:
      filename = secure_filename(file.filename)
      file.save(os.path.join('data/image', filename))
      return get_plant_condition(os.path.join('data/image', filename)), 200
   

@app.route('/getLightCondition')
def get_light_condition():
   light = request.args.get('light')
   result = get_light_cluster(light)
   return result, 200


@app.route('/getHumidityCondition')
def get_humidity_condition():
   humidity = request.args.get('humidity')
   result = get_humidity_cluster(humidity)
   return result, 200

@app.route('/user_login', methods=['POST'])
def user_auth():
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        return user_login(username, password)
    else:
        return 'No JSON received', 400


@app.route('/user_register', methods=['POST'])
def user_regis():
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        return user_register(username, password)
    else:
        return 'No JSON received', 400
     

@app.route('/api/plants/<plantID>/conditions')
def get_plant_conditions(plantID):
   result = {
      "plantId": 1,
      "humidity": 50,
      "temperature": 22,
      "lightLevel": 300,
      "atmosphericPressure": 1013
  }
   return jsonify(result), 200

@app.route('/api/plants')
def get_all_plants():
   result = [
      {
         "plantId": 1,
         "plantName": "Fern",
         "plantStatus": "NORMAL"
      },
      {
         "plantId": 2,
         "plantName": "Bamboo",
         "plantStatus": "MAINTAIN"
      },
      {
         "plantId": 3,
         "plantName": "Cactus",
         "plantStatus": "DANGEROUS"
      }
   ]
   return jsonify(result), 200

# localhost:5010/api/plants/<plantId>/action?action=water
@app.route('/api/plants/<plantId>/action')
def take_action(plantId):
   action = request.args.get('action')
   result = action + " has been done..."
   return result, 200

#/api/plants/{plantId}/environmental-data/line-chart/{dataType}
@app.route('/api/plants/<plantId>/environmental-data/line-chart/<dataType>')
def get_chart_data(plantId, dataType):
   result = {
      "value":
         {
            "name": dataType,
            "data": [20, 31, 15, 31, 69, 22, 39, 61, 28]
         }
   }
   return jsonify(result), 200

#/api/plants/{plantId}/environmental-data/pie-chart/{dataType}
@app.route('/api/plants/<plantId>/environmental-data/pie-chart/<dataType>')
def get_pie_data(plantId, dataType):
   result = [
      {
         "type": "humidity",
         "standardData": 27,
         "currentData": 50,
      },
      {
         "type": "light",
         "standardData": 27,
         "currentData": 50,
      },
      {
         "type": "temperature",
         "standardData": 27,
         "currentData": 50,
      }
   ]
   return jsonify(result), 200
   

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5010)
   