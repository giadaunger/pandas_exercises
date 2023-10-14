import pandas as pd

names = ["Maria", "Adam", "Peter", "Vanessa", "Hanna"]
titeld_column = {"Name": names}
data = pd.DataFrame(titeld_column)
print(data)