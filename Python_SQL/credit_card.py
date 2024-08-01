def validate_credit_card(card_number):

    if not 13 <= len(card_number) <= 16:
        return "Invalid"

    if (card_number.startswith('4') and len(card_number) == 13) or \
       (card_number.startswith('5') and len(card_number) == 13) or \
       (card_number.startswith('37') and len(card_number) == 16) or \
       (card_number.startswith('6') and len(card_number) == 15):
        pass
    else:
        return "Invalid"

    def card_func(card_number):
        total_sum = 0
        reverse_digits = card_number[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total_sum += n

        return total_sum % 10 == 0

    if card_func(card_number):
        return "Valid"
    else:
        return "Invalid"


card_number = input("Enter a credit card number: ")

result = validate_credit_card(card_number)
print(f"The credit card number is {result}.")
