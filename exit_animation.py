import time

sentence = "exiting the program"

for i in range(1, 4):
    print(f"\r{sentence}{'.' * i}", end="")
    time.sleep(1)

print()  # Move to the next line after finishing
