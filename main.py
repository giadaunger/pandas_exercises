import pandas as pd

names = ["Maria", "Adam", "Peter", "Vanessa", "Hanna"]

titled_columns = {"Name": names,
                  "Height": [1.66, 1.87, 1.75, 1.68, 1.60],
                  "Weight": [56, 85, 70, 63, 60]
                  }

data = pd.DataFrame(titled_columns)


# Printing information from the DataFrame
select_column = data["Weight"] # Selecting a specific column
select_column = data["Weight"][2] # Selecting a specific persons weight (by column)
select_row = data.iloc[1] # Selecting a specific row
select_row = data.iloc[1]["Height"] # Selecting a specific persons height (by row)
print(select_row)


# Manipulating DataFrame values
bmi = [] # Creating a new list for BMI values
for i in range(len(data)): # Looping through the data
    bmi_score = data["Weight"][i] / (data["Height"][1] ** 2) # Calculating the BMI score
    bmi.append(bmi_score) # Appening the BMI score to the list

data["BMI"] = bmi # Cretaing a new column to the DataFrame
print(data)


# Save data to file
data.to_csv("bmi.csv", sep="\t")