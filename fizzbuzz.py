class FizzBuzz:
    def convert(self, num: int) -> str:
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        if num % 3 == 0:
            return "Fizz"
        if num % 5 == 0:
            return "Buzz"
        return str(num)


if __name__ == "__main__":
    fizzBuzz = FizzBuzz()
    for num in range(1, 101):
        print(fizzBuzz.convert(num))
