from product_listing_generator import encode_image


image = encode_image(
    "product_images/shoes.jpg"
)


print("Image encoded successfully!")

print("Encoded length:")
print(len(image))

print("First characters:")
print(image[:50])