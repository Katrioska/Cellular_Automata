# Cellular_Automata
Various cellular automaton tests made with python and pygame.
I started doing these tests inspired by ["Predator and Prey"](https://github.com/Hopson97/CellularAutomaton) and ["Empire"](https://github.com/Hopson97/Empire) by Hopson97

## Test 1:
Rules:
- Each cell has these values inherited from parent's cell or by default values if it's initial cell:
  - Strength
  - Maturity
  - Maxchilds
  - Lifetime
  - ColonyID

- For each step when the simulation run:
  - The Current_lifetime increases by 1.
  - If Current_lifetime >= Lifetime then cell dies.
  - If Current_lifetime >= Maturity then cell reproduces:
    - 50% probability to reproduce in each step
    - If reproduces, Childs values increases by 1.
    - If Childs >= Maxchilds then cells cannot reproduce anymore.
    - For each child, parent's values has a mutation of 10% (Except ColonyID)
    - Only for test reasons: If two cells of the same colony collides, one of them dies.
  - If cell encounter with other cell of different colony.
    - Combat starts, cell with highest strength will win)
