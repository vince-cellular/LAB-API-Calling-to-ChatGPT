import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from product_listing_generator import (
    encode_image,
    create_product_listing_prompt
)

# Load API key
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Product information
image_path = "product_images/shoes.jpg"

product_name = "Running Shoes"
price = 120
category = "Shoes"
additional_info = "Comfortable sports shoes"

# Encode image
base64_image = encode_image(image_path)

# Create prompt
prompt = create_product_listing_prompt(
    product_name,
    price,
    category,
    additional_info
)

print("Sending request to OpenAI...")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    temperature=0.7
)

result = response.choices[0].message.content

print("\nGenerated Listing:\n")
print(result)

# Try to save JSON
try:
    listing = json.loads(result)

    with open("generated_listings.json", "w", encoding="utf-8") as f:
        json.dump(listing, f, indent=4)

    print("\n✓ Listing saved to generated_listings.json")

except Exception:
    print("\nThe response was not valid JSON.")