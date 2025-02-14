import requests

url = "https://www.w3schools.com/"  # Replace with your target URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text  # Get the HTML content
    print(html_content)
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
