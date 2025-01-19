# **GoMarble Review Scraper**

## **Overview**
GoMarble Review Scraper is an API server designed to extract reviews dynamically from e-commerce product pages. The project utilizes **Selenium** for browser automation and integrates various large language models (LLMs) for dynamic CSS selector identification. The solution was intended to handle review scraping, including pagination, across diverse platforms.

---

## **Features and Intent**
- **Dynamic Review Extraction:** Extract reviews by identifying CSS selectors dynamically using LLMs.
- **Pagination Handling:** Automate navigation through review pages for complete data extraction.
- **Standardized API Response:** Structure responses in JSON format for easy integration.

---

## **Current Progress**

### **Backend Implementation**
- A complete Python script (`main.py`) was developed to:
  - Use Selenium for browser automation and webpage interaction.
  - Integrate multiple LLMs (Hugging Face, LLaMA, Gemma, Mistral, Falcon) to dynamically detect CSS selectors.
- Browser testing was successfully implemented for target websites.

### **Testing Results**
- The Selenium integration worked as expected, with the browser successfully navigating to review pages.
- Multiple LLMs were tested to extract dynamic CSS selectors for reviews, but the results were not reliable or accurate enough.

### **Challenges Encountered**
- **LLM Limitations:** The tested LLMs (Hugging Face models, LLaMA, Mistral, Falcon) were unable to identify CSS selectors dynamically with the required accuracy.
- **OpenAI API Key:** The project heavily depended on OpenAI's premium API for more precise CSS selector identification. The lack of access to this key hindered the project's completion.

### **Frontend and Deployment**
- **Frontend:** Frontend development was planned but not implemented due to time constraints and dependency on backend issues.
- **Deployment:** Deployment was not attempted as the backend functionality was incomplete.

---

## **Setup Instructions**

### **Prerequisites**
1. Python 3.7+ installed on your system.
2. Selenium WebDriver (e.g., ChromeDriver) compatible with your Chrome version. [Download here](https://sites.google.com/chromium.org/driver).

### **Steps**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/GoMarbleReviewScraper.git
   cd GoMarbleReviewScraper



## **Effort and Challenges**

- **Selenium Integration:** Successfully implemented Selenium for dynamic webpage handling and navigation.
- **LLM Testing:** Explored multiple large language models (Hugging Face, LLaMA, Gemma, Mistral, Falcon) for dynamic CSS identification. Despite efforts, these models were insufficient for the task.
- **OpenAI API Dependency:** The intended solution required OpenAI’s premium API for reliable dynamic CSS selector identification. The lack of access to this API was the primary blocker in completing the project.
- **Learning and Exploration:** Significant effort was invested in testing and integrating multiple LLMs, understanding their limitations, and debugging browser automation workflows.

---

## **Future Work**

- **OpenAI API Integration:** With access to OpenAI’s premium API, the project could achieve accurate CSS identification and complete functionality.
- **Frontend Development:** Add a user-friendly interface for API interaction and displaying reviews.
- **Deployment:** Package the solution for production and deploy it to a live environment.

---

## **Acknowledgments**

This project reflects significant effort and exploration into leveraging Selenium and LLMs for review scraping. While challenges were encountered, the groundwork for a successful solution has been established.

