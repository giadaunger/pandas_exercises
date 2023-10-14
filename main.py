import pandas as pd

names = ["Maria", "Adam", "Peter", "Vanessa", "Hanna"]

titled_columns = {"Name": names,
                  "Height": [166, 187, 175, 168, 160],
                  "Weight": [56, 85, 70, 63, 60]
                  }

data = pd.DataFrame(titled_columns)


# Printing information from the DataFrame
select_column = data["Weight"] # Selecting a specific (by column)
select_column = data["Weight"][2] # Selecting a specific persons weight (by column)
select_row = data.iloc[1] # Selecting a specific (by row)
select_row = data.iloc[1]["Height"] # Selecting a specific persons height (by row)
# print(select_row)