# An Unofficial REST API for BugGuide.net

![](https://github.com/migftw/bugguide-api/blob/master/BugGuide-API.png)

Explore the data-set of 40511 insects!

Based on json-server and bugguide.net’s multiple .txt sets, I created an API to deliver insects’ data in JSON format. At present, the API only delivers the common name, genus, species, family, order, bug_guide_id, and bugguide.net URL information.

## API Endpoint

```https://bugs.verfasor.com/api```

## Documentation

Data can be parsed as JSON. Access to the bugs.verfasor.com doesn't require a token-based authentication. Please use it for development and testing only. And kindly avoid sending too many requests to Vercel, who's hosting the REST API.

## Examples

White space between the words are fine, mmkay.

| Query Type  |  URL |
|---|---|
| General query | ```GET https://bugs.verfasor.com/api?q=Soldier%20Beetle``` |
| Query a Common Name  | ```GET https://bugs.verfasor.com/api?q=Soldier%20Beetle``` |
| Query a Genus  | ```GET https://bugs.verfasor.com/api?Genus=Chauliognathus``` |
| Query Species  | ```GET https://bugs.verfasor.com/api?Species=pensylvanicus``` |
| Query a Family  | ```GET https://bugs.verfasor.com/api?Family=Cantharidae``` |
| Query an Order  | ```GET https://bugs.verfasor.com/api?Order=Coleoptera``` |
| Query a Bug Guide ID  | ```GET https://bugs.verfasor.com/api?BugGuideID=438``` |
| Query combination and filter  | ```GET https://bugs.verfasor.com/api?Order=Coleoptera&q=beetle``` |

## Get a random bug info in Python

```
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
```

## Alpha disclaimer

The bugs.verfasor.com REST API is actually in the alpha stage, which implies that "bugs" and issues may still remain undiscovered until this phase of testing is complete. The alpha stage also means that the data may be corrupted, is not 100% validated or complete, and is subject to change. Finally, services may have downtime and the API schemas and calls are subject to change
