def get_user_input():
    while True:
        try:
            pizzas_ordered = int(input("How many pizzas ordered? "))
            if pizzas_ordered < 0:
                raise ValueError("Please enter a positive integer!")
            break
        except ValueError:
            print("Please enter a number!")

    while True:
        delivery_required = input("Is delivery required? (Y/N) ").upper()
        if delivery_required in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
        is_tuesday = input("Is it Tuesday? (Y/N) ").upper()
        if is_tuesday in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
        used_app = input("Did the customer use the app? (Y/N) ").upper()
        if used_app in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    return pizzas_ordered, delivery_required, is_tuesday, used_app


def calculate_price(pizzas_ordered, delivery_required, is_tuesday, used_app):
    pizza_price = 12.0
    delivery_charge = 2.5 if delivery_required == 'Y' and pizzas_ordered < 5 else 0.0
    discount_tuesday = 0.5 if is_tuesday == 'Y' else 0.0
    discount_app = 0.25 if used_app == 'Y' else 0.0

    total_price = pizzas_ordered * pizza_price + delivery_charge
    total_price *= (1 - discount_app)  

    total_price -= total_price * discount_tuesday

    return round(total_price, 2)


def main():
    print("BPP Pizza Price Calculator")
    print("--------------------------")

    pizzas_ordered, delivery_required, is_tuesday, used_app = get_user_input()
    total_price = calculate_price(pizzas_ordered, delivery_required, is_tuesday, used_app)

    print("\nTotal Price: £{:.2f}.".format(total_price))


if __name__ == "__main__":
    main()
