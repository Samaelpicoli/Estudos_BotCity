from botcity.plugins.http import BotHttpPlugin

#realizando requests com botcity na página reqres.in

url_base = 'https://reqres.in/api'

#Realizando POST e convertendo em Json

#instanciando a classe com a url + endpoint da página

#1) Criando usuário
http = BotHttpPlugin(url_base + "/users")
parametros = {
    "name": "morpheus",
    "job": "leader"
}
#trazendo o post em formato json e acessando uma chave
http.set_params(parametros)
resultado = http.post_as_json()['job']
print(resultado)

#Realizando GETs e salvando em JSON

#instanciando a classe com a url + endpoint da página

#2) Lista de usuários, trazendo os dados em formato json e acessando uma chave
http = BotHttpPlugin(url_base + "/users?page=2")
print(http.get_as_json()['data'][1]['email'])
