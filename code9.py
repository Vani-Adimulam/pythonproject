import pandas as pd
c=pd.read_excel("C:\\worksheet\\employee.xlsx")
df=pd.DataFrame(c)
print(df)
print()
print("After sorting a spread sheet:")
print()
print(df.sort_values("Years_of_experience",ascending=False))
