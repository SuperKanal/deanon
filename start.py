import requests
import json

def deanonymize(ip, telegram_username):
    # API endpoint for IP information
    ip_info_url = f"https://ipinfo.io/{ip}"
    
    # API endpoint for Telegram username search
    telegram_search_url = f"https://api.telegram.org/bot<YOUR_BOT_TOKEN>/searchPublicChat?username={telegram_username}"
    
    # Make requests to the API endpoints
    ip_response = requests.get(ip_info_url)
    telegram_response = requests.get(telegram_search_url)
    
    # Parse the responses
    ip_data = json.loads(ip_response.text)
    telegram_data = json.loads(telegram_response.text)
    
    # Extract relevant information
    ip_location = ip_data.get("loc", "Unknown")
    telegram_id = telegram_data.get("result", {}).get("id", "Unknown")
    
    return {
        "IP": ip,
        "Location": ip_location,
        "Telegram ID": telegram_id,
        "Telegram Username": telegram_username
    }

# Example usage
ip = "91.239.160.127"
telegram_username = "johndoe"
result = deanonymize(ip, telegram_username)
print(result)
