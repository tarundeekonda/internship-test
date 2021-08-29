import pandas as pd

# Reading main.csv into a data frame
df = pd.read_csv("main.csv")

# Filtering records on the basis of whether country contains the word USA.
df = df[df['COUNTRY'].str.contains('USA')]

# Saving the output as  filteredCountry.csv 
df.to_csv("filteredCountry.csv", index = False)
