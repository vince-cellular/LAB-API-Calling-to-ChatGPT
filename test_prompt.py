from product_listing_generator import create_product_listing_prompt


prompt = create_product_listing_prompt(
    "Running Shoes",
    120,
    "Shoes",
    "Comfortable sports shoes"
)

print(prompt)