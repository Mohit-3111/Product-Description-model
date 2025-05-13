from pydantic import BaseModel, Field
from typing import List

class ProductDescriptionInput(BaseModel):
    product_name: str = Field(..., description="Name of the product", example="Eco-Friendly Water Bottle")
    target_audience: str = Field(..., description="Target audience for the product", example="Health-conscious adults")
    keywords: List[str] = Field(..., description="List of key product features", example=["BPA-free", "Keeps drinks cold for 24 hours", "Leak-proof design"])

class LLMOutput(BaseModel):
    short_product_description: str = Field(..., description="Short product description based on the input data following the guidelines.")

class ProductDescriptionTotalOutput(BaseModel):
    input: ProductDescriptionInput
    output: LLMOutput
