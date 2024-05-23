
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначаємо символи
x = sp.symbols('x')

# Визначаємо функцію
func = 2 * (4 / (1.2 * sp.sqrt(2 * sp.pi)) * sp.exp(-0.5 * ((x - 11) / 1.2) ** 2) + 
            7 / (2.4 * sp.sqrt(2 * sp.pi)) * sp.exp(-0.5 * ((x - 15) / 2.4) ** 2))

# Перетворюємо функцію у lambda вираз для обчислення значень
f = sp.lambdify(x, func, 'numpy')

# Межі інтегрування
a = 10
b = 20

# Кількість випадкових точок
N = 100000

# Генеруємо N випадкових точок на інтервалі [a, b]
x_random = np.random.uniform(a, b, N)
# Обчислюємо значення функції в цих точках
f_values = f(x_random)
# Обчислюємо середнє значення функції
mean_f = np.mean(f_values)
# Обчислюємо наближене значення інтегралу
monte_carlo_integral = (b - a) * mean_f
# Обчислення інтегралу за допомогою функції quad
quad_integral, quad_error = spi.quad(f, a, b)
# Виводимо результати
print(f"Наближене значення інтегралу: {monte_carlo_integral}")
print(f"Середнє значення функції: {mean_f}")
print(f"Кількість випадкових точок: {N}")
print(f"Інтеграл: {quad_integral}")
print(f"Оцінка помилки: {quad_error}")
# Створення діапазону значень для x
x = np.linspace(8, 22, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b, 1000)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) на інтервалі [' + str(a) + ', ' + str(b) + ']')
plt.grid()
plt.show()

