from StackHanoi import Stack

print("\n¡Vamos a jugar a las torres de Hanoi!")

#Crear las pilas
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


#Configurar el juego
num_disks = int(input("¿Con cuántos discos quieres jugar? "))

while num_disks < 3:
    num_disks = int(input("Ingresa un número mayor o igual a 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)  # Cambiado a push


num_optimal_moves = (2 ** num_disks) - 1
print(f"\nLo más rápido que puedes resolver este juego es en {num_optimal_moves} movimientos.")

#Obtener entrada del usuario
def get_input():
    choices = ['L', 'M', 'R']  

    while True:
        
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Escribe {letter} para {name}")

       
        user_input = input("Elige una pila: ").strip().upper()

        
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]
        else:
            print("Entrada no válida. Intenta de nuevo.")


        
#Jugando el juego
