import socket
from urllib.parse import urlparse
import os

def get_ip_from_url(url):
    try:
        # Parse the URL to extract the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname if parsed_url.hostname else url

        # Get the IP address of the hostname
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error: {e}"

def save_ip_to_folder(ip, folder_path, filename="ip_address.txt"):
    try:
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "w") as file:
            file.write(ip)
        print(f"IP address saved to {file_path}")
    except Exception as e:
        print(f"Error saving IP to folder: {e}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    folder = input("Enter the folder path to save the IP: ")
    ip_address = get_ip_from_url(url)
    print(f"The IP address of {url} is: {ip_address}")
    save_ip_to_folder(ip_address, folder)
