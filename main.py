import pandas as pd
answers = []
data = pd.read_csv(r"C:\Users\diede\Downloads\15 bezienswaardigheden - Sheet1.csv")
data = data.fillna(0)
data.columns = ["B","L","T","C","S"]
data = data[:16]
data.sort_values(["C"],inplace=True)
print((data.groupby("C")["T"].mean()))
print((data.groupby("C")["T"].sum()))
list_of_categories = [x for x in data["C"].drop_duplicates()]
for i in list_of_categories:
    a_i = input(f"hou je van {i} answer y/n \n")
    answers.append(a_i)
import numpy as np
import random
for i,j in zip(list_of_categories,answers):
    if j == "y":
       a = data.where(i ==data["C"]).dropna()
       print(a.sample())