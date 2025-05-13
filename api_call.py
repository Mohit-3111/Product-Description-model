from openai import OpenAI, APIError, AuthenticationError, RateLimitError
import os
from dotenv import load_dotenv
from prompt import short_product_description_promt
from input_output_pydantic_classes import ProductDescriptionInput, ProductDescriptionTotalOutput, LLMOutput
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is not set in the environment variables.")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_product_description(input_data: ProductDescriptionInput) -> ProductDescriptionTotalOutput:

    try:
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": short_product_description_promt},
                {"role": "user", "content": str(input_data.model_dump())}],
            response_format = LLMOutput,
            temperature=0.7 # Adjust temperature for creativity
        )
        llm_output = response.choices[0].message.content

        output = ProductDescriptionTotalOutput(
            input=input_data,
            output=json.loads(llm_output)
        )

        return output

    except AuthenticationError:
        raise RuntimeError("Authentication Error: Invalid API Key.")
    except RateLimitError:
        raise RuntimeError("Rate limit exceeded. Please try again later.")
    except Exception as e:
        raise RuntimeError(f"Unexpected Error: {e}")
