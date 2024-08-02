import os

def generate_html(company):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Company Information</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                background-color: #DED0B6;
                color: black;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                width: 100%;
                max-width: 900px;
                display: flex;
                flex-direction: column;
                padding: 10px;
                box-sizing: border-box;
            }}
            .header {{
                display: flex;
                flex-direction: column;
                align-items: center;
                position: relative;
                margin-bottom: 10px;
            }}
            .header .textbox {{
                position: absolute;
                top: 10px;
                left: 10px;
                width: 100px;
                height: 100px;
                border: 1px solid black;
                padding: 5px;
                box-sizing: border-box;
            }}
            .header .title {{
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                margin-left: 130px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: calc(100% - 130px);
            }}
            .header .subtitle {{
                font-size: 18px;
                font-weight: normal;
                text-align: center;
                margin-left: 130px;
                white-space: normal;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: calc(100% - 130px);
            }}
            .content {{
                display: flex;
                justify-content: space-between;
                margin-top: 10px;
                width: 100%;
            }}
            .column {{
                width: 48%;
            }}
            .info-section {{
                margin-bottom: 10px;
                border-radius: 10px;
                padding: 0;
                box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.4);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
            }}
            .info-section h2 {{
                font-size: 20px;
                margin: 10px;
            }}
            .info-section p {{
                font-size: 16px;
                line-height: 1.5;
                margin: 10px;
            }}
        </style>
        <script>
            function fitText() {{
                const titleElement = document.getElementById('companyTitle');
                const parentElement = titleElement.parentElement;
                let fontSize = 24;

                while (titleElement.scrollWidth > parentElement.clientWidth - 130 && fontSize > 10) {{
                    fontSize--;
                    titleElement.style.fontSize = fontSize + 'px';
                }}
            }}

            window.onload = fitText;
            window.onresize = fitText;
        </script>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="textbox"></div>
                <div class="title" id="companyTitle">{company['Company Name']}</div>
                <br>
                <div class="subtitle" id="companySubtitle">{company['About']}</div>
            </div>
            <div class="content">
                <div class="column">
                    <div class="info-section">
                        <h2>Basic Information:</h2>
                        <p>&#127874;<strong>Founded in:</strong> {company['Founded in Year']}</p>
                        <p>&#9818;<strong>Founder:</strong> {company['Founder by']}</p>
                        <p>&#127775;<strong>Key Person:</strong> {company['Key Person']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Location Details:</h2>
                        <p>&#128205;<strong>City:</strong> {company['City']}</p>
                        <p>&#127971;<strong>Corporate Office:</strong> {company['Corporate Office']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Leadership:</h2>
                        <p>&#128084;<strong>CEO:</strong> {company['CEO']}</p>
                    </div>
                </div>
                <div class="column">
                    <div class="info-section">
                        <h2>Financial Information:</h2>
                        <p>&#128176;<strong>Revenue:</strong> {company['Revenue (INR Crore)']}</p>
                        <p>&#128240;<strong>Latest Funding News:</strong> {company['Latest Funding news']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Company Classification:</h2>
                        <p>&#128187;<strong>Platform:</strong> {company['Platform']}</p>
                        <p>&#x1F3AF;<strong>Vertical:</strong> {company['Vertical']}</p>
                        <p>&#127807;<strong>Number of Branches:</strong> {company['Branch']}</p>
                        <p>&#128101;<strong>Employee Count:</strong> {company['Employees Count']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Competitive Landscape:</h2>
                        <p>&#127942;<strong>Key Competitor:</strong> {company['Key Competitors']}</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_template

def fn_generate_summary_html(company, current_directory):
    html_template = generate_html(company)
    return html_template






























