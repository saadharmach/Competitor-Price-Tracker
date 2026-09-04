import requests
import time




def fetch_all_products(store_domain: str, delay: float = 1.0) -> list[dict]:
    all_products = []
    page = 1
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
}
    
    while True:
        try:
            url = f"{store_domain}/products.json?page={page}&limit=250"
            response = requests.get(url, headers=headers, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching products from {store_domain}: {e}")
            break
        if response.status_code != 200:
            break
        products = response.json().get("products", [])
        if not products:
            break
        all_products.extend(products)
        page += 1
        time.sleep(delay)
    return all_products


    
