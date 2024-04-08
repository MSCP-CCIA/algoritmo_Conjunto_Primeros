primeros = {}
def calcular_primeros(gramatica):
  for no_terminal in gramatica.keys():
      print(no_terminal)
      calcular_primeros_recursivo(no_terminal)
  return primeros
def calcular_primeros_recursivo(no_terminal):
  primeros[no_terminal]=set()
  for produccion in gramatica[no_terminal]:
      primer_simbolo = produccion[0]
      if primer_simbolo.islower() or primer_simbolo == 'ε':
          primeros[no_terminal].add(primer_simbolo)
          return primeros[no_terminal]
          print(primeros)
      elif primer_simbolo in gramatica.keys():
          primeros[no_terminal].update(calcular_primeros_recursivo(primer_simbolo))
  return primeros[no_terminal]
gramatica = {
    'S': ['Aa', 'b'],
    'A': ['ε','c'],
    'C': ['D','f','p'],
    'D': ['S','g']
}
primeros = calcular_primeros(gramatica)
print("Conjunto de primeros:")
for no_terminal, conjunto_primeros in primeros.items():
    print(f"{no_terminal}: {conjunto_primeros}")