'''
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:56:29 2024

@author: Vijay.Babu
"""
import os

def generate_html(company):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Company Information</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                background-color: #DED0B6;
                color: black;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                width: 100%;
                max-width: 900px;
                display: flex;
                flex-direction: column;
                padding: 10px;
                box-sizing: border-box;
            }}
            .header {{
                display: flex;
                flex-direction: column;
                align-items: center;
                position: relative;
                margin-bottom: 10px;
            }}
            .header .textbox {{
                position: absolute;
                top: 10px;
                left: 10px;
                width: 100px;
                height: 100px;
                border: 1px solid black;
                padding: 5px;
                box-sizing: border-box;
            }}
            .header .title {{
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                margin-left: 130px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: calc(100% - 130px);
            }}
            .header .subtitle {{
                font-size: 18px;
                font-weight: normal;
                text-align: center;
                margin-left: 130px;
                white-space: normal;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: calc(100% - 130px);
            }}
            .content {{
                display: flex;
                justify-content: space-between;
                margin-top: 10px;
                width: 100%;
            }}
            .column {{
                width: 48%;
            }}
            .info-section {{
    margin-bottom: 10px;
    border-radius: 10px;
    padding: 0;
    /* Frosted glass effect */
    background: rgba(255, 255, 255, 0.4); /* Semi-transparent white background */
    backdrop-filter: blur(10px); /* Apply blur effect */
    border: 1px solid rgba(255, 255, 255, 0.2); /* Light border for better visibility */
            }}

            .info-section h2 {{
                font-size: 20px;
                margin: 10px;
            }}
            .info-section p {{
                font-size: 16px;
                line-height: 1.5;
                margin: 10px;
            }}
        </style>
        <script>
            function fitText() {{
                const titleElement = document.getElementById('companyTitle');
                const parentElement = titleElement.parentElement;
                let fontSize = 24;

                while (titleElement.scrollWidth > parentElement.clientWidth - 130 && fontSize > 10) {{
                    fontSize--;
                    titleElement.style.fontSize = fontSize + 'px';
                }}
            }}

            window.onload = fitText;
            window.onresize = fitText;
        </script>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="textbox"></div>
                <div class="title" id="companyTitle">{company['Company Name']}</div>
                <br>
                <div class="subtitle" id="companySubtitle">{company['About']}</div>
            </div>
            <div class="content">
                <div class="column">
                    <div class="info-section">
                        <h2>Basic Information:</h2>
                        <p>&#127874;<strong>Founded in:</strong> {company['Founded in Year']}</p>
                        <p>&#9818;<strong>Founder:</strong> {company['Founder by']}</p>
                        <p>&#127775;<strong>Key Person:</strong> {company['Key Person']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Location Details:</h2>
                        <p>&#128205;<strong>City:</strong> {company['City']}</p>
                        <p>&#127971;<strong>Corporate Office:</strong> {company['Corporate Office']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Leadership:</h2>
                        <p>&#128084;<strong>CEO:</strong> {company['CEO']}</p>
                    </div>
                </div>
                <div class="column">
                    <div class="info-section">
                        <h2>Financial Information:</h2>
                        <p>&#128176;<strong>Revenue:</strong> {company['Revenue (INR Crore)']}</p>
                        <p>&#128240;<strong>Latest Funding News:</strong> {company['Latest Funding news']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Company Classification:</h2>
                        
                        <p>&#128187;<strong>Platform:</strong> {company['Platform']}</p>
                        <p>&#x1F3AF;<strong>Vertical:</strong> {company['Vertical']}</p>
                        
                        <p>&#127807;<strong>Number of Branches:</strong> {company['Branch']}</p>
                        <p>&#128101;<strong>Employee Count:</strong> {company['Employees Count']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Competitive Landscape:</h2>
                        <p>&#127942;<strong>Key Competitor:</strong> {company['Key Competitors']}</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_template

def fn_generate_summary_html(company, current_directory):
    html_template = generate_html(company)
    return html_template

'''
'''















































# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:56:29 2024

@author: Vijay.Babu
"""
import os

def generate_html(company):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Company Information</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                background-color: #DED0B6;
                color: black;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                width: 100%;
                max-width: 900px;
                display: flex;
                flex-direction: column;
                padding: 10px;
                box-sizing: border-box;
            }}
            .header {{
                display: flex;
                flex-direction: column;
                align-items: center;
                position: relative;
                margin-bottom: 10px;
            }}
            .header .textbox {{
                position: absolute;
                top: 10px;
                left: 10px;
                width: 100px;
                height: 100px;
                border: 1px solid black;
                padding: 5px;
                box-sizing: border-box;
            }}
            .header .title {{
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                margin-left: 130px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: calc(100% - 130px);
            }}
            .header .subtitle {{
                font-size: 18px;
                font-weight: normal;
                text-align: center;
                margin-left: 130px;
                white-space: normal;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: calc(100% - 130px);
            }}
            .content {{
                display: flex;
                justify-content: space-between;
                margin-top: 10px;
                width: 100%;
            }}
            .column {{
                width: 48%;
            }}
            .info-section {{
                margin-bottom: 10px;
                background-color: #367d8a;
                border-radius: 10px;
                padding: 0;
            }}
            .info-section h2 {{
                font-size: 20px;
                margin: 10px;
            }}
            .info-section p {{
                font-size: 16px;
                line-height: 1.5;
                margin: 10px;
            }}
        </style>
        <script>
            function fitText() {{
                const titleElement = document.getElementById('companyTitle');
                const parentElement = titleElement.parentElement;
                let fontSize = 24;

                while (titleElement.scrollWidth > parentElement.clientWidth - 130 && fontSize > 10) {{
                    fontSize--;
                    titleElement.style.fontSize = fontSize + 'px';
                }}
            }}

            window.onload = fitText;
            window.onresize = fitText;
        </script>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="textbox"></div>
                <div class="title" id="companyTitle">{company['Company Name']}</div>
                <br>
                <div class="subtitle" id="companySubtitle">{company['About']}</div>
            </div>
            <div class="content">
                <div class="column">
                    <div class="info-section">
                        <h2>Basic Information:</h2>
                        <p>&#127874;<strong>Founded in:</strong> {company['Founded in Year']}</p>
                        <p>&#128100;<strong>Founder:</strong> {company['Founder by']}</p>
                        <p>&#127775;<strong>Key Person:</strong> {company['Key Person']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Location Details:</h2>
                        <p>&#128205;<strong>City:</strong> {company['City']}</p>
                        <p>&#127971;<strong>Corporate Office:</strong> {company['Corporate Office']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Leadership:</h2>
                        <p>&#128084;<strong>CEO:</strong> {company['CEO']}</p>
                    </div>
                </div>
                <div class="column">
                    <div class="info-section">
                        <h2>Financial Information:</h2>
                        <p>&#128176;<strong>Revenue:</strong> {company['Revenue (INR Crore)']}</p>
                        <p>&#128240;<strong>Latest Funding News:</strong> {company['Latest Funding news']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Company Classification:</h2>
                        
                        <p>&#128187;<strong>Platform:</strong> {company['Platform']}</p>
                        <p>&#9881;<strong>Vertical:</strong> {company['Vertical']}</p>
                        
                        <p>&#127807;<strong>Number of Branches:</strong> {company['Branch']}</p>
                        <p>&#128101;<strong>Employee Count:</strong> {company['Employees Count']}</p>
                    </div>
                    <div class="info-section">
                        <h2>Competitive Landscape:</h2>
                        <p>&#9876;<strong>Key Competitor:</strong> {company['Key Competitors']}</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_template

def fn_generate_summary_html(company, current_directory):
    html_template = generate_html(company)
    return html_template

    
'''