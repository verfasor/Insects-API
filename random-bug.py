import requests
import json
import random

seed = random.randint(0, 40510)
print(seed)

# API
link = 'https://bugs.verfasor.com/api'

# Request data
data = requests.get(link).text

# Print stuff you like
number = json.loads(data)
print("%s" % (number[seed]["Number"]))

genus = json.loads(data)
print("%s" % (genus[seed]["Genus"]))

species = json.loads(data)
print("%s" % (species[seed]["Species"]))

family = json.loads(data)
print("%s" % (family[seed]["Family"]))

order = json.loads(data)
print("%s" % (order[seed]["Order"]))

bugguideid = json.loads(data)
print("%s" % (bugguideid[seed]["BugGuideID"]))

url = json.loads(data)
print("%s" % (url[seed]["URL"]))

commonname = json.loads(data)
print("%s" % (commonname [seed]["CommonName"]))