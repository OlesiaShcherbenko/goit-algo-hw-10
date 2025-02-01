import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2

# Метод Монте-Карло для обчислення інтеграла
N = 1000000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand < f(x_rand)  # Кількість точок під кривою
integral_mc = (under_curve.sum() / N) * (b - a) * f(b)

# Аналітичний розрахунок за допомогою quad
integral_quad, error = spi.quad(f, a, b)

# Вивід результатів
print(f"Інтеграл методом Монте-Карло: {integral_mc:.6f}")
print(f"Аналітичний інтеграл (quad): {integral_quad:.6f}")
print(f"Абсолютна похибка: {abs(integral_mc - integral_quad):.6f}")

# Візуалізація
x = np.linspace(a, b, 400)
y = f(x)

plt.figure(figsize=(6, 5))
plt.plot(x, y, 'r', linewidth=2)
plt.fill_between(x, y, color='gray', alpha=0.3, label="Область інтегрування")
plt.scatter(x_rand[:1000], y_rand[:1000], color='blue', s=1, alpha=0.2, label="Випадкові точки")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Метод Монте-Карло для обчислення інтегралу")
plt.axvline(a, color='gray', linestyle='--')
plt.axvline(b, color='gray', linestyle='--')
plt.legend()
plt.grid()
plt.show()