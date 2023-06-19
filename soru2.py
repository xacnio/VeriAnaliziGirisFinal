import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
barSayisi = cikolataVeri.groupby('Company Location')['Specific Bean Origin or Bar Name'].count().sort_values(ascending=False)
print(barSayisi)

# Lokasyona göre grupla
# Bar ismine göre sayıları al (bar sayısını bul)