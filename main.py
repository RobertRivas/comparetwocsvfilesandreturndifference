import pandas as pd

mapp_Items = pd.read_csv(r'2021_MAPP_Items_Prices_10.28.20.xlsx - MAPP Item List V1 2021.csv')

woo_commerce_items = pd.read_csv(r'wc-product-export-22-1-2021-1611355516966.csv')

print(mapp_Items.head())
print(woo_commerce_items.SKU)


# df2[~df2.Email.isin(df1.Email)]
# print(woo_commerce_items[~mapp_Items['Part #'].isin(woo_commerce_items.SKU)])

items_not_on_web = mapp_Items.query('SKU not in @woo_commerce_items.SKU')


print(items_not_on_web)

items_not_on_web.to_csv(r'C:\Users\Kim\PycharmProjects\falltech_web_vs_mapp_pricing_comparison\items_not_on_web.csv')