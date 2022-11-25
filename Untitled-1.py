import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('movies.csv')


quantile = df['vote_count'].quantile(0.75)
print(quantile)
result = df[df['vote_count'] > quantile].sort_values('vote_average',ascending=False).head(10)
print(result)



df['release_date'] = pd.to_datetime(df['release_date'])


df["year"] = df.release_date.dt.year

zx=df.groupby("year").agg({"revenue": np.mean, "budget": np.mean})
chart=zx.loc['2010-01-01':'2017-12-31', ['revenue', 'budget']]
print(zx)
        

z=np.arange(3)

def million(x, pos):
        return '{:2.1f}M'.format(z*1e-6)

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(df['release_date'],chart['budget'],label='budget',color = 'red')
axes.bar (df['release_date'],chart['revenue'],label='revenue')
axes.legend(loc=(1.05,0.9))
axes.set_title('Średni przychód i budżet filmu w latach 2010-2016')
formatter = plt.FuncFormatter(million)
axes.yaxis.set_major_formatter(formatter)
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

runtime.plot(kind='bar')
plt.show() 
