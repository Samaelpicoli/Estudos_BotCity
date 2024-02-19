from botcity.plugins.googledrive import BotGoogleDrivePlugin
import os

#fazer upload de arquivos no google drive

#coloque sua senha do Google Drive na variável chave, nesse caso estou buscando nas minhas váriaveis de ambiente
chave = os.getenv('CHAVE_GOOGLE')

#instanciando a classe
google_drive = BotGoogleDrivePlugin(chave)

#com a classe instanciada posso fazer upload e downloads de arquivos no google drive

#upload - preciso passar o id da pasta onde vou subir o arquivo
id_pasta = google_drive.search_folder_by_name('estudos-rpa')
pasta = os.path.dirname(__file__)
print(pasta)

caminho_pasta = os.path.dirname(__file__) + '\\imagens'
arquivos = os.listdir(caminho_pasta)

for arquivo in arquivos:
    nome_arquivo = f'{caminho_pasta}\\{arquivo}'
    print(nome_arquivo)
    #para fazer o upload preciso do nome do arquivo, e o nome da pasta no google drive
    google_drive.upload_file(file_path=nome_arquivo, parent_folder_id=id_pasta, file_name=arquivo)

#download
#para fazer o download passo o nome da imagem que quero fazer o download e o caminho/nome que esse arquivo terá
id_arquivo = google_drive.search_file_by_name('imagem_02.jpg')
google_drive.download_file(file_id=id_arquivo, file_path='imagem_03.jpg')





