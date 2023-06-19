import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
enAzIncelemeYil = cikolataVeri['Review Date'].value_counts().idxmin()
print(enAzIncelemeYil)

# Review Date'e göre sayıları al ve en az veri olan yılı bul