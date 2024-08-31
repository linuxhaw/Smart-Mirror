import google.generativeai as genai
import PIL.Image
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import os

GOOGLE_API_KEY = "AIzaSyAPemI2H57SQCuw_LjN4yGba0dE_JAwC3g"

os.environ["GOOGLE_API_KEY"] = "AIzaSyAPemI2H57SQCuw_LjN4yGba0dE_JAwC3g"
genai.configure(api_key=GOOGLE_API_KEY)

folder_path = "./Dataset/Dress"
results = {}

# List of valid image extensions
valid_image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]

for image in os.listdir(folder_path):
    # Filter out non-image files based on file extension
    if not any(image.lower().endswith(ext) for ext in valid_image_extensions):
        continue  # Skip non-image files

    image_path = os.path.join(folder_path, image)
    try:
        img = PIL.Image.open(image_path)

        model = genai.GenerativeModel('gemini-1.5-flash-001')

        prompt = """ 
            Analyze the suitability of this outfit for different types of events, considering the following categories: Blouse, Cardigan, Dress, Heels, Jacket, Long Skirt, Shirt, Short Skirt, Slippers, Sneakers, Style Pants, and Top.

            Classify the outfit into one or more of these categories: Blouse, Cardigan, Dress, Heels, Jacket, Long Skirt, Shirt, Short Skirt, Slippers, Sneakers, Style Pants, and Top.
            List the types of events this outfit would be appropriate for, based on its classification.
            Provide reasons why this outfit is suitable for each event listed.
            [Outfit Classification]
            [Suitable Events]
            [Reason for Each Event]
        """

        contents = [img, prompt]
        response = model.generate_content(contents)

        # Correct way to access the text from response
        if hasattr(response, 'parts'):  # Check if response has 'parts' attribute
            results[image_path] = "\n".join(part.text for part in response.parts if hasattr(part, 'text'))  # Extract text safely

    except PIL.UnidentifiedImageError:
        print(f"Cannot identify image file {image_path}. Skipping.")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0, max_tokens=None, timeout=None, max_retries=2)

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
            
            ... (rest of the prompt remains unchanged)
            """
        ),
        MessagesPlaceholder(variable_name="descriptions"),
        MessagesPlaceholder(variable_name="user_input")
    ]
)

descriptions = formatted_descriptions
user_input = "I have to go to the party, can you give me a recommendation?"

chain = prompt | llm | StrOutputParser()

response = chain.invoke(
    {
        "descriptions": [HumanMessage(content=descriptions)],
        "user_input": [HumanMessage(content=user_input)]
    },
)

print(response)