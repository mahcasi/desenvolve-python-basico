import random

num_elementos = random.randint(5, 20)
print(num_elementos)

elementos = []
for _ in range(num_elementos):
    elementos.append(random.randint(1, 10))

print(f"Lista de elementos: {elementos}")
print(f"Soma dos valores: {sum(elementos)}")
print(f"Média dos valores: {sum(elementos) / num_elementos:.2f}")