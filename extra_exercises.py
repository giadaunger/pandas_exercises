import pandas as pd

# Read file and name it Pokemon
pokemon = pd.read_csv("pokemon.csv")

# Print information about DataFrame
print(pokemon.info())

# Print columns "Name" and "Generation"
print(pokemon[["Name", "Generation"]])

# Print the last Pokemon
print(pokemon.tail(1))

# Name the rows based on the "Name" column with set_index()
name_column = pokemon.set_index("Name")
print(name_column)

# Access the row Charmander
charmander_row = pokemon.loc[pokemon["Name"] == "Charmander"]
print(charmander_row)

# Print all the rows between "Venusaur" and "Charmander"
slice_row = pokemon.loc[(pokemon["Name"] == "Venusaur") & (pokemon["Name"] == "Charmander")]
print(slice_row)

# Add a brand new column called SpeedAttackRatio 
pokemon["SpeedAttackRatio"] = pokemon["Speed"] / pokemon["Attack"]
print(pokemon)

# Delete AttckRatio column
pokemon = pokemon.drop(columns=["SpeedAttackRatio"])
print(pokemon)

# Print the unique types
unique_types = pokemon["Type 1"].unique()
print(unique_types)

# How many pokemon are there for each unique type? Use .value_counts()
how_many_of_each_unique_type = pokemon["Type 1"].value_counts()
print(how_many_of_each_unique_type)

# Display the 10 most common combinations
most_common_combinations = pokemon[["Type 1", "Type 2"]].value_counts().head(10)
print(most_common_combinations)