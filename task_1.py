
import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')  # Кількість продукту А
B = pulp.LpVariable('Juice', lowBound=0, cat='Continuous')  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += A + B, "Production"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження для води
model += 1 * A <= 50  # Обмеження для цукру
model += 1 * A <= 30  # Обмеження для лимонного соку
model += 2 * B <= 40  # Обмеження для фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade produced: {A.varValue} units")
print(f"Juice produced: {B.varValue} units")
print(f"Total products produced: {pulp.value(model.objective)} units")