import pandas as pd
import os

# pandas concat funtion to concat multiple csv files

master1 = pd.DataFrame()

list = [i for i in os.listdir("Sales_Data")]

for i in list:
    df = pd.read_csv(f"Sales_Data/{i}")
    master1 = pd.concat([master1, df])

master1.to_csv("master1.csv", index=False)    

# pandas append function to append csv files -- work same as concat

master2 = pd.DataFrame()


for i in list:
    df = pd.read_csv(f"Sales_Data/{i}")
    
    master2 = master2.append(df)
    
master2.to_csv("master2.csv", index=False)