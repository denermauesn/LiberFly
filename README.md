# LiberFly
Desafio Liberfly

bibliotecas usadas:
- pandas
- requests

Post():
    recebe um Dict, e envia por POST para o endereço da api

read_file():
    recebe o caminho de um arquivo .xlsx e faz a leitura para um DataFrame pandas

insert_data():
    itera sobre as linhas do dataframe e submete os registros com a função Post()