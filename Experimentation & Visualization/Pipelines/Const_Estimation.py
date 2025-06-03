def calculate_electricity_bill(month: int, consumption_kwh: float) -> float:
    # Define summer months
    summer_months = {6, 7, 8, 9}

    # Define rates based on month type
    if month in summer_months:
        rates = [
            (330, 2.61),
            (700, 3.66),
            (1500, 4.46),
            (3000, 7.08),
            (float('inf'), 7.43)
        ]
    else:
        rates = [
            (330, 2.18),
            (700, 3.00),
            (1500, 3.45),
            (3000, 5.56),
            (float('inf'), 5.83)
        ]

    # Calculate the bill
    bill = 0.0
    previous_limit = 0

    for limit, rate in rates:
        if consumption_kwh > previous_limit:
            kwh_in_tier = min(consumption_kwh, limit) - previous_limit
            bill += kwh_in_tier * rate
            previous_limit = limit
        else:
            break

    return round(bill, 2)
