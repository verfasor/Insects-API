# An Unofficial REST API for bugguide.net.

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

## Alpha disclaimer

The bugs.verfasor.com REST API is actually in the alpha stage, which implies that "bugs" and issues may still remain undiscovered until this phase of testing is complete. The alpha stage also means that the data may be corrupted, is not 100% validated or complete, and is subject to change.

Finally, services may have downtime and the API schemas and calls are subject to change
