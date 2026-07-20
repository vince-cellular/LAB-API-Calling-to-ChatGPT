# API Calling to ChatGPT Lab

## Student
- Name: Vincent de Paul NZOTEGOUONG
- Course: Ironhack AI Engineering Bootcamp

---

## Project Overview

This project demonstrates how to use the OpenAI ChatGPT Vision API to automatically generate professional e-commerce product listings from product images and metadata.

The application:
- Reads product information from a CSV file
- Encodes product images into Base64
- Sends images and prompts to the OpenAI Vision API
- Receives structured JSON responses
- Saves generated listings to a JSON file

---

## Technologies Used

- Python
- OpenAI API
- GPT-4o Mini
- Pandas
- python-dotenv
- Base64
- JSON

---

## Project Structure

```
LAB-API-Calling-to-ChatGPT/
│
├── product_listing_generator.py
├── products.csv
├── generated_listings.json
├── product_images/
├── test_api.py
├── test_image.py
├── test_prompt.py
├── vision_api_test.py
├── README.md
└── .env (not included)
```

---

## How the API Integration Works

The application securely loads the OpenAI API key from a `.env` file. Product images are converted into Base64 format before being sent to the OpenAI Vision API together with a carefully designed prompt containing the product name, price, and category.

The API analyzes the image and returns a structured JSON response containing:
- Product title
- Product description
- Key features
- SEO keywords

The generated listings are saved into `generated_listings.json`.

---

## Challenges Faced

During development I encountered several challenges:
- Setting up the Python virtual environment.
- Loading images correctly from the project folder.
- Fixing Python indentation errors.
- Formatting prompts for the Vision API.
- Parsing JSON responses returned by the API.

Each issue was resolved through debugging, restructuring the code, and testing each component individually.

---

## Quality of Generated Listings

The generated listings include:
- SEO-friendly product titles
- Detailed product descriptions
- Product features
- Relevant keywords

The AI successfully combines the supplied metadata with details observed in the product images.

---

## Possible Improvements

Future improvements could include:
- Processing larger product datasets
- Multiple image analysis
- Cost tracking
- Retry logic for API failures
- Exporting directly to e-commerce platforms
- A simple web interface for users

---

## Results

The application successfully:
- Connected to the OpenAI API
- Encoded product images
- Generated listings for three products
- Saved results in JSON format
- Implemented basic error handling

---

## Author

Vincent de Paul NZOTEGOUONG