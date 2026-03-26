import pandas as pd
file_path  = r"C:\Users\hp\OneDrive\Desktop\e-commerce-analysis.xlsx"


orders = pd.read_excel(file_path,sheet_name="olist_orders_dataset")
products = pd.read_excel(file_path,sheet_name="sheet1")
sellers = pd.read_excel(file_path,sheet_name="sheet2")
category = pd.read_excel(file_path,sheet_name="sheet3")
order_items = pd.read_excel(file_path,sheet_name="sheet4")
payments = pd.read_excel(file_path,sheet_name="sheet5")
reviews = pd.read_excel(file_path,sheet_name="sheet6")
customers = pd.read_excel(file_path,sheet_name="sheet7")

print(orders.shape)
print(order_items.shape)
print(products.shape)

print(orders.columns)