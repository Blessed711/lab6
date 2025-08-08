# Функція для знаходження всіх входжень рядка beta в рядок alpha
def find_all_occurrences(alpha, beta):
    positions = []  # Список для збереження позицій входжень
    count = 0        # Лічильник кількості входжень
    n, m = len(alpha), len(beta)  # Довжини відповідних рядків

    # Проходимо по всіх можливих позиціях, де beta може початися в alpha
    for i in range(n - m + 1):
        # Якщо підрядок з alpha співпадає з beta — запам'ятовуємо позицію
        if alpha[i:i + m] == beta:
            positions.append(i + 1)  # +1 для переходу до 1-індексації
            count += 1

    # Виводимо кількість знайдених входжень
    print(count)
    # Якщо хоча б одне входження знайдено — виводимо позиції через пробіл
    if count > 0:
        print(" ".join(map(str, positions)))

# Зчитуємо рядки alpha (текст) і beta (зразок)
alpha = input().strip()
beta = input().strip()

# Викликаємо функцію пошуку входжень
find_all_occurrences(alpha, beta)
