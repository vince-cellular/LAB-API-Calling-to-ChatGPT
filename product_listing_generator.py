import os
import json
import base64
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# ==========================
# Load API Key
# ==========================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("API Key Loaded Successfully!")

# ==========================
# Encode Image
# ==========================

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# ==========================
# Prompt Generator
# ==========================

def create_product_listing_prompt(product_name, price, category, additional_info=None):

    prompt = f"""
You are an expert e-commerce copywriter.

Analyze the attached product image and create a professional product listing.

Product Information:
- Product Name: {product_name}
- Price: ${price:.2f}
- Category: {category}
"""

    if additional_info:
        prompt += f"- Additional Information: {additional_info}\n"

    prompt += """

Please create:

1. Product Title
2. Product Description (150-200 words)
3. Five Key Features
4. 10-15 SEO Keywords

Return ONLY valid JSON.

{
    "title":"",
    "description":"",
    "features":[],
    "keywords":""
}
"""

    return prompt


# ==========================
# Load Products
# ==========================

products = pd.read_csv("products.csv")

print(f"\nLoaded {len(products)} products.\n")

generated_listings = []

# ==========================
# Process Products
# ==========================

for index, product in products.iterrows():

    print(f"Processing {product['name']}...")

    try:

        image64 = encode_image(product["image"])

        prompt = create_product_listing_prompt(
            product["name"],
            product["price"],
            product["category"]
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.7,
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
                                "url": f"data:image/jpeg;base64,{image64}"
                            }
                        }
                    ]
                }
            ]
        )

        content = response.choices[0].message.content

        try:
            listing = json.loads(content)

        except json.JSONDecodeError:

            listing = {
                "title": product["name"],
                "description": content,
                "features": [],
                "keywords": ""
            }

        listing["id"] = int(product["id"])
        listing["price"] = float(product["price"])
        listing["category"] = product["category"]

        generated_listings.append(listing)

        print("✓ Success\n")

    except Exception as e:

        print(f"✗ Error: {e}\n")


# ==========================
# Save Results
# ==========================

with open("generated_listings.json", "w", encoding="utf-8") as f:
    json.dump(generated_listings, f, indent=4)

print("=" * 50)
print("FINISHED")
print(f"Generated {len(generated_listings)} listings.")
print("Saved to generated_listings.json")
print("=" * 50)