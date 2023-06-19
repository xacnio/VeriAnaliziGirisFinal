import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
enCokIncelemeYil = cikolataVeri['Review Date'].value_counts().idxmax()
print(enCokIncelemeYil)

# Review Date'e göre sayıları al ve en çok veri olan yılı bul