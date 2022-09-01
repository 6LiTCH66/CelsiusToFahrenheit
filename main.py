
def celsiusToFahrenheit(celsius):
    try:
        fahrenheit = (int(celsius) * 9/5) + 32 # °F = (°C × 9/5) + 32
        print("Temperature in F =", fahrenheit)
        return True
    except ValueError:
        print("Invalid input!\nTry again!")
        return False
        

def main():
    while True:
        celsius = input("Temperature in C = ")
        if celsiusToFahrenheit(celsius):
            break

if __name__ == "__main__":
    main()

