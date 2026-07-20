import pandas as pd

products = pd.read_csv("products.csv")

print(products)

print("\nTotal products:")
print(len(products))