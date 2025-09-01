import argparse
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.chrome.service import Service

def save(url: str, output_file: str):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--incognito")
    options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    print(f"Opened: {url}")
    print("Cache is recording... for stop press Enter")
    input()

    current_url = driver.current_url
    cookies = driver.get_cookies()
    local_storage = driver.execute_script("return JSON.stringify(localStorage);")
    session_storage = driver.execute_script("return JSON.stringify(sessionStorage);")

    session_data = {
        "url": current_url,
        "cookies": cookies,
        "localStorage": json.loads(local_storage),
        "sessionStorage": json.loads(session_storage)
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(session_data, f, indent=2, ensure_ascii=False)

        print(f"Cache will saved {output_file}")
    driver.quit()


parser = argparse.ArgumentParser(description="Session recorder (CLI)")
parser.add_argument("--url", type=str, required=True, help="URL for recording session")
parser.add_argument("--out", type=str, help="output .json file")
args = parser.parse_args()

if not args.out:
    domain = urlparse(args.url).netloc.replace('.', '_')
    args.out = f"session_{domain}.json"

save(args.url, args.out)
