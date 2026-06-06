def find_divisors(num):
    divs = []

    for i in range(2, num):
        if num % i == 0:
            divs.append(str(i))


    return divs
    # print(divs)

if __name__ == '__main__':
    find_divisors(300)

