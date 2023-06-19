import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
sirketSayilar = cikolataVeri.groupby('Company Location')['Company (Manufacturer)'].nunique().sort_values(ascending=False)
print(sirketSayilar)

# Lokasyona göre grupla
# Şirket ismine göre unique değerleri al (şirket sayısını bul)