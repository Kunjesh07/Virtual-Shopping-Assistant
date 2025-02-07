import random


def search_products(query, max_price=None, size=None):
    """Mock function to search for products based on user criteria."""
    products = [
        {"name": "Floral Skirt", "price": 35, "size": "S", "available": True},
        {"name": "Denim Jacket", "price": 80, "size": "M", "available": True},
        {"name": "White Sneakers", "price": 65, "size": "8", "available": False},
    ]
    results = [p for p in products if query.lower() in p["name"].lower() and (max_price is None or p["price"] <= max_price) and (size is None or p["size"] == size)]
    return results

def estimate_shipping(product_name, location, deadline):
    """Mock function to estimate shipping time and cost."""
    return {"product": product_name, "delivery_possible": random.choice([True, False]), "cost": random.randint(5, 15), "arrival_date": deadline}

def check_discount(product_name, code):
    """Mock function to validate and apply discount codes."""
    valid_codes = {"SAVE10": 10, "DISCOUNT5": 5}
    discount = valid_codes.get(code, 0)
    return {"product": product_name, "discount_applied": discount}

def compare_prices(product_name):
    """Mock function to compare prices across different sites."""
    competitors = {"SiteA": 80, "SiteB": 75, "SiteC": 78}
    return competitors

def get_return_policy(site):
    """Mock function to return e-commerce site return policies."""
    policies = {"SiteA": "30-day returns", "SiteB": "No returns on sale items", "SiteC": "Free returns within 14 days"}
    return {"site": site, "return_policy": policies.get(site, "Unknown policy")}


