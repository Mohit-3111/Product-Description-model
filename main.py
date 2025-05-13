from input_output_pydantic_classes import ProductDescriptionInput
from api_call import generate_product_description
import pprint

if __name__ == "__main__":
    
    example_input = ProductDescriptionInput(
        product_name="Eco-Friendly Water Bottle",
        target_audience="Health-conscious adults",
        keywords=["BPA-free", "Keeps drinks cold for 24 hours", "Leak-proof design"],
    )

    result = generate_product_description(example_input)
    pprint.pprint(result.model_dump())
