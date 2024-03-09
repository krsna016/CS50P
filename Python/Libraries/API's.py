import json
import pprint
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# Here we are using the iTunes API to search for a song, The API returns a JSON object.
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")
# This is the response object, it contains the status code, the headers and the body of the response.
# # pprint.pprint(response.json())
# # print(json.dumps(response.json(), indent=4))
obj = response.json()
print("The trackName is : ")
for result in obj["results"]:
    print(result["trackName"])