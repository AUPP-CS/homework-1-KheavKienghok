from currency_conversion import currency_conversion

# Print a welcome message and list of valid currencies
print("╔════════════════════════════════════════════════════════════════════════════╗")
print("║              Welcome to the AUPP Currency Conversion to RIEL APP           ║")
print("║----------------------------------------------------------------------------║")
print("║                                                                            ║")
print("║                            Instructions:                                   ║")
print("║                                                                            ║")
print("║    1. Enter the currency you want to convert from. (USD $, YUAN ¥, BAHT ฿) ║")
print("║    2. Enter the ammount you want to convert.                               ║")
print("║    3. The ammount will be converted to RIEL (៛).                           ║")
print("║                                                                            ║")
print("╚════════════════════════════════════════════════════════════════════════════╝")
print("\n")

# Ask the user for the currency they want to conusvert from
currency_store = input("Enter the currency: ").lower()

# Ask the user for the amount they want to convert
currency_amount = input("Enter the amount  : ")

# Call the currency_conversion function with the user's currency and amount
result = currency_conversion(currency_store, currency_amount)

riel_cambodia = "\u17DB"
print("\n╔════════════════════════════════════════════════════════════════════════════╗")
print("║                                                                            ║")
print(f"║           Your total in RIEL៛ after conversion is:   {result:<15}       ║")
print("║                                                                            ║")
print("╚════════════════════════════════════════════════════════════════════════════╝")