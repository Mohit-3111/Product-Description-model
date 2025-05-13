# 🛍️ AI-Powered Product Description Generator

**Automatically create short, engaging product descriptions for online stores using LLMs.**

---

## Project Overview

This project showcases how to use a generative AI model (OpenAI GPT-4o-mini) to automatically generate **friendly, persuasive, and SEO-friendly product descriptions** for online stores based on structured input.
It demonstrates prompt engineering, robust input validation with Pydantic, and API integration using **FastAPI** for real-time deployment.

---

## Features

✅ Structured input using `pydantic`
✅ Professionally crafted prompt for high-quality output
✅ GPT-4o-mini model integration via OpenAI API
✅ FastAPI endpoint for deployment
✅ Error handling for common OpenAI API issues
✅ Easily customizable for different product categories or tone of voice

---

## Input Example

```json
{
  "product_name": "Eco-Friendly Water Bottle",
  "target_audience": "Health-conscious adults",
  "keywords": [
    "BPA-free",
    "Keeps drinks cold for 24 hours",
    "Leak-proof design"
  ]
}
```

---

## Output Example
Stay hydrated the smart way with our Eco-Friendly Water Bottle. Designed for health-conscious adults, this BPA-free bottle keeps your drinks cold for up to 24 hours. Its sleek, leak-proof design makes it perfect for workouts, commutes, or your desk. Upgrade your hydration game today!

---

## Tech Stack
Python 3.10+

FastAPI

OpenAI GPT-4o-mini (via OpenAI SDK)

Pydantic for input/output modeling

---

## How It Works

**1. User Input:** Structured product info is passed (via script or API).
**2. Prompting:** A custom-crafted prompt guides the LLM’s output.
**3. OpenAI API:** GPT-4o-mini generates a short, compelling product description.
**4. Output:** Returned as a structured JSON object (for easy rendering on frontends).

---

## Getting Started

**1. Set Your API Key**
In .env file, add your openAI API key
```console
OPENAI_API_KEY=your_openai_key_here
```

**2. Run the CLI Version**
```console
python main.py
```

**3. Run the FastAPI App**
```console
uvicorn fast_api_app:app --reload
```
Then navigate to:
http://127.0.0.1:8000/docs#/default/generate_description_generate_description__post for interactive Swagger UI

---

## File Structure
````console
.
├── main.py                            # Script-based usage
├── fast_api_app.py                    # FastAPI app
├── api_call.py                        # Handles OpenAI API calls
├── prompt.py                          # Prompt template
├── input_output_pydantic_classes.py   # Input/output schema definitions
├── .env                               # API key config
```