import requests
import json

def deanonymize(ip, telegram_username):
    # API endpoint for IP information
    ip_info_url = f"https://ipinfo.io/{ip}"
    
    # API endpoint for Telegram username search
    telegram_search_url = f"https://api.telegram.org/bot<YOUR_BOT_TOKEN>/searchPublicChat?username={telegram_username}"
    
    # API endpoint for passport information search
    passport_search_url = f"https://api.example.com/passport?number={passport_number}"
    
    # API endpoint for phone number information search
    phone_search_url = f"https://api.example.com/phone?number={phone_number}"
    
    # Make requests to the API endpoints
    ip_response = requests.get(ip_info_url)
    telegram_response = requests.get(telegram_search_url)
    passport_response = requests.get(passport_search_url)
    phone_response = requests.get(phone_search_url)
    
    # Parse the responses
    ip_data = json.loads(ip_response.text)
    telegram_data = json.loads(telegram_response.text)
    passport_data = json.loads(passport_response.text)
    phone_data = json.loads(phone_response.text)
    
    # Extract relevant information
    ip_location = ip_data.get("loc", "Unknown")
    telegram_id = telegram_data.get("result", {}).get("id", "Unknown")
    passport_info = passport_data.get("passport", {})
    phone_info = phone_data.get("phone", {})
    
    # Additional information
    city = ip_data.get("city", "Unknown")
    name = passport_info.get("name", "Unknown")
    surname = passport_info.get("surname", "Unknown")
    patronymic = passport_info.get("patronymic", "Unknown")
    address = passport_info.get("address", "Unknown")
    phone_number = phone_info.get("number", "Unknown")
    phone_operator = phone_info.get("operator", "Unknown")
    
    return {
        "IP": ip,
        "Location": ip_location,
        "City": city,
        "Telegram ID": telegram_id,
        "Telegram Username": telegram_username,
        "Name": name,
        "Surname": surname,
        "Patronymic": patronymic,
        "Address": address,
        "Phone Number": phone_number,
        "Phone Operator": phone_operator,
        "Passport Number": passport_info.get("number", "Unknown")
    }

# Example usage
ip = "91.239.160.127"
telegram_username = "none"
passport_number = "none"
phone_number = "none"
result = deanonymize(ip, telegram_username, passport_number, phone_number)
print(result)
