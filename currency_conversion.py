def currency_conversion(currency, amount):
    # Add your code here

    if amount.replace('.', '', 1).isdigit():
        if currency == "usd":
            return float(amount) * 4075
        elif currency == "yuan":
            return float(amount) * 575
        elif currency == "baht":
            return float(amount) * 115
        else:
            return "not found"
    else:
        return "invalid amount"
    
    # Reminders: 
    # - currency is a string that tells us what currency to change to. It can be 'usd', 'yuan', or 'baht'.
    # - amount is a number that tells us how much money to change into riel.
    
    # 1. add a check to ensure that 'amount' is a number.
    # 2. convert the 'amount' to the right 'currency'.
