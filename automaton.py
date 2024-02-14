import pyformlang.finite_automaton as automata

# Creamos un autómata finito determinista, llamando la funció de la librería
automat = automata.DeterministicFiniteAutomaton()

# Creamos cuantos estados quereamos
state0 = automata.State(0)
state1 = automata.State(1)
state2 = automata.State(2)

# Agregar estados al DFA
automat.add_start_state(state0)
automat.add_final_state(state0)
automat.add_final_state(state2)

# Agregar transiciones
automat.add_transition(state0, 0, state0)
automat.add_transition(state0, 1, state1)
automat.add_transition(state1, 1, state0)
automat.add_transition(state1, 0, state2)
automat.add_transition(state2, 1, state2)
automat.add_transition(state2, 0, state1)

# Verificar si el autómata acepta una cadena
cadena = input("->")
cadena = [int(i) for i in cadena]  #Crea una lista haciendo que donde está parado se convierta en un entero
print(automat.accepts(cadena)) # True or false

