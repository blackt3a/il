






with open("./bank.txt","r") as target:
    data = target.read()
    for line in data.split(","):
        print(line)
