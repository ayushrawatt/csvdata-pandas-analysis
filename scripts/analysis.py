import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")

df["date"] = pd.to_datetime(df["date"])

df["revenue"] = df["price"] * df["quantity"]

top_products = df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(10)
top_products = top_products.reset_index()

city_sales = df.groupby("city")["revenue"].sum().sort_values(ascending=False).reset_index()

category_sales = df.groupby("category")["revenue"].sum().reset_index()

with pd.ExcelWriter("ecommerce_analysis_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    top_products.to_excel(writer, sheet_name="Top Products", index=False)
    city_sales.to_excel(writer, sheet_name="City Sales", index=False)
    category_sales.to_excel(writer, sheet_name="Category Revenue", index=False)