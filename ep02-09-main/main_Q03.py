from automata.tm.mntm import MNTM
from util.util import mntm_configurations
from src.Q03 import mntm3

# Exemplo de uso da MNTM
cadeia3 = 'a+bb+ab+a'

if (all(n in mntm3.input_symbols for n in cadeia3)):
  gen3 = mntm3.read_input_stepwise(cadeia3)
  conf = mntm_configurations(gen3)
  print("Configurações: ")
  for c in conf:
    print(c)
else:
  print("Cadeia inválida")