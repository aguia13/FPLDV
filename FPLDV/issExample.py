import requests

parameters = {"lat":37.78,"lon":-122.41}

response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)
data = response.json()


#endpoint to how many ppl are on iss
people = requests.get("http://api.open-notify.org/astros.json")
pData = people.json()

print(pData["number"])
print(pData)

#print(data)
#print(response.headers)