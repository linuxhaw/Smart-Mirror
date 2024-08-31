import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import os
import requests

GOOGLE_API_KEY = "AIzaSyAPemI2H57SQCuw_LjN4yGba0dE_JAwC3g"

os.environ["GOOGLE_API_KEY"] = "AIzaSyAPemI2H57SQCuw_LjN4yGba0dE_JAwC3g"

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

folder_path = "Dataset/Dress"
# results = {}


def recommender(folder_path):
    results = {}

    for image in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image)

        response = query(image_path)

        results[image_path] = response[0]['generated_text']

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.5, max_tokens=None, timeout=None, max_retries=2)

    descriptions_list = list(results.values())
    file_paths = list(results.keys())

    descriptions_with_paths = [f"{desc} [Path: {path}]" for desc, path in zip(descriptions_list, file_paths)]
    formatted_descriptions = "\n".join(descriptions_with_paths)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a helpful assistant that recommends outfit styles based on the provided descriptions of clothing items.

                You will receive descriptions {descriptions} of outfit images from a few of the following categories: Blouse, Cardigan, Dress, Heels, Jacket, Long Skirt, Shirt, Short Skirt, Slippers, Sneakers, Style Pants, and Top.

                The selected images may come from only 2 or 3 of these categories.

                Your task is to analyze these descriptions and choose the most suitable outfit combinations based on the user's input {user_input}. Each outfit should include a combination of items that create a cohesive and stylish look.

                Additionally, please consider the user's age {age}.

                Outfit Selection Criteria:

                1. Mandatory Items: Each outfit must include:
                - A top (Blouse, Shirt, Top) and a bottom (Style Pants, Long Skirt, Short Skirt) and a pair of shoes (Heels, Slippers).
                - OR a dress (Dress) and a pair of shoes (Heels, Slippers).

                2. Combination Rules:
                - If a Blouse, Shirt, or Top is selected as topwear, it must be paired with either Style Pants, Long Skirt, or Short Skirt as bottomwear, and Heels or Slippers as footwear.
                - If a Dress is selected, there is no need for a bottomwear, but Heels or Slippers must be chosen as footwear.

                3. Additional Items: Optional outerwear like Cardigans or Jackets can be included to complete the outfit.

                Provide the selected outfits with their corresponding file paths in the following format:

                [top or dress path],[bottom path if applicable],[shoes path],[optional: outerwear path]

                Example Output:

                [yellow blouse path],[gray tailored pants path],[black heels path]

                Guidelines for Outfit Selection:

                1. Consider Color Coordination: Choose items that complement each other in color or pattern.
                2. Match Style and Occasion: Ensure the selected outfit is suitable for a specific occasion or style, such as casual, formal, or business.
                3. Balance Proportions: Combine items that create a balanced silhouette.
                4. Incorporate Footwear Appropriately: Shoes must always match the overall style and color of the outfit.
                5. Use Layers and Accessories: Include items like cardigans or jackets to complete outfits when appropriate.

                Remember: outfit combination must include a topwear (or dress), bottomwear (if applicable), and footwear (Heels or Slippers).

                Please just give only file paths. Do not give any additional text responses.

                Please do not give two outfit from same category. For example, two pants, two topwears.
                """
            ),
            MessagesPlaceholder(variable_name="descriptions"),
            MessagesPlaceholder(variable_name="age"),
            MessagesPlaceholder(variable_name="user_input")
        ]
    )

    descriptions = formatted_descriptions

    Age = 24
    user_input = "I will go to my friend's wedding. I want to wear pink dress"

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke(
        {
            "descriptions": [HumanMessage(content=descriptions)],
            "user_input" : [HumanMessage(content=user_input)],
            "age" : [HumanMessage(content=Age)]
        },
    )


    return response
        

for i in recommender(folder_path).split(","):
    print(i)










