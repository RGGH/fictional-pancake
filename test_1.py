import requests

url = "https://neuro-2fle3wxkia-nw.a.run.app/vars"

params = {"weeks":"2","years":"3","books":"3","projects":"2","earn":"44"}

answer = requests.post(url, json = params)

print(answer.text)