def main():
    mass = int(input())
    energy = calculate_energy(mass)
    print(energy)

def calculate_energy(mass: int) -> int:
    energy = mass * 300000000 ** 2
    return str(energy)

main()