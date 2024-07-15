import requests
import re

def validate_ip(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    return re.match(pattern, ip) is not None

def get_ip_info(ip):
    if not validate_ip(ip):
        return "Invalid IP address format. Please enter a valid IPv4 address."

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,query")
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'success':
            return f"IP: {data['query']}\nCountry: {data['country']}\nRegion: {data['regionName']}\nCity: {data['city']}\nZIP: {data['zip']}\nLatitude: {data['lat']}\nLongitude: {data['lon']}\nTimezone: {data['timezone']}\nISP: {data['isp']}\nOrganization: {data['org']}\nAS: {data['as']}"
        else:
            return f"Error: {data['message']}"
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to connect to the API. Please check your internet connection."

# Example usage
ip = input("Enter an IP address: ")
info = get_ip_info(ip)
print(info)
