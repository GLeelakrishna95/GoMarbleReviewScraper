from fastapi import FastAPI, Query
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import json

# FastAPI app
app = FastAPI()

# Set your Gemini API key here
# GEMINI_API_KEY = "AIzaSyB7WVETwnbjdqDHkc5xbp8qhQ8BIILg6H8"

def identify_css_selectors_with_mistral(html: str) -> dict:
    """
    Use Mistral-7B via LM Studio to identify CSS selectors for reviews dynamically.
    """
    LM_STUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"

    # Prepare the prompt
    prompt = f"""
    You are an expert in web scraping. Analyze the following HTML content and identify the CSS selectors for:
    1. Review container
    2. Review title
    3. Review body
    4. Review rating
    5. Review author
    6. Next page button for pagination

    Return the result in this exact JSON format:
    {{
      "review_container": "...",
      "title": "...",
      "body": "...",
      "rating": "...",
      "reviewer": "...",
      "next_page": "..."
    }}

    HTML content:
    {html[:4000]}  # Truncate to avoid exceeding token limits
    """

    # Prepare the payload
    payload = {
        "model": "llama-2-7b-chat",  # Use the model you loaded in LM Studio
        "messages": [{"role": "user", "content": prompt}]
    }

    # Send the request to LM Studio
    response = requests.post(LM_STUDIO_API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()["choices"][0]["message"]["content"]
        try:
            # Clean the response to remove invalid escape sequences
            clean_result = result.replace("\\_", "_")  # Replace escaped underscores
            return json.loads(clean_result)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON response after cleaning: {clean_result}")
    else:
        raise Exception(f"Error from LM Studio API: {response.status_code} - {response.text}")


@app.get("/api/reviews")
def get_reviews(url: str = Query(...)):
    """
    Extract reviews from a given product page URL using Selenium and Gemini.
    """
    # Initialize the Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    reviews = []
    try:
        # Load the page
        driver.get(url)
        driver.implicitly_wait(10)
        page_html = driver.page_source

        # Use Gemini to identify CSS selectors
        selectors = identify_css_selectors_with_mistral(page_html)

        # Extract reviews
        while True:
            review_elements = driver.find_elements(By.CSS_SELECTOR, selectors["review_container"])
            for review in review_elements:
                title = review.find_element(By.CSS_SELECTOR, selectors["title"]).text
                body = review.find_element(By.CSS_SELECTOR, selectors["body"]).text
                rating = review.find_element(By.CSS_SELECTOR, selectors["rating"]).text
                reviewer = review.find_element(By.CSS_SELECTOR, selectors["reviewer"]).text
                reviews.append({
                    "title": title,
                    "body": body,
                    "rating": int(rating.split()[0]),
                    "reviewer": reviewer
                })
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, selectors["next_page"])
                next_button.click()
                driver.implicitly_wait(10)
            except:
                break
    finally:
        driver.quit()

    return {"reviews_count": len(reviews), "reviews": reviews}
