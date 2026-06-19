from google import genai
import os 
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
def summarize_text(text): 
 
    prompt = f"""
    Summarize the following text. 
 
    Rules: 
    - Keep summary under 100 words 
    - Maintain meaning 
    - Remove unnecessary details 
 
    Text: 
    {text} 
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
    return "Failed to generate summary."
 
