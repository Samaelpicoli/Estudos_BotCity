from botcity.plugins.excel import BotExcelPlugin

#manipulando um arquivo xlsx, instanciando a classe
bot_excel = BotExcelPlugin()

#leitura do arquivo
bot_excel.read('excelPlugin.xlsx')

#remover uma linha
bot_excel.remove_row(2, 'excelPlugin')

#criar uma nova aba na planilha
bot_excel.create_sheet('Teste')
bot_excel.set_active_sheet('Teste')

#adicionar uma linha na nova aba
bot_excel.add_row(['Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste', 'Teste'])

#adicionar uma nova coluna na aba anterior
bot_excel.set_active_sheet('excelPlugin')
bot_excel.add_column('Estudos', 'excelPlugin')

#como remover uma coluna
bot_excel.remove_columns(['A', 'B'], 'excelPlugin')

#como escrever em apenas uma célula
bot_excel.set_cell('B', 8, value='Olá')

#gerar um novo arquivo que salvará todas as mudanças
bot_excel.write('estudos-excel.xlsx')

