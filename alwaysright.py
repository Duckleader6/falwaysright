import random

run = True

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)
e = random.randint(1, 100)

async def main():
    while True:
        hi = str(await input("What fact would you like to check?: "))
        print("That is:", max(a, b, c, d, e), "% right.")
        if await input("Do you want to convert something else? (y/n)\n") == "n":
            break

globals()["main"] = main
