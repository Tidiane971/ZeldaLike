class FSM:
    def __init__(self, initial_state, transitions):
        self.state = initial_state
        self.transitions = transitions

    def send_input(self, input_symbol):
        # Vérifie si une transition existe pour le couple (état_courant, symbole)
        if (self.state, input_symbol) in self.transitions:
            self.state = self.transitions[(self.state, input_symbol)]

    def get_state(self):
        return self.state
