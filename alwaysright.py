import random

run = True

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)

async def main():
    hi = str(await input("Ask a question: "))
    print("That is:", max(a, b, c), "% right.")

globals()["main"] = main
