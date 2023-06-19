import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
ortPuanlar = cikolataVeri.groupby('Country of Bean Origin')['Rating'].mean().sort_values(ascending=False)
print(ortPuanlar)