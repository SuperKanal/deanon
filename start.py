import requests
import re

def deanon():
    choice = input("Enter 'phone' to search for phone number or 'ip' to search for IP: ")
    
    if choice.lower() == 'phone':
        phone_number = input("Enter the phone number: ")
        search_phone(phone_number)
    elif choice.lower() == 'ip':
        ip_address = input("Enter the IP address: ")
        search_ip(ip_address)
    else:
        print("Invalid choice. Please enter 'phone' or 'ip'.")

def search_phone(phone_number):
    # Perform a search for the phone number on the internet
    search_url = f"https://www.google.com/search?q={phone_number}"
    response = requests.get(search_url)
    html = response.text
    
    # Find possible IP addresses in the search results
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    possible_ips = re.findall(ip_pattern, html)
    
    print("Possible IP addresses found:")
    for ip in possible_ips:
        print(ip)
    
    # Perform a whois lookup for the phone number
    whois_url = f"https://whois.com/whois/{phone_number}"
    response = requests.get(whois_url)
    html = response.text
    
    # Extract relevant information from the whois lookup
    whois_info = extract_whois_info(html)
    print("\nWhois information:")
    for key, value in whois_info.items():
        print(f"{key}: {value}")

def search_ip(ip_address):
    # Perform a search for the IP address on the internet
    search_url = f"https://www.google.com/search?q={ip_address}"
    response = requests.get(search_url)
    html = response.text
    
    # Find possible phone numbers in the search results
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    possible_phones = re.findall(phone_pattern, html)
    
    print("Possible phone numbers found:")
    for phone in possible_phones:
        print(phone)
    
    # Perform a whois lookup for the IP address
    whois_url = f"https://whois.com/whois/{ip_address}"
    response = requests.get(whois_url)
    html = response.text
    
    # Extract relevant information from the whois lookup
    whois_info = extract_whois_info(html)
    print("\nWhois information:")
    for key, value in whois_info.items():
        print(f"{key}: {value}")

def extract_whois_info(html):
    # Extract relevant information from the whois lookup HTML
    whois_info = {}
    
    # Extract the registrar information
    registrar_pattern = r'Registrar:</b>(.*?)<br>'
    registrar_match = re.search(registrar_pattern, html, re.DOTALL)
    if registrar_match:
        whois_info['Registrar'] = registrar_match.group(1).strip()
    
    # Extract the registration date
    registration_date_pattern = r'Registered On:</b>(.*?)<br>'
    registration_date_match = re.search(registration_date_pattern, html, re.DOTALL)
    if registration_date_match:
        whois_info['Registration Date'] = registration_date_match.group(1).strip()
    
    # Extract the expiration date
    expiration_date_pattern = r'Expiration Date:</b>(.*?)<br>'
    expiration_date_match = re.search(expiration_date_pattern, html, re.DOTALL)
    if expiration_date_match:
        whois_info['Expiration Date'] = expiration_date_match.group(1).strip()
    
    # Extract the name servers
    name_servers_pattern = r'Name Server:</b>(.*?)<br>'
    name_servers_match = re.search(name_servers_pattern, html, re.DOTALL)
    if name_servers_match:
        whois_info['Name Servers'] = name_servers_match.group(1).strip()
    
    # Extract the contact information
    contact_info_pattern = r'Contact:</b>(.*?)<br>'
    contact_info_match = re.search(contact_info_pattern, html, re.DOTALL)
    if contact_info_match:
        whois_info['Contact'] = contact_info_match.group(1).strip()
    
    return whois_info

# Run the script
deanon()
