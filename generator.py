from google import genai
import os 
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

def generate_blog(topic): 
    prompt = f""" 
    Generate a structured blog using using the topic given
    Topic:  {topic}
    The blog should be creative and related to topic itself.
        """
    try:            
        response = client.models.generate_content(       
                model="gemini-2.5-flash",       
                contents=prompt
           )  
        return response.text
    except Exception as e:
        print("Invalid")
        print(e)
    return "Failed to generate blog."
 
