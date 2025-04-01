import pandas as pd

# Define dataset
data = {
    'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
             1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
             2018, 2022],
    'Winner': ['Uruguay', 'Italy', 'Italy', 'Uruguay', 'Germany', 'Brazil', 'Brazil', 'England', 'Brazil', 'Germany',
               'Argentina', 'Italy', 'Argentina', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany',
               'France', 'Argentina'],
    'Runner-Up': ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Hungary', 'Sweden', 'Czechoslovakia', 'Germany', 'Italy', 'Netherlands',
                  'Netherlands', 'Germany', 'Germany', 'Argentina', 'Italy', 'Brazil', 'Germany', 'France', 'Netherlands', 'Argentina',
                  'Croatia', 'France']
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("world_cup_data.csv", index=False)
print("Dataset saved successfully!")
