from typing import List, Tuple

class TuringMachine:
    def __init__(self, 
                 tape: List[str], 
                 states: List[str], 
                 transition_function: List[Tuple[str, str, str, str, str]]) -> None:
        """
        Initialize a Turing machine.

        :param tape: A list representing the initial tape.
        :param states: A list of all possible states.
        :param transition_function: A list of tuples (current state, read symbol, next state, write symbol, move direction).
        """
        self.tape = tape
        self.states = states
        self.transition_function_dict = { (s, r): (n, w, m) for s, r, n, w, m in transition_function}
        self.current_state = states[0]
        self.head_position = 0
        self.halted = False

    def __repr__(self) -> str:
        """
        Represent the Turing machine's current state for debugging purposes.
        """
        tape_str = ''.join(self.tape)
        head_str = ' ' * self.head_position + '^'
        return f"Tape: {tape_str}\nHead: {head_str}\nState: {self.current_state}"

    def step(self) -> None:
        """
        Execute one step of the Turing machine based on the transition function.
        """
        if self.halted:
            return

        # Read the symbol at the current head position
        read_symbol = self.tape[self.head_position]
        
        # Get the transition for the current state and read symbol
        transition = self.transition_function_dict.get((self.current_state, read_symbol))

        if transition is None:
            # No transition defined for the current state and read symbol (Halting)
            self.halted = True
        else:
            # Unpack the transition
            next_state, write_symbol, move_direction = transition

            # Write the new symbol to the tape
            self.tape[self.head_position] = write_symbol

            # Move the head in the specified direction
            if move_direction == 'R':
                self.head_position += 1
                if self.head_position == len(self.tape):
                    self.tape.append(' ')
            elif move_direction == 'L':
                if self.head_position == 0:
                    self.tape.insert(0, ' ')
                else:
                    self.head_position -= 1

            # Update the current state
            self.current_state = next_state

    def run(self) -> None:
        """
        Run the Turing machine until it reaches a halting state.
        """
        while not self.halted:
            self.step()
