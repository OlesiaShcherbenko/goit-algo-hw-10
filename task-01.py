from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="drink-production", sense=LpMaximize)

# Змінні (кількість виробленого лимонаду та фруктового соку)
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Обмеження ресурсів
model += (2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint")
model += (1 * lemonade <= 50, "Sugar Constraint")
model += (1 * lemonade <= 30, "Lemon Juice Constraint")
model += (2 * fruit_juice <= 40, "Fruit Puree Constraint")

# Функція максимізації (загальна кількість напоїв)
model += lemonade + fruit_juice, "Total Production"

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Optimal production: Lemonade = {lemonade.varValue}, Fruit Juice = {fruit_juice.varValue}")