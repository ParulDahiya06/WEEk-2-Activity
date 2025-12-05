class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


def main():
    scale = input("Enter the input temperature unit (C/F): ").strip().upper()
    value = float(input(f"Enter temperature value in {scale}: "))

    if scale == "C":
        temp = Temperature(value)
        print(f"{value}°C is {temp.fahrenheit:.2f}°F")
    elif scale == "F":
        temp = Temperature(0)
        temp.fahrenheit = value
        print(f"{value}°F is {temp.celsius:.2f}°C")
    else:
        print("Invalid input unit. Please enter C or F.")


if __name__ == "__main__":
    main()