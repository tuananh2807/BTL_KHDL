import pandas as pd

df = pd.read_csv("DuLieu/weather.csv")

print(df.head())

print("\n====================")
print("Tên cột:")
print(df.columns)

print("\n====================")
print("Kích thước dữ liệu:")
print(df.shape)

print("\n====================")
print("Thông tin dữ liệu:")
print(df.info())