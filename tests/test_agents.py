import pytest
from tools.shopify_tools import fetch_shopify_products

def test_fetch_shopify():
    # pytest -s tests/test_agents.py
    result = fetch_shopify_products.run("demo-store.myshopify.com", "test")
    assert isinstance(result, list)
