import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import numpy as np
import json

# 0 	T-shirt/top
# 1 	Trouser
# 2 	Pullover
# 3 	Dress
# 4 	Coat
# 5 	Sandal
# 6 	Shirt
# 7 	Sneaker
# 8 	Bag
# 9 	Ankle boot

result_match = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]

API_endpoint = input("Please input the API endpoint: ")
Tk().withdraw()

filename = askopenfilename()
img = Image.open(filename)
img_array = str((np.asarray(img).astype(np.float32)/255).reshape((1,-1)).tolist())

predict_data = {'data':img_array}
resp = requests.post("http://"+API_endpoint,json=predict_data)

index = np.array(json.loads(resp.text)[0]).argmax(axis=0)
print("What you have is a: {}".format(result_match[index]))