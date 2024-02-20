from botcity.plugins.http import BotHttpPlugin

#realizando requests com botcity na página reqres.in

url_base = 'https://reqres.in/api'

#Realizando GETs

#instanciando a classe com a url + endpoint da página

#1) Lista de usuários
http = BotHttpPlugin(url_base + "/users?page=2")
print(http.get().text)
print(http.get().status_code)

#2) Um único usuário
http = BotHttpPlugin(url_base + "/users/2")
print(http.get().text)
print(http.get().status_code)

#3) Um único usuário não encontrado
http = BotHttpPlugin(url_base + "/users/23")
print(http.get().status_code)

#4) Lista - Resources
http = BotHttpPlugin(url_base + "/unknown")
print(http.get().text)
print(http.get().status_code)

#5) Único - Resources
http = BotHttpPlugin(url_base + "/unknown/2")
print(http.get().text)
print(http.get().status_code)

#6) Único - Resources - não encontrado
http = BotHttpPlugin(url_base + "/unknown/23")
print(http.get().text)
print(http.get().status_code)
