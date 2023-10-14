import pandas as pd

names = ["Maria", "Adam", "Peter", "Vanessa", "Hanna"]

titled_columns = {"Name": names,
                  "Height": [166, 187, 175, 168, 160],
                  "Wight": [56, 85, 70, 63, 60]
                  }
                  
data = pd.DataFrame(titled_columns)
print(data)