# Bug Guide Unofficial API

Explore the data-set of 35447 insects!

Based on bugguide.net’s multiple .txt sets, I created an API to deliver insects’ data in JSON format. At present, the API only delivers the common name, genus, species, family, order, bug_guide_id, and bugguide.net URL information.

## API Endpoint

```https://bugs.deadauthor.org?api&```

## Documentation

Data can be parsed as JSON. Access to the bugs.deadauthor.org doesn't require a token-based authentication. Kindly avoid sending too many requests. Please consider [donating](https://paypay.me/mighil) if you plan to actively use the API.

## Examples

| Query Type  |  URL |
|---|---|
| Query a common name  | ```GET https://bugs.deadauthor.org?api&common_name=Brown%20Angle%20Shades``` |
| Query a genus  | ```GET https://bugs.deadauthor.org?api&genus=Oligotoma``` |
| Query species  | ```GET https://bugs.deadauthor.org?api&species=nigra``` |
| Query a family  | ```GET https://bugs.deadauthor.org?api&family=Oedemeridae``` |
| Query an order  | ```GET https://bugs.deadauthor.org/?api&order=Coleoptera``` |
| Query a bug_guide_id  | ```GET https://bugs.deadauthor.org?api&bug_guide_id=389``` |
| Query combination example  | ```GET https://bugs.deadauthor.org?api&species=scrutator&order=Coleoptera``` |

## Alpha disclaimer

The bugs.deadauthor.org API is actually in the alpha stage, which implies that "bugs" and issues may still remain undiscovered until this phase of testing is complete.

The alpha stage also means that the data may be corrupted, is not 100% validated or complete, and is subject to change.

Finally, services may have downtime and the API schemas and calls are subject to change
