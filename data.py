import json
import requests
from pprint import pprint

url = "http://api.lolesports.com/api/v1/leagues?slug=worlds"

re = requests.get(url=url)

if re.status_code == 200:
    data = json.loads(re.text)
    pprint(data)
else:
    print(re.status_code)


#     "http://esports-api.com/api/leagueoflegends/teams/{teamId}"
#     "http://esports-api.com/api/leagueoflegends/teams/11"
#
# Response JSON
#
#     {
#         "Data": {
#             "homeLeague": 2,
#             "subs": [
#                 {
#                     "role": "Mid Lane",
#                     "name": "Reginald",
#                     "id": 62
#                 }
#             ],
#             "acronym": "TSM",
#             "logoUrl": "https://lolstatic-a.akamaihd.net/esports-assets/production/team/team-solomid-50imvfy0.png",
#             "teamPhotoUrl": "http://na.lolesports.com/",
#             "altLogoUrl": "https://lolstatic-a.akamaihd.net/esports-assets/production/team/team-solomid-bjjwknt9.png",
#             "starters": [
#                 {
#                     "role": "Mid Lane",
#                     "name": "Bjergsen",
#                     "id": 60
#                 },
#                 {
#                     "role": "AD Carry",
#                     "name": "Doublelift",
#                     "id": 153
#                 },
#                 {
#                     "role": "Jungler",
#                     "name": "Svenskeren",
#                     "id": 171
#                 },
#                 {
#                     "role": "Top Lane",
#                     "name": "Hauntzer",
#                     "id": 345
#                 },
#                 {
#                     "role": "Support",
#                     "name": "Biofrost",
#                     "id": 1158
#                 }
#             ],
#             "bios": [
#                 {
#                     "lang": "fr_FR",
#                     "text": "TSM se place régulièrement parmi les meilleures équipes des LCS NA. Avec son historique très riche qui remonte a...."
#                 },
#                 {
#                     "lang": "pt_BR",
#                     "text": "Depois de sofrer uma derrota esmagadora contra a Counter Logic Gaming nas Finais da Etapa de Primavera da NA LCS...."
#                 },
#                 {
#                     "lang": "en_US",
#                     "text": "After suffering a crushing defeat to Counter Logic Gaming in the 2016 NA LCS Spring Split Finals, TSM has been o...."
#                 },
#                 {
#                     "lang": "es_AR",
#                     "text": "Después de sufrir una derrota aplastante ante Counter Logic Gaming en la final del torneo de apertura de la LCS...."
#                 },
#                 {
#                     "lang": "de_DE",
#                     "text": "Nach der vernichtenden Niederlage gegen Counter Logic Gaming im Finale des Frühjahrs-Splits der NA LCS 2016 hat...."
#                 },
#                 {
#                     "lang": "pl_PL",
#                     "text": "TSM to najbardziej rozpoznawalna na świecie zachodnia organizacja. Powstała jako jedna z pierwszych, jeszcze w ...."
#                 },
#                 {
#                     "lang": "es_ES",
#                     "text": "Tras sufrir una desalentadora derrota contra Counter Logic Gaming en la final del split de primavera de la LCS ...."
#                 }
#             ],
#             "updatedAt": [
#                 2016,
#                 9,
#                 8,
#                 21,
#                 40,
#                 21
#             ],
#             "id": 11,
#             "name": "TSM"
#         }
#     }
