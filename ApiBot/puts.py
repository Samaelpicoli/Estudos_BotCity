from botcity.plugins.http import BotHttpPlugin

#realizando requests com botcity na página reqres.in

url_base = 'https://reqres.in/api'

#Realizando PUTs

#instanciando a classe com a url + endpoint da página

#1) Atualizar usuário
http = BotHttpPlugin(url_base + "/users/2")
parametros = {
    "name": "morpheus",
    "job": "zion resident"
}
#passo os parametros que a página solicita para o POST
http.set_params(parametros)
resultado = http.post().text
print(resultado)

