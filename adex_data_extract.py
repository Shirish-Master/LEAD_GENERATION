from cryptography.fernet import Fernet
import json
import pyodbc
import os
import pandas as pd

def decrypt_credentials(encrypted_credentials, key):
    f = Fernet(key)
    decrypted_credentials = {key: f.decrypt(encrypted_credentials[key].encode()).decode() for key in encrypted_credentials}
    return decrypted_credentials

def get_client_market_share(tam_Client_list, strfolderpath_ref):
    
    # Establish a connection to the SQL Server database
    server = 'ENTER_SERVER_HERE'
    database = 'ENTER_DATABASE_HERE'
    
    file_path = strfolderpath_ref + 'encrypted_credentials.json'
    print(f"Looking for file at: {os.path.abspath(file_path)}")
    if not os.path.exists(file_path):
        print("File does not exist.")
    else:
        with open(file_path, 'r') as file:
            encrypted_credentials = json.load(file)
    
    # Replace with the actual key you used for encryption (keep this key secure)
    key = b'ENTER_ENCRYPTION_KEY_HERE'
    
    # Decrypt the credentials
    decrypted_credentials = decrypt_credentials(encrypted_credentials, key)
    
    
    username = decrypted_credentials['username']
    password = decrypted_credentials['password']
    
    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()

    
    with open(strfolderpath_ref + 'ADEX_query.sql', 'r') as file:
        query_unique_market_share = file.read()

    
    client_condition = " OR ".join(f"[Client_Name] LIKE '{client}'" for client in tam_Client_list)

    
    modified_query = query_unique_market_share.replace("?", client_condition)
    print(modified_query)
    
    cursor.execute(modified_query)

    
    rows = cursor.fetchall()
    
    columns = [column[0] for column in cursor.description]
    
    data = {column: [] for column in columns}
    
    for row in rows:
        for column, value in zip(columns, row):
            data[column].append(value)
    
    df_client_market_share = pd.DataFrame(data)
    
    cursor.close()
    conn.close()
    return df_client_market_share

def fn_run_ADEX_client_data_main(client_name, current_directory):
        
    strfolderpath_ref = os.path.join(current_directory, 'ADEX_data\\')

    df_Client_name_TAM_mapping = pd.read_excel(strfolderpath_ref + 'Client_name_TAM_mapping.xlsx')
    
    tam_Client_list = df_Client_name_TAM_mapping[df_Client_name_TAM_mapping['Name_of_Group_code_for_Advertiser_Latest'] == client_name]['Tam Client Name'].tolist()
    print(tam_Client_list)
    
    if tam_Client_list is not None and len(tam_Client_list) > 1:
        df_client_market_share = get_client_market_share(tam_Client_list, strfolderpath_ref)
    else:
        print([client_name])
        df_client_market_share = get_client_market_share([client_name], strfolderpath_ref)
    
    if df_client_market_share is not None and not df_client_market_share.empty:    
        return df_client_market_share 
    else:
        return None

