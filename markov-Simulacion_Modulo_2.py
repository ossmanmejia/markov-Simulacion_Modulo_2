import numpy as np

# Define los estados
states = ["Elegante", "Casual", "Deportiva"]

# Define la matriz de transición
transition_matrix = np.array([
    [0.7, 0.2, 0.1],  # Probabilidades de cambiar desde "Elegante"
    [0.3, 0.4, 0.3],  # Probabilidades de cambiar desde "Casual"
    [0.2, 0.3, 0.5]   # Probabilidades de cambiar desde "Deportiva"
])

# Función para elegir un estado inicial aleatorio


def random_initial_state():
    return np.random.choice([0, 1, 2])

# Función para elegir el siguiente estado basado en el estado actual


def next_state(current_state_index):
    return np.random.choice([0, 1, 2], p=transition_matrix[current_state_index])


# Simular las preferencias para 12 meses
num_months = 12
preference_sequence = []

# Elegir un estado inicial aleatorio
initial_state_index = random_initial_state()
print(f"Estado inicial seleccionado: {states[initial_state_index]}")

current_state_index = initial_state_index

# Crear una matriz para almacenar los datos de preferencias
preference_matrix = np.zeros((num_months, 3))

for month in range(num_months):
    # Codificación one-hot para el estado actual
    preference_matrix[month, current_state_index] = 1
    preference_sequence.append(states[current_state_index])
    current_state_index = next_state(current_state_index)

# Calcular la frecuencia de cada preferencia
elegante_count = preference_sequence.count("Elegante")
casual_count = preference_sequence.count("Casual")
deportiva_count = preference_sequence.count("Deportiva")

elegante_percentage = elegante_count / num_months * 100
casual_percentage = casual_count / num_months * 100
deportiva_percentage = deportiva_count / num_months * 100

print(f"Elegante preference: {elegante_count} ({elegante_percentage:.2f}%)")
print(f"Casual preference: {casual_count} ({casual_percentage:.2f}%)")
print(f"Deportiva preference: {deportiva_count} ({deportiva_percentage:.2f}%)")

# Mostrar la matriz de preferencias
print("\nMatriz de preferencias durante 12 meses:")
print(preference_matrix)
