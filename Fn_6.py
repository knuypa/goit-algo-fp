items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо елементи за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, details in sorted_items:
        # Вибираємо страви, поки загальна вартість не перевищує бюджет
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_calories += details['calories']
            total_cost += details['cost']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    # Створюємо двовимірну таблицю dp
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    w = budget
    selected_items = []

    # Знаходимо обрані предмети шляхом зворотного відстеження з таблиці dp
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    return selected_items, total_calories

# Приклад використання
budget = 100
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Результат жадібного алгоритму:")
print("Обрані страви:", greedy_result[0])
print("Загальна калорійність:", greedy_result[1])

print("\nРезультат алгоритму динамічного програмування:")
print("Обрані страви:", dp_result[0])
print("Загальна калорійність:", dp_result[1])