import requests

def cotacao(origem, destino):
    api_key='374741883895b3e271fc7c50b8fdfc237db4f197d03818e6c86c006afec0cb86'
    escolha = '{}-{}'.format(origem,destino)
    url_api = 'http://economia.awesomeapi.com.br/json/last/{}?token={}'.format(escolha,api_key)
    cotacao_atual = requests.get(url_api)
    
    if cotacao_atual.status_code == 200:
        dados = cotacao_atual.json()
        par = origem + destino
        return float(dados[par]['bid'])
    else:
        print('Erro ao acessar a API: ', cotacao_atual.status_code)
     
        return None
            
print('{} Conversor de Moedas(USD-BRL) {}'.format('-'*3, '-'*3))
valor = float(input('Digite um valor: '))
m_origem = input('Digite a moeda de origem (BRL ou USD): ').upper()
m_destino= input('Digite a moeda de destino (BRL ou USD): ').upper()

if m_origem==m_destino:
    print('Moeda de origem e destino são iguais! Valor: {}'.format(valor))
else:
    converter = cotacao(m_origem,m_destino)
    if converter:
        valor_final = valor * converter
        print('{:.2f}{} é igual a {:.2f}{}'.format(valor,m_origem,valor_final,m_destino)) 