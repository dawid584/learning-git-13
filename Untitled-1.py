import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('movies.csv')


quantile = df['vote_average'].quantile(0.75)
print(quantile)
result = df[df['vote_average'] > quantile].sort_values('vote_average',ascending=False).head(10)
print(result)



df['release_date'] = pd.to_datetime(df['release_date'])
data=df.groupby(pd.Grouper(key='release_date',freq='Y')).sum()
data=data.loc['2010-01-01':'2016-12-31', ['revenue', 'budget']]


z=np.arange(3)

def million(z, pos):
        return 'USD {:20.1f}MLD'.format(z*1e-9)


x = np.array([2010, 2011, 2012, 2013, 2014, 2015 , 2016])

fig, ax = plt.subplots()


formatter = plt.FuncFormatter(million)
ax.yaxis.set_major_formatter(formatter)
plt.bar(x,data['budget'],label='budget')
plt.plot(x,data['revenue'], color='red',label='revenue') # zmieniamy kolor poprzedniej linii
plt.legend(loc=1)
plt.xlabel('Lata') # dodajemy opis osi X
plt.ylabel('Wartość') # dodajemy opis osi Y
plt.title('Średni przychód i budzet filmów w latach 2010-2016') # dodajemy tytuł wykresu
plt.show()


df_2= pd.read_csv('genres.csv')

data_2= df.groupby(['genre_id','title']).mean()

state_table= pd.merge(df_2 ,data_2, how='left' ,on='genre_id')
print(state_table)

the_most_often = state_table['genres'].value_counts()
print(the_most_often[:1])

runtime = state_table.pivot_table(values = 'runtime', index = 'genres', aggfunc='mean')
runtime.sort_values(by='runtime', ascending=False).round(2)
print(runtime)

runtime['runtime'].hist(bins=30)
plt.show() 
