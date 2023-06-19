import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
menseiUlkeOrtalama = cikolataVeri.groupby('Country of Bean Origin')['Rating'].mean().sort_values(ascending=False)
print(menseiUlkeOrtalama)

# Bar menşeine göre grupla
# Rating ortalamasını al