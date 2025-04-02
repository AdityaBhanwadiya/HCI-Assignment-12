import os
from dotenv import load_dotenv

# Load environment variables from a .env file
# This allows sensitive information like API keys to be stored securely
load_dotenv()

class Config:
    # Retrieve the Azure OpenAI API key from the environment variables
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    
    # Retrieve the Azure OpenAI endpoint URL from the environment variables
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    
    # Retrieve the deployment name for the Azure OpenAI model
    AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    
    # Retrieve the model name (e.g., gpt-4) from the environment variables
    AZURE_OPENAI_MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL")
    
    # Retrieve the API version to use with Azure OpenAI
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")