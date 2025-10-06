import requests
import time
from urllib.parse import quote

class Mail:
    def __init__(self, domains = ["outlook", "gmail_plus", "hotmail", "googlemail"],proxy = ""):
        self.session = requests.Session()
        if proxy != "":
            self.session.proxies = {"http": proxy, "https": proxy}
        self.domains = domains
        self.email = self.__create_mail()
        time.sleep(1)
        code = self.activate_mail()
        if code != 200:
            print(code)
            raise Exception("Could not activate mail")

    def __create_mail(self):
        try:
            # Set headers that a browser would typically send
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/json",
                "Origin": "https://emailmux.com",
                "Referer": "https://emailmux.com/"
            }
            
            response = self.session.post("https://emailmux.com/generate-email", 
                                       json={"domains": self.domains}, 
                                       headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json().get("email")
        except requests.exceptions.RequestException as e:
            print(f"Error creating email: {e}")
            raise

    def get_mails(self):
        try:
            self.activate_mail()
            factored_mail = quote(self.email, safe="")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://emailmux.com/"
            }
            response = self.session.get(f"https://emailmux.com/emails?email={factored_mail}", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting mails: {e}")
            return []

    def activate_mail(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://emailmux.com/",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1"
            }
            factored_mail = quote(self.email, safe="")
            self.session.get("https://emailmux.com/", headers=headers)
            
            url = f"https://emailmux.com/use-email?email={factored_mail}"
            response = self.session.get(url, headers=headers)
            
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Error activating mail: {e}")
            return 500

    def get_mail_adress(self):
        return self.email