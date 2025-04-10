import requests

def analyze_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        print(f"Analyzing headers for {url}:\n")
        for key, value in headers.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter URL to analyze: ")
    analyze_headers(url)
