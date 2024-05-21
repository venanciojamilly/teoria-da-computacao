from automata.tm.mntm import MNTM
from util.util import mntm_configurations
from src.Q04 import mntm4

# Exemplo de uso da MNTM
cadeia4 = "ab#aaabaaaaaa"

if (all(n in mntm4.input_symbols for n in cadeia4)) and cadeia4.count('#')==1:
  gen4 = mntm4.read_input_stepwise(cadeia4)
  conf = mntm_configurations(gen4)
  print("Configurações: ")
  for c in conf:
    print(c)
else:
  print("Cadeia inválida")