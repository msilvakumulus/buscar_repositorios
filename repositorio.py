import requests

user = input("Por favor, digite o nome de busca:")

r = requests.get("https://api.github.com/users/"+str(user)+"/repos")

print("Lista de repositórios: ")
for i in r.json():
    if isinstance(i, dict):
        print(i["name"])

r.close()
