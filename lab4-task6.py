sn = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))
inn = int(input("Enter the increment number: "))

print("Numbers from 0 to starting number:")
for i in range(0, sn + 1):
    print(i)

print("Numbers from 1 to starting number:")
for i in range(1, sn + 1):
    print(i)

print("Numbers from starting number to ending number:")
for i in range(sn, en + 1):
    print(i)

print("Numbers from starting number to ending number with increment:")
for i in range(sn, en + 1, inn):
    print(i)