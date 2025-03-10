import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import requests

def download_cert(cert_url, save_path):
    try:
        response = requests.get(cert_url)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Certificate successfully downloaded to {save_path}")
    except requests.RequestException as e:
        print(f"Error downloading the certificate: {e}")

def launch_chrome_with_cert(cert_path):
    if not os.path.exists(cert_path):
        print("Error: The certificate file does not exist. Please check and try again.")
        return
    
    # Default Chrome path
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    
    # Check if Chrome exists, otherwise prompt user
    if not os.path.exists(chrome_path):
        chrome_path = input("Chrome executable not found. Please paste the full path to chrome.exe: ").strip()
        if not os.path.exists(chrome_path):
            print("Error: The Chrome path you provided does not exist. Please check and try again.")
            return
    
    command = [chrome_path, f"--cast-developer-certificate-path={cert_path}"]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to launch Chrome: {e}")

def main():
    cert_url = "https://gist.githubusercontent.com/tchebb/1d34c8a4bd76c93a2c8e2d642768ddb8/raw/f2eb55638c0efb0c0323ecb33d107adbfb8d266b/chromecast-ica-3.pem"
    cert_save_path = os.path.join(os.getenv('TEMP', '/tmp'), "chromecast-ica-3.pem")  # Save to temp folder
    
    # Download the certificate
    download_cert(cert_url, cert_save_path)

    # Use the downloaded certificate with Chrome
    launch_chrome_with_cert(cert_save_path)

if __name__ == "__main__":
    main()
