

# recebe um número inteiro >= 2.
# devolve a quantidade de números primos que existem entre 2 e n.
def n_primos(n):
    primo = True
    x = 2
    c = 0
    while n != 1:
        while x <= n and primo != False:            
            if x < n and n % x == 0:
                primo = False                 
            if x == n and primo == True:
                c = c + 1
            x = x + 1
        x = 2
        n = n - 1
        primo = True
        if n == 1:
            return c
            
            
            




