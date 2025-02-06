import requests
import datetime

#today's date
today = str(datetime.date.today())
today = today.replace('-','')

TOKEN = "has23r4nfk4erADF145FQqefinf55"
USERNAME = "ankush123"

pixela_enp = "https://pixe.la/v1/users"
graph_enp = f"{pixela_enp}/{USERNAME}/graphs"
pixel_enp = f"{graph_enp}/graph1"
edit_enp = f"{pixel_enp}/{today}"

user_params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

graph_config = {
    'id' : 'graph1',
    'name' : 'Reading Graph',
    'unit' : 'number of pages',
    'type' : 'int',
    'color' : 'momiji'
}

pixel_config = {
    'date' : today,
    'quantity' : input("How many pages did you read today?")
}

Headers = {
    'X-USER-TOKEN' :  TOKEN
}

new_data = {
    "quantity" : '20'
}



#response = requests.post(url=pixela_enp, json = user_params)
#print(response.text)

#response = requests.post(url=graph_enp, json = graph_config, headers=Headers)
#print(response.text)

#response = requests.post(url=pixel_enp, json = pixel_config, headers=Headers)
#print(response.text)

#response = requests.put(url=edit_enp, json = new_data, headers=Headers)
#print(response.text)

response = requests.delete(url=edit_enp, headers=Headers)
print(response.text)