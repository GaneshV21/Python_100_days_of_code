import requests
import datetime
pixela_endpoint="https://pixe.la/v1/users"
USERNAME=USERNAME
Token=Token
headers={
    "X-USER-TOKEN":Token
}

users_params={
    "token":token,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(pixela_endpoint,json=users_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter={
    "id":"graph21",
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"sora"
}

# response=requests.post(graph_endpoint,json=graph_parameter,headers=headers)
# print(response.text)

add_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph21"

date=str(datetime.datetime.now())
new_date=date.split(" ")[0].split("-")
new_date="".join(new_date)
print(new_date)

new_date2= datetime.datetime.now().strftime("%Y%m%d")
print(new_date2)
add_pixel_parameter={
    "date":new_date,
    "quantity":input("How many kilometers did you cycle today? ")
}

# response=requests.post(add_pixel_endpoint,json=add_pixel_parameter,headers=headers)
# print(response.text)

# put  and delete:

update_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph21/{new_date}"
update_pixel_parameter={
    "quantity":"21.8"
}
# response=requests.put(update_pixel_endpoint,json=update_pixel_parameter,headers=headers)
# print(response.text)

delete_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph21/{new_date}"
response=requests.delete(delete_pixel_endpoint,headers=headers)
print(response.text)