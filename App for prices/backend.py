def calculate_price(start_price: float, amount: int, discount: float):

    price = start_price * amount
    off_price = price * discount / 100
    final_price = price - off_price

    return final_price


if __name__ == '__main__':
    start_price = float(input('Цена товара: '))
    amount = int(input('Количество: '))
    discount = float(input('Скидка (%): '))

    result = calculate_price(start_price, amount, discount)

    print(result)