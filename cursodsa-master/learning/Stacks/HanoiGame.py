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


#Obtener entrada del usuario


        
#Jugando el juego
