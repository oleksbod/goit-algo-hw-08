import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Перетворення списку у купу
    heapq.heapify(cable_lengths) 

    total_cost = 0

    while len(cable_lengths) > 1:
        # Отримуємо два найменших кабелі
        first_cable = heapq.heappop(cable_lengths)
        second_cable = heapq.heappop(cable_lengths)
        
        # З'єднуємо їх і додаємо витрати до загальної суми
        connection_cost = first_cable + second_cable
        total_cost += connection_cost

        # Додаємо новий кабель до купи
        heapq.heappush(cable_lengths, connection_cost)
    
    return total_cost

# Приклад використання
cable_lengths = [10, 5, 8, 2, 7]
result = min_cost_to_connect_cables(cable_lengths)
print("Мінімальні витрати на з'єднання кабелів:", result)
