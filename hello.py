print("Hello,GitHub!")import requests

# Replace with the raw URL of your hello.py file from GitHub
url = "https://raw.githubusercontent.com/your-username/Assignment1/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print("Fetched script content:\n")
    print(response.text)
else:
    print(f"Failed to fetch script. Status code: {response.status_code}")

 
