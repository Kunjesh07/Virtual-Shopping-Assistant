from tools import search_products, estimate_shipping, check_discount, compare_prices, get_return_policy
def shopping_agent(user_query):
    """Processes user queries and determines which tools to call."""
    response = ""
    
    if "find" in user_query.lower():
        product = "floral skirt" if "skirt" in user_query.lower() else "denim jacket" if "jacket" in user_query.lower() else "unknown product"
        max_price = 40 if "under $40" in user_query.lower() else None
        size = "S" if "size S" in user_query.lower() else None
        results = search_products(product, max_price, size)
        if results:
            response += f"I found {results[0]['name']} for ${results[0]['price']} in size {results[0]['size']}. "
            response += "It is in stock!" if results[0]['available'] else "Unfortunately, it's out of stock."
        else:
            response += "I couldn't find any matching products."
    
    if "arrive by" in user_query.lower():
        product = "White Sneakers"
        shipping_info = estimate_shipping(product, "UserLocation", "Friday")
        if shipping_info["delivery_possible"]:
            response += f" The {shipping_info['product']} can be delivered by {shipping_info['arrival_date']} with a shipping cost of ${shipping_info['cost']}."
        else:
            response += f" Sorry, the {shipping_info['product']} cannot be delivered by your requested date."
    
    if "discount" in user_query.lower() or "promo code" in user_query.lower():
        product = "Floral Skirt"
        discount = check_discount(product, "SAVE10")
        if discount > 0:
            response += f" Great news! A discount of ${discount} has been applied to {product}."
        else:
            response += " Sorry, the promo code is not valid."
    
    if "better deals" in user_query.lower() or "cheaper price" in user_query.lower():
        product = "Denim Jacket"
        prices = compare_prices(product)
        if isinstance(prices, dict) and prices:
            best_site = min(prices, key=prices.get)
            response += f" The best deal for {product} is on {best_site} at ${prices[best_site]}."
        else:
            response += " Sorry, I couldn't find any competitor prices."
    
    if "return" in user_query.lower() or "hassle-free" in user_query.lower():
        site = "SiteB"
        policy = get_return_policy(site)
        response += f" The return policy for {site} is: {policy}."
    
    return response.replace("{", "").replace("}", "").replace("'", "") if response else "Sorry, I couldn't process your request."

# Example Run
if __name__ == "__main__":
    user_queries = [
        "Find a floral skirt under $40 in size S. Is it in stock?",
        "I need white sneakers (size 8) for under $70 that can arrive by Friday.",
        "I found a 'casual denim jacket' at $80 on SiteA. Any better deals?",
        "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free.",
    ]
    
    for query in user_queries:
        print(f"User Query: {query}")
        print(shopping_agent(query))
        print("-" * 50)  # Separator for readability