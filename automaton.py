import pyformlang.finite_automaton as automata

# Creating a Deterministic Automaton
automat = automata.DeterministicFiniteAutomaton()

# Creating the amount the states 
state0 = automata.State(0)
state1 = automata.State(1)
state2 = automata.State(2)

# Adding states to the DFA
automat.add_start_state(state0)
automat.add_final_state(state0)
automat.add_final_state(state2)

# Adding transitions
automat.add_transition(state0, 0, state0)
automat.add_transition(state0, 1, state1)
automat.add_transition(state1, 1, state0)
automat.add_transition(state1, 0, state2)
automat.add_transition(state2, 1, state2)
automat.add_transition(state2, 0, state1)

# Input for the user to enter the string
cadena = input("->")
cadena = [int(i) for i in cadena]  # Create a list by making where you stand become an integer
print(automat.accepts(cadena)) # Returns True or false

