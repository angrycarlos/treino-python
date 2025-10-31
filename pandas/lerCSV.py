import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt
from random import uniform

fake =  Faker('pt_BR')
dados = []
for _ in range(20):
    dados.append({
        'Nome: ': fake.name(),
        'Cidade': fake.city(),
        'Data': fake.date_between(start_date='-1y', end_date='today'),
        'Valor pagamento': round(uniform(100,5000), 2)
    })

dados_table = pd.DataFrame(dados)

dados_table.to_csv('VendasFakes.csv', index=False, encoding='utf-8')

graf = pd.read_csv('VendasFakes.csv')

cidades = graf.groupby('Cidade')['Valor pagamento'].sum().sort_values(ascending=False)
top_cidades= cidades.head(7)
plt.figure(figsize=(8,8))

plt.pie(
    top_cidades,
    labels=top_cidades.index,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True

)
plt.title('7 cidades com maior valores de pagamentos')
plt.tight_layout
plt.show()