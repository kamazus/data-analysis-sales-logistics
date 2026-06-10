import pandas as pd

df = pd.read_excel('data/ecommerce_sales.xlsx')
print("Названия колонок в файле:")
print(df.columns.tolist())
print("\nПервые 3 строки данных:")
print(df.head(3))

print(len(df))
print(df.duplicated().sum())
df = df.drop_duplicates()
print(len(df))

df.columns = df.columns.str.lower()
df['date'] = pd.to_datetime(df['date'])
df['couponcode'] = df['couponcode'].fillna('No Coupon')

df['totalprice'] = df['quantity'] * df['unitprice']
df_sales = df[['orderid', 'date', 'customerid', 'product', 'quantity', 'unitprice', 'totalprice', 'couponcode', 'referralsource', 'paymentmethod']]
df_logistics = df[['orderid', 'shippingaddress', 'orderstatus', 'trackingnumber','itemsincart']]

df_sales.to_csv('data/clean_sales.csv', index=False)
df_logistics.to_csv('data/clean_logistics.csv', index=False)