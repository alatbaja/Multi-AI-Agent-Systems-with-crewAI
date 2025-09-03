from crewai_tools import tool
import requests

@tool("shopify_products")
def fetch_shopify_products(store_name: str, token: str) -> list:
    """Fetch last 10 products from Shopify store"""
    url = f"https://{store_name}/admin/api/2024-04/products.json?limit=10"
    headers = {"X-Shopify-Access-Token": token}
    res = requests.get(url, headers=headers)
    return res.json()["products"]
