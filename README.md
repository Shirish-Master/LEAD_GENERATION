# Project Name

## Overview

This project utilizes the OpenAI API to extract company data and connect to a SQL Server database for data manipulation.

## Setup Instructions

1. **Clone the Repository:**

2. **Install Required Packages:**

3. **Add Sensitive Information:**
- **API Key:** Create a file named `api_key.txt` in the `GPT_API_Extract` directory and add your OpenAI API key.
- **Database Credentials:** Create `encrypted_credentials.json` in the reference directory with the following format:
```json
{
    "username": "your_encrypted_username",
    "password": "your_encrypted_password"
}
```
## Excel Sheets

- **Client_name_TAM_mapping.xlsx:** Contains columns for `Name_of_Group_code_for_Advertiser_Latest` and `Tam Client Name`.
- **df__addx__result.xlsx:** Used for storing results related to ADDEX.
- **df__bw__client__action__data.xlsx:** Used for storing data related to BW.

## Usage

Run the main script to start extracting data.

## Notes

- Keep sensitive information secure and do not share publicly.
- Ensure the directory structure is maintained for the project to work correctly.

## License

-This version includes mentions of the two additional Excel sheets and maintains a simple and clear format. Adjust any specific details as necessary.

