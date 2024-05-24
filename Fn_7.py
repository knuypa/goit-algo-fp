import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    outcomes = [0] * 11  # Масив для підрахунку кількості кожної суми від 2 до 12

    for _ in range(num_rolls):
        result = roll_dice()
        outcomes[result - 2] += 1

    probabilities = [count / num_rolls * 100 for count in outcomes]
    return probabilities

def main():
    num_rolls = 1000000  # Кількість кидків
    probabilities = monte_carlo_simulation(num_rolls)

    # Аналітичні ймовірності
    analytical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

    # Вивід результатів
    sums = list(range(2, 13))
    print("Сума\tМонте-Карло\tАналітична")
    for i, sum_value in enumerate(sums):
        print(f"{sum_value}\t{probabilities[i]:.2f}%\t\t{analytical_probabilities[i]}%")

    # Побудова графіку
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probabilities, width=0.4, label='Монте-Карло', color='blue', alpha=0.6)
    plt.plot(sums, analytical_probabilities, 'ro-', label='Аналітичні', color='red')

    plt.xlabel('Сума на кубиках')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()