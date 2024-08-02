import pandas as pd
import requests
import openai
import os

def chat_with_openai(prompt, model_selected, strfolderpath_ref):
    # Open the file containing the API key
    with open(strfolderpath_ref + 'api_key.txt', 'r') as file:
        chatgpt_api_key = file.read().strip()  
    
    # OpenAI API endpoint
    URL = "https://api.openai.com/v1/chat/completions"
    
    
    payload = {
        "model": model_selected,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "top_p": 1.0,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }
    
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {chatgpt_api_key}"  # Bearer token for authorization
    }
    
    
    retries = 2
    for attempt in range(retries):
        try:
            response = requests.post(URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                getfun = response.json()['choices'][0]['message']['content']
                return getfun
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} - Error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None

    print("Max retries exceeded")
    return None


def run_get_client_Data(prompt, client_name, model_name, API_selector, columns, strfolderpath_ref):
    preprompt = "For the company name:" + client_name
    
    if API_selector == 'OpenAI':
        getfun = chat_with_openai(preprompt + prompt, model_name, strfolderpath_ref)
    
    
    getfun_cleaned = getfun.strip()

    
    getfun_cleaned = getfun_cleaned.strip('{').strip('}')

    
    key_value_pairs = getfun_cleaned.split(',')

    
    data = {}

    
    for pair in key_value_pairs:
        
        pair_split = pair.split(':', 1)

        
        if len(pair_split) == 2:
            key, value = pair_split
            
            key = key.strip().strip('"\'')
            value = value.strip().strip('"\'')

            
            if key in columns:
                
                data[key] = value

    
    df_res = pd.DataFrame([data])
    
    return df_res   


def get_client_Data_main(client_name, current_directory):
    # Define the folder path reference
    strfolderpath_ref = os.path.join(current_directory, 'GPT_API_Extract\\')

    # Define the prompt for the API request
    prompt = (
        " : I want following mentioned details and result should only in pandas dictionary "
        "City:, Company Name:, Industry:, Founded in Year:, Founder by:, Key Person:, About:, Location:, Base Location:,"
        "Category:, Branch:, Employees Count:, Corporate Office:, Latest Funding news:, CEO:, Platform:, Latest news on Milestone Achieved:"
        "Brief:, Key Competitors:, Market Capitalization (INR Crore):, Revenue (INR Crore):, Corporate Office:, Vertical:"
        "Do not provide any explanation, comments or remarks."
    )
    
    # Define API and model settings
    API_selector = 'OpenAI'
    model_name = 'gpt-3.5-turbo'
    
    # Initialize an empty DataFrame with all possible columns
    columns = [
        "City", "Company Name", "Industry", "Founded in Year", "Founder by", "Key Person",
        "About", "Location", "Base Location", "Category", "Branch", "Employees Count",
        "Corporate Office", "Latest Funding news", "CEO", "Platform",
        "Latest news on Milestone Achieved:Brief", "Key Competitors",
        "Market CapitalizationINR Crore)", "Revenue (INR Crore)", "Vertical"
    ]
    
    # Get the client data
    df_result = run_get_client_Data(prompt, client_name, model_name, API_selector, columns, strfolderpath_ref)

    return df_result
