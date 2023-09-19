from math import*
var_x = int(input("Введіть значення x: "))
var_sigma = int(input("Введіть значення σ: "))
var_mu = int(input("Введіть значення μ: "))
var_y = (1/var_sigma*sqrt(2*pi))*expm1(-1*(var_x-var_mu)**2/2*var_sigma**2)
print("Значення функції Гауса f(x)= ",var_y)



