import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
menseiSayilar = cikolataVeri['Country of Bean Origin'].value_counts()
print(menseiSayilar)