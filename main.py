import pandas as pd
import requests



def Post(data):
    url = 'https://desafio.liberfly.com.br/meetings'    
    r = requests.post(url, data)
    return r

def read_file(filename):
    data = pd.read_excel(filename)
    return data

def insert_data(data):
    for index, row in data.iterrows():
        row = row.to_dict()
        r = Post(row)
        print(r.text)   

def show_today():
    r = requests.get('https://desafio.liberfly.com.br/meetings/showtoday')
    return r.text

if __name__ == "__main__" :    
    data = read_file('planilha.xlsx')
    
    insert_data(data)
    print(show_today())
    

    
    