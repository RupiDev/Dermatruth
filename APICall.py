import requests
import json


filesForFirstParse = {
    'api_key': (None, 'gryzgcX2dsic4Rrj1oZKEvx-x79rE5tf'),
    'api_secret': (None, 'WmhD0zJCtwcHKwP6qmDtnzhVpO_hU5HB'),
    'image_file': ('X.png', open('X.png', 'rb')),
    'return_landmark': (None, '1'),
    'return_attributes': (None, 'age,gender'),
}

response = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', files=filesForFirstParse)
result = json.loads(response.text)
x = result["faces"]
y = (x[0])
faceToken = y["face_token"]


filesForSecondParse = {
	'api_key': (None, 'gryzgcX2dsic4Rrj1oZKEvx-x79rE5tf'),
    'api_secret': (None, 'WmhD0zJCtwcHKwP6qmDtnzhVpO_hU5HB'),
    'return_attributes': (None, 'age,gender,skinstatus'),
    'face_tokens': (None, faceToken),
}

response = requests.post('https://api-us.faceplusplus.com/facepp/v3/face/analyze', files=filesForSecondParse)
result = json.loads(response.text)
x = result["faces"]
y = (x[0])
z = y["attributes"]
skinItems = z["skinstatus"]

darkCicleNumber = skinItems["dark_circle"]
stainNumber = skinItems["stain"]
acneNumber = skinItems["acne"]
healthNumber = skinItems["health"]

print(darkCicleNumber)
print(stainNumber)
print(acneNumber)
print(healthNumber)