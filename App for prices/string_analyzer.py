def find_sequence(text, mode):
    i = 0
    answer = []

    while i < len(text):
        symbol = text[i]
        count = 1

        while i + 1 < len(text) and text[i + 1] == symbol:
            count += 1
            i += 1

        if count > 1:
            sequence = symbol * count
            answer.append((symbol, count, sequence))

        i += 1

    if mode == "Во всех символах":
        return answer

    filtered_answer = []


    for symbol, count, sequence in answer:
        if mode == "Только в буквах" and symbol.isalpha():
            filtered_answer.append((symbol, count, sequence))

        elif mode == "Только в цифрах" and symbol.isdigit():
            filtered_answer.append((symbol, count, sequence))

    return filtered_answer

    # return answer
    # print(answer)

if __name__ == '__main__':
    find_sequence('abccccdddd', 'Только в буквах')
