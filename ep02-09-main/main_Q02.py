from automata.tm.dtm import DTM
from util.util import dtm_configurations
from src.Q02 import dtm2

# Exemplo de uso da DTM
cadeia2 = 'a+bb+ab+a'
if (all(n in dtm2.input_symbols for n in cadeia2)):
  gen2 = dtm2.read_input_stepwise(cadeia2)
  state2, output2, configurations2 = dtm_configurations(gen2)
  print(f"Estado final: {state2}")
  print(f"Saída: {output2}")
  print("Configurações: ")
  for c in configurations2:
    print(f" {c}")
else:
  print("Cadeia inválida")