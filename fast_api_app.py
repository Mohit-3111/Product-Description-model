from input_output_pydantic_classes import ProductDescriptionInput, ProductDescriptionTotalOutput
from fastapi import FastAPI, HTTPException
from api_call import generate_product_description

app = FastAPI()

@app.post("/generate-description/")
async def generate_description(input_data: ProductDescriptionInput):
    try:
        result = generate_product_description(input_data)
        return result.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))