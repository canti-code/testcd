import socket
from urllib.parse import urlparse
import os
from twilio.rest import Client

# Function to get the IP from the URL
def get_ip_from_url(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname if parsed_url.hostname else url
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error: {e}"

# Function to send the IP address via SMS
def send_ip_to_sms(ip_address, to_phone_number, from_phone_number, account_sid, auth_token):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"The IP address is: {ip_address}",
            from_=from_phone_number,
            to=to_phone_number
        )
        print(f"IP address sent to {to_phone_number}. SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

if __name__ == "__main__":
    # Collect URL input
    url = input("Enter the URL: ")

    # Get the IP address from the URL
    ip_address = get_ip_from_url(url)
    print(f"The IP address of {url} is: {ip_address}")

    # Twilio details
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    from_phone_number = 'your_twilio_phone_number'
    to_phone_number = input("Enter the phone number to send the IP to: ")

    # Send IP address via SMS
    send_ip_to_sms(ip_address, to_phone_number, from_phone_number, account_sid, auth_token)
