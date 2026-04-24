# p138-s-digitos.py
# Dado un n entero, sr sus dígitos individuales

def sd(n: int) -> int:
    s = 0
    while n != 0:
        digito = n % 10
        s = s + digito
        n = n // 10
    return s

def main() -> None:
    n = int(input("Introduce un número entero: "))
    r = sd(n)
    print(f"La suma de los dígitos de {n} es {r}")

if __name__ == "__main__":
    print('\033[H\033[J')
    main()