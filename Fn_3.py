import heapq

def dijkstra(graph, start):
    # Відстані до кожної вершини ініціалізуються як нескінченність
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Відстань до стартової вершини завжди 0
    priority_queue = [(0, start)]  # Піраміда зі стартовою вершиною

    while priority_queue:
        # Вибираємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Цей блок коду оптимізує час обробки від вже відвіданих вершин
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо сусідні вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдено шлях коротший, ніж поточно відомий
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Створення графа
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Запуск алгоритму
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)
print(f"Найкоротші шляхи від вершини {start_vertex}: {shortest_paths}")