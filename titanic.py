import pandas as pd

df = pd.read_csv("titanic.csv")

df.info() # Get info about your DataFrame
print(df.shape) # Amount of rows and columns that DataFrame contains
print(df.head()) # Prints the first 5 rows
print(df.head(10)) # Prints the first 5 rows
print(df.tail()) # Prints the last 5 rows


for i in list(df.columns): # Loops through all the columns and prints them
    print(i)
    pass

print(df["Name"]) # Prints out all the names
print(df[["Name", "Age"]]) # Prints out names and ages

mask = df["Age"] == 22
print(df[mask].head()) # Printing the first 5 with age of 22

print((df["Age"] == 22) & (df["Survived"] == 1)) # Prints all the deceased at age 22
print(df[df["Name"].str.contains("Persson")]) # Prints every passenger whos name inculdes Persson
print(df["Name"].sample(5)) # Prints out 5 random names
print(df.sort_values("Fare", ascending=False)[["Name", "Fare"]].head(5)) # Prints out 5 tickes that cost the most