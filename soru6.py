import pandas as pd
cikolataVeri = pd.read_csv('veri_set.csv')
mean_ratings = cikolataVeri.groupby('Country of Bean Origin')['Rating'].mean()
std_ratings = cikolataVeri.groupby('Country of Bean Origin')['Rating'].std(0)
min_ratings = cikolataVeri.groupby('Country of Bean Origin')['Rating'].min()
max_ratings = cikolataVeri.groupby('Country of Bean Origin')['Rating'].max()
count_ratings = cikolataVeri.groupby('Country of Bean Origin')['Rating'].count()

result = pd.concat([min_ratings, max_ratings, mean_ratings, std_ratings, count_ratings], axis=1)
result.columns = ['Min Puan', 'Max Puan', 'Ortalama Puan', 'Standart Sapma', 'Bar Sayı']
result = result.sort_values(by='Max Puan', ascending=False)
print("En yüksek puanlı bara sahip ülkeler:")
print(result)
print("En kaliteli bar puan ortalamasına sahip ülkeler:")
result = result.sort_values('Ortalama Puan', ascending=False)
print(result)
print("En kaliteli çikolata kökenleri:")
# Sort: standart sapma en düşük ve ortalama puanı en yüksek olanlar
result = result.sort_values(['Ortalama Puan', 'Standart Sapma'], ascending=[False, True])
print(result)