from botcity.plugins.http import BotHttpPlugin

#realizando requests com botcity na página reqres.in

url_base = 'https://reqres.in/api'

#Realizando POSTs

#instanciando a classe com a url + endpoint da página

#1) Criando usuário
http = BotHttpPlugin(url_base + "/users")
parametros = {
    "name": "morpheus",
    "job": "leader"
}
#passo os parametros que a página solicita para o POST
http.set_params(parametros)
resultado = http.post().text
print(resultado)


#2) Registrar com Sucesso
http = BotHttpPlugin(url_base + "/register")

params = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
#passo os parametros que a página solicita para o POST
http.set_params(params)
resultado = http.post().text
print(resultado)

#3) Registrar com falha
http = BotHttpPlugin(url_base + "/register")

params = {
    "email": "sydney@fife"
}
#passo os parametros que a página solicita para o POST
http.set_params(params)
resultado = http.post().text
print(resultado)

#4) Realizar login
http = BotHttpPlugin(url_base + "/login")

params = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
#passo os parametros que a página solicita para o POST
http.set_params(params)
resultado = http.post().text
print(resultado)

#5) Login com falha
http = BotHttpPlugin(url_base + "/login")

params = {
    "email": "sydney@fife"
}
#passo os parametros que a página solicita para o POST
http.set_params(params)
resultado = http.post().text
print(resultado)

#6) Atualizar usuário
http = BotHttpPlugin(url_base + "/users/2")
parametros = {
    "name": "morpheus",
    "job": "zion resident"
}
#passo os parametros que a página solicita para o POST
http.set_params(parametros)
resultado = http.post().text
print(resultado)