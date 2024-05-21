from automata.tm.dtm import DTM
from util.util import dtm_configurations
from src.Q01 import dtm1

#   Exemplo de uso da DTM
cadeia1 = 'AAaBB'

if (all(n in dtm1.input_symbols for n in cadeia1)):
  gen1 = dtm1.read_input_stepwise(cadeia1)
  state1, output1, configurations1 = dtm_configurations(gen1)
  print(f"Estado final: {state1}")
  print(f"Saída: {output1}")
  print("Configurações: ")
  for c in configurations1:
    print(f" {c}")
else:
  print("Cadeia inválida")