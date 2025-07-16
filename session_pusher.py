from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from urllib.parse import urlparse
import argparse

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def restore_session(driver, session_file: str, target_url: str):
    with open(session_file, encoding='utf-8') as f:
        session_data = json.load(f)

    parsed_url = urlparse(target_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
    driver.get(base_url)

    for cookie in session_data["cookies"]:
        if 'sameSite' in cookie and cookie['sameSite'] is None:
            del cookie['sameSite']
        if 'expiry' in cookie and not isinstance(cookie['expiry'], int):
            del cookie['expiry']
        if 'domain' in cookie and cookie['domain'].startswith('.'):
            cookie['domain'] = cookie['domain'][1:]
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Помилка додавання cookie: {cookie.get('name')} - {e}")

    driver.execute_script("""
        let data = arguments[0];
        for (let key in data) {
            localStorage.setItem(key, data[key]);
        }
    """, session_data["localStorage"])

    driver.execute_script("""
        let data = arguments[0];
        for (let key in data) {
            sessionStorage.setItem(key, data[key]);
        }
    """, session_data["sessionStorage"])

    driver.get(target_url)

parser = argparse.ArgumentParser(description="session pusher")
parser.add_argument("--url", "-u", type=str, required=True, help="URL to push all cached data")
parser.add_argument("--cach", "-c", required=True, type=str, help="Path to cach (.json)")
args = parser.parse_args()

if not args.url or not args.cach:
    pass
else:
    restore_session(driver, args.url, args.cach)

input("Session pushed, press Enter to exit...")
driver.quit()
