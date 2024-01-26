def currency_conversion(currency, amount):
    # Add your code here
    try:
        amount = float(amount) 
    except ValueError:
        return "invalid amount"
    
    if currency == "usd":
        return amount * 4075
    elif currency == "yuan":
        return amount * 575
    elif currency == "baht":
        return amount * 115
    else:
        return "not found"
    
    # Reminders: 
    # - currency is a string that tells us what currency to change to. It can be 'usd', 'yuan', or 'baht'.
    # - amount is a number that tells us how much money to change into riel.
    
    # 1. add a check to ensure that 'amount' is a number.
    # 2. convert the 'amount' to the right 'currency'.
