import pandas as pd
import numpy as np

pokemon = pd.read_csv("pokemon.csv")
print(pokemon)

print(pokemon.iloc[0]) # Prints the first pokemon)

print(pokemon[["Name", "HP"]]) # Prints oyt name and HP

# Two different ways to print out info about "Bulbasaur"
pmon = pokemon.set_index("Name", drop=False)
print(pmon.loc["Bulbasaur"])
print(pmon.iloc[0])

# Slicing
print(pmon.iloc[0:3])
print(pmon.loc["Bulbasaur":"Charizard"][["Name", "HP"]]) 

# Adds a ne column called "SpeedAttackRatio"
pokemon["SpeedAttackRatio"] = pokemon["Speed"] / pokemon["Attack"]
#print(pokemon)

# Deletes a column permanently
pokemon = pokemon.drop(columns=["SpeedAttackRatio"])
print(pokemon)

print(pokemon["Type 1"].unique()) # Prints all the unique types
print(pokemon["Type 1"].value_counts()) # Prints all the types and how many there are of each
print(pokemon["Type 1"].value_counts(normalize=True)) # Prints the procentage of each type
print(pokemon[["Type 1", "Type 2"]].value_counts()) # Prints all the combinations
print(pokemon[["Type 1", "Type 2"]].value_counts().head(5)) # Prints the 5 most common combinations
print(pokemon[["Type 1", "Type 2"]].value_counts().tail(5)) # Prints the 5 rearest combinations