# src/processor.py

def flatten_products(raw_products: list[dict], store_name: str) -> list[dict]:
    """
    Takes raw product dicts (each with nested 'variants') and flattens
    them into one flat dict per variant, tagged with which store it came from.
    """
    flat_records = []
    
    for product in raw_products:
        product_id = product.get("id")
        product_title = product.get("title","unknown")
        product_type = product.get("product_type","unknown")
        vendor = product.get("vendor","unknown")

        
        for variant in product["variants"]:
            raw_price = variant.get("price")
            record = {
                "store": store_name,
                "product_id": product_id,
                "product_title": product_title,
                "product_type": product_type,
                "vendor": vendor,
                "variant_id": variant.get("id"),
                "variant_title": variant.get("title",None),
               
                "price": float(raw_price) if raw_price is not None else 0.0,
                "sku": variant.get("sku",None),
                "availability": variant.get("available",None),
                "option1": variant.get("option1",None),
                "option2": variant.get("option2",None),
                "option3": variant.get("option3",None),
                
            }
            flat_records.append(record)
            
            
    
    return flat_records