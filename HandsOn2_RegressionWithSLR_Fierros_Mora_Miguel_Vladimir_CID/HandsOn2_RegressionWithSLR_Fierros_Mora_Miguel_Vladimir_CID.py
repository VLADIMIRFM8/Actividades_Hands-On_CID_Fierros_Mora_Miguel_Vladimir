#Hands-On 2_Regression With SLR_Fierros_Mora_Miguel_Vladimir_CID

# Datos de la tabla
X =[23, 26, 30, 34, 43, 48, 52, 57, 58]  # Advertising (Mill. Euro)
Y = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518] # Sales (Mill. Euro)

#Conteo de elementos en el dataset
n = len(X)

print("\t \n\n1- SUMATORIAS: ")

#Sumatorias de los elementos de X e Y
Sum_X = sum(X)
print("Sumatoria de X: ", Sum_X)
Sum_Y = sum (Y) 
print("Sumatoria de Y: ", Sum_Y)

#Sumatoria de XY
sum_XY = sum(X[i] * Y[i] for i in range(n))
print("Sumatoria de SumXY: ", sum_XY)

#Sumatoria de Sum(X^2)
sum_X2 = sum(X[i] ** 2 for i in range(n))
print("Sumatoria de Sum(X^2): ", sum_X2)

print("\n2- MULTIPLICACIONES DE SUMATORIAS: ")
#Sumatoria de SumX * SumY
sum_X_Y = sum(X)*sum(Y)
print("Multiplicación de SumX*SumY: ", sum_X_Y)

#Sumatoria de SumX * SumX
sum_XX = sum(X)*sum(X)
print("Multiplicación de SumX*SumX: ", sum_XX)

#Multiplicación de n por sumatoria de SumXY
N_sumXY = n*sum_XY
print("Multiplicación de n*SumXY: ", N_sumXY)

print("\n3- RESTA DE SUMATORIAS: ")

#Resta de la multiplicación de n por sumatoria de SumXY menos la multiplicación de SumX * SumY
#A = n * sumXY - SumXSumY
A = N_sumXY - sum_X_Y
print("Resta de n*SumXY - SumX*SumY: ", A)

#Resta de la multiplicación de n por Sum(X^2) menos la multiplicación de SumX * Sum X
C = (n * sum_X2) - sum_XX
print("Resta de n*Sum(X^2) - SumX*SumX: ", C)

print("\n4- RESULTADOS DE B0 Y B1: ")

# Cálculo de B1
B_0 = ((sum_X2*Sum_Y) - (Sum_X*sum_XY))/C
#print("El valor de B0 es: ", B_0)

# Cálculo de B0
B_1 = (N_sumXY - sum_X_Y) / C
#print("El valor de B1 es: ", B_1)


print(f"B0 (intercepción): {B_0:.2f}")
print(f"B1 (pendiente): {B_1:.2f}\n")

print("\n5- RESULTADOS Y PREDICCIONES: ")


print(f"\nEcuación de regresión obtenida: Ŷ = {B_0:.2f} + {B_1:.2f} * x1")

print("\n6- PREDICCIONES DE VALORES DE ADVERTISING NO CONOCIDOS USANDO B0 Y B1: ")
P1 = B_0 + B_1*25
print(f"\nPredicción #1 con '25' de Advertising: Ŷ = {P1:.2f} Million Euro")
P2 = B_0 + B_1*32
print(f"Predicción #2 con '32' de Advertising: Ŷ = {P2:.2f} Million Euro")
P3 = B_0 + B_1*40
print(f"Predicción #3 con '40' de Advertising: Ŷ = {P3:.2f} Million Euro")
P4 = B_0 + B_1*46
print(f"Predicción #4 con '46' de Advertising: Ŷ = {P4:.2f} Million Euro")
P5 = B_0 + B_1*56
print(f"Predicción #5 con '56' de Advertising: Ŷ = {P5:.2f} Million Euro")

