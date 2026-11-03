import pandas as pd
import numpy as np
import os

df=pd.read_excel("Dataset for Data Analytics.xlsx")
print(df.head())

df.info()

print("total number of missing values in the dataset:", df.isnull().sum().sum())

df["CouponCode"]=df["CouponCode"].fillna("No Coupon")
print(df.isnull().sum())

print("duplicate rows:", df.duplicated().sum())

print("Duplicate OrderIDs:", df["OrderID"].duplicated().sum())

df = df.drop_duplicates()

df = df.drop_duplicates(subset=["OrderID"])

print("Remaining duplicate rows:", df.duplicated().sum())

print("Remaining duplicate OrderIDs:",
      df["OrderID"].duplicated().sum())

print(df["Date"].dtype)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("Invalid dates:", df["Date"].isnull().sum())

print(df["Date"].dt.strftime("%Y-%m-%d").head())

print(df[["Quantity", "UnitPrice",
          "ItemsInCart", "TotalPrice"]].dtypes)


df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

df["ItemsInCart"] = pd.to_numeric(df["ItemsInCart"], errors="coerce")

df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")


print(df["PaymentMethod"].unique())

print(df["OrderStatus"].unique())

print(df["Product"].unique())

print("Invalid Quantity:", (df["Quantity"] <= 0).sum())

print("Invalid UnitPrice:", (df["UnitPrice"] <= 0).sum())

print("Invalid ItemsInCart:", (df["ItemsInCart"] < 0).sum())


calculated_total = (df["Quantity"] * df["UnitPrice"]).round(2)

mismatches = (calculated_total != df["TotalPrice"].round(2)).sum()

print("TotalPrice mismatches:", mismatches)

os.makedirs("output", exist_ok=True)

output_path = "output/Cleaned_Dataset.xlsx"

df.to_excel(output_path, index=False)

print("Cleaned dataset exported successfully!")