import pandas as pd
df=pd.read_csv("C:/Users/user742/PycharmProjects/pythonProject2/pokeman/pokemon_data.txt")
print(df)
print("************")
print(df.tail(5))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(df.columns)
'''
#import pandas as pd
def_txt=pd.read_csv('pokemon_data.txt',delimiter='\t')
print(def_txt)
print("************")
print(df.iloc[2,5])
print("************")

df_xlsx = pd.read_excel('C:/Users/user742/PycharmProjects/pythonProject2/pokeman/pokemon_data.tx')
print(df_xlsx.head(3))
print("=================================")
print("#################################################")
print(df[['Name','Type 1', 'HP']])
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(df.iloc[0:4])
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for index, row in df.iterrows():
     print(index, row)

     print(index, row['Name'])


print(df.loc[df['Type 1'] == "Grass"])
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(df.iloc[2,1])
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(df.sort_values(['Speed'], ascending=True))
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(df.sort_values(['Type 1', 'Speed'], ascending=[1,0]))
print("````````")
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df)
print("////////////////////////////////////////////////////////////////")
df = df.drop(columns=['Total'])
print(df)
print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df)
print("=======================================================")
cols = list(df.columns)
print(cols)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#print(df["Name", "Type 1"])

 #df = df[cols[0:4] + [cols[-1]]+cols[4:12]]
#print(df)

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df = df.drop(columns=['Total'])
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.to_csv('modified.csv', index=False)

df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')
print("/////////////////////////////////////////////////////")
print(df['Type 1'] == 'Grass')
print("***********************")
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

print(new_df)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#new_df.reset_index(drop=True, inplace=True)

#new_df.to_csv('filtered.csv')
print("-------------------------------------------------------------------------------")
df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']

print(df)

df = pd.read_csv('modified.csv')
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")

df = pd.read_csv('modified.csv')

df['count'] = 1

df.groupby(['Type 1', 'Type 2']).count()['count']
print(df)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
new_df = pd.DataFrame(columns=df.columns)
#
'''
for df in pd.read_csv('modified.csv', chunksize=3):
     results = df.groupby(['Type 1']).count()

     new_df = pd.concat([new_df, results])