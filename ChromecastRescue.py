import subprocess
import os
import tkinter as tk
from tkinter import filedialog

def launch_chrome_with_cert(cert_path):
    if not os.path.exists(cert_path):
        print("Error: The file path you provided does not exist. Please check and try again.")
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
    # Tkinter GUI for file dialog
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    cert_path = filedialog.askopenfilename(title="Select Chromecast Certificate File", filetypes=[("PEM Files", "*.pem")])
    
    if cert_path:
        launch_chrome_with_cert(cert_path)
    else:
        print("No file selected. Exiting.")

if __name__ == "__main__":
    main()
