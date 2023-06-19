import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
lesitinliOrtalama = cikolataVeri[cikolataVeri['Ingredients'].str.contains('L', na=False)]['Rating'].mean()
lesitinsizOrtalama = cikolataVeri[~cikolataVeri['Ingredients'].str.contains('L', na=False)]['Rating'].mean()

print("Lesitinli çikolataların ortalama puanı:", lesitinliOrtalama)
print("Lesitinsiz çikolataların ortalama puanı:", lesitinsizOrtalama)