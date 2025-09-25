y = 0
j = 0
for i in range(10):
    if i == 3:
        print("="*10)
        print("CR7")
        print("="*10)
        continue

    if i == 5:
        print("="*10)
        print("Arrascaeta")
        print("="*10)

    for j in range(1, 10):
            print(f"{i=}, {j=}, {y=}")

            for y in range(1, 10):
                 print(f"{i=}, {j=}, {y=}")
else:
    print("acabou")