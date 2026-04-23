import pandas as pd
import numpy as np
import random
import os

def generate_inventory_data(n=500):
    products = [
        ("Braiding Hair", "Hair"),
        ("Edge Control", "Styling"),
        ("Hair Gel", "Styling"),
        ("Shampoo", "Care"),
        ("Conditioner", "Care"),
        ("Hair Oil", "Care")
    ]

    data = []

    for i in range(n):
        product_id = i
        product_name, category = random.choice(products)

        price = round(random.uniform(5, 50), 2)

        stock_level = random.randint(10, 200)

        # Demand varies by product
        base_demand = {
            "Braiding Hair": random.randint(5, 15),
            "Edge Control": random.randint(3, 10),
            "Hair Gel": random.randint(3, 8),
            "Shampoo": random.randint(2, 6),
            "Conditioner": random.randint(2, 6),
            "Hair Oil": random.randint(1, 5)
        }

        daily_demand = base_demand[product_name]

        # Weekend effect
        is_weekend = random.choice([0, 1])
        if is_weekend:
            daily_demand += random.randint(1, 5)

        # Units sold depends on stock + demand
        units_sold = min(stock_level, daily_demand + random.randint(-2, 3))

        supplier_lead_time = random.randint(2, 7)

        # Reorder logic
        reorder_point = daily_demand * supplier_lead_time

        restocked = 1 if stock_level < reorder_point else 0

        data.append([
            product_id,
            product_name,
            category,
            price,
            stock_level,
            daily_demand,
            supplier_lead_time,
            reorder_point,
            is_weekend,
            units_sold,
            restocked
        ])

    columns = [
        "product_id", "product_name", "category", "price",
        "stock_level", "daily_demand", "supplier_lead_time",
        "reorder_point", "is_weekend", "units_sold", "restocked"
    ]

    df = pd.DataFrame(data, columns=columns)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/inventory_data.csv", index=False)

    print("Inventory dataset created!")

if __name__ == "__main__":
    generate_inventory_data()