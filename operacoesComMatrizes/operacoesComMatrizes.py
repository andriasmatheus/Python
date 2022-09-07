def menu():
  print("*----- Menu -----*")
  print("Escolha a operação:")
  opcao = int(input("1 - Adição de Matrizes;\n2 - Matriz transposta;\n3 - Determinante da matriz.\nEntrada: "))

  if(opcao == 1):
    adicaoDeMatrizes()
  elif(opcao == 2):
    matrizTransposta()
  elif(opcao == 3):
    determinanteDaMatriz()
  else:
    print("Entrada inválida. Retornando ao menu...\n")
    menu()

def adicaoDeMatrizes():
  print("\nADIÇÃO DE MATRIZES:")
  numLinha = int(input("Digite o número de linhas da matriz A: "))
  numColuna = int(input("Digite o número de colunas da matriz A: "))
  numLinhaN = int(input("Digite o número de linhas  da matriz B: "))
  numColunaN = int(input("Digite o número de colunas da matriz B: "))
  if(numLinhaN >= 1 and numColunaN >= 1 and numLinhaN == numLinha and numColunaN == numColuna):
    matrizM = []
    linha = []

    for l in range(numLinha):
      linha = []
      for k in range(numColuna):
        linha.append(float(input("Digite o elemento %d %d da matriz A: " %(l+1, k+1))))
      matrizM.append(linha)
  
    matrizN = []
    linha2 = []
  
    for li in range(numLinhaN):
      linha2 = []
      for ko in range(numColunaN):
          linha2.append(float(input("Digite o elemento %d %d da matriz B: " %(li+1, ko+1))))
      matrizN.append(linha2)
  

    linhaResultante = []
    matrizResultante = []
    for i in range(numLinha):
      linhaResultante = []
      for k in range(numColuna):
        linhaResultante.append(matrizN[i][k] + matrizM[i][k])
      matrizResultante.append(linhaResultante)

    print("\nMatriz resultante:\n")
    for i in range(len(matrizResultante)):
      for k in range(len(matrizResultante[0])):
        print("%.1f " %matrizResultante[i][k], end="")
      print("")
    print("Retornando ao menu...\n")
    menu()
  else:
    print("Matrizes Incompatíveis.")
    print("Retornando ao menu...\n")
    menu()

def matrizTransposta():
  print("\nMATRIZ TRANSPOSTA\n")
  linha = int(input("Digite o número de linhas  da matriz: "))
  coluna = int(input("Digite o número de colunas da matriz: "))
  matriz = []
  matrizTransposta = []
  for l in range(linha):
      linhaV = []
      for k in range(coluna):
          linhaV.append(float(input("Digite o elemento %d %d da matriz: " %((l+1),(k+1)))))
      matriz.append(linhaV)
      
  print("\nMATRIZ:")
  for l in range(len(matriz)):
      for k in range(len(matriz[l])):
          print("%.1f " %(matriz[l][k]), end = "")
      print("")
  print("")    

  elementosColuna = []
  matrizTransposta = []
  for k in range(coluna):
    elementosColuna = []
    for l in range(len(matriz)):
      elementosColuna.append(matriz[l][k])
    matrizTransposta.append(elementosColuna)

  print("MATRIZ TRANSPOSTA:\n")

  for t in range(len(matrizTransposta)):
    for j in range(len(matrizTransposta[t])):
      print("%.1f " %(matrizTransposta[t][j]), end = "")
    print("")

  print("Retornando ao menu...\n")
  menu()

def determinanteDaMatriz():
  print("\nDETERMINANTE\n")
  matriz = []
  ordem = int(input("Digite a ordem da matriz (até ordem 3): "))
  if(ordem == 1):
    matriz.append(float(input("Digite o elemento 1 1 da matriz: ")))
    print("\nDeterminante:  %.1f" %matriz[0])
  elif(ordem == 2):
    linha = []
    for l in range(2):
        linha = []
        for k in range(2):
            linha.append(float(input("Digite o elemento %d %d da matriz: " %((l+1), (k+1)))))
        matriz.append(linha)
    determinante = (-(matriz[0][1]*matriz[1][0])+(matriz[0][0]*matriz[1][1]))
    print("\nDeterminante: %.1f" %determinante)
  elif(ordem == 3):
      for l in range(3):
          linha = []
          for k in range(3):
              linha.append(float(input("Digite o elemento %d %d da matriz: " %((l+1), (k+1)))))
          matriz.append(linha)
      determinante = (((matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[0][1]*matriz[1][2]*matriz[2][0])+(matriz[0][2]*matriz[1][0]*matriz[2][1]))-((matriz[0][2]*matriz[1][1]*matriz[2][0])+(matriz[0][0]*matriz[1][2]*matriz[2][1])+(matriz[0][1]*matriz[1][0]*matriz[2][2])))
      print("\nDeterminante: %.1f" %determinante) 
  print("Retornando ao menu...\n")
  menu()

menu()