# example

import requests
import json


s = requests.get('https://bugs.deadauthor.org?api&common_name=Saunders%27%20Embiid')
data = s.json()

with open('data.json', 'w') as alpha:
    json.dump(data, alpha)

with open('data.json') as beta:
  data2 = json.load(beta)    
  
with open('data.json', "w+") as op:
    for item in data2.values():
        json.dump(item, op)   

with open('data.json') as gamma:
  data3 = json.load(gamma)  
  common_name = data3['common_name']  
  print(common_name) 
        
