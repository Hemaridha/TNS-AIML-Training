import pandas as pd

data = {
    "Product Name": ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Accessories"],
    "Price": [50000, 25000, 2000, 1500, 800],
    "Quantity Sold": [10, 30, 60, 45, 80]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Data:")
print(df)

# Product with highest sales
highest_product = df.loc[df["Total Sales"].idxmax()]

print("\nProduct with Highest Sales:")
print(highest_product)

# Average product price
print("\nAverage Product Price:", df["Price"].mean())

# Products with quantity sold > 50
print("\nProducts with Quantity Sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

# Sort based on total sales
print("\nProducts sorted by Total Sales:")
print(df.sort_values("Total Sales", ascending=False))
