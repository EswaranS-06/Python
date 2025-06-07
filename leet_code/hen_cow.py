heads = 36#int(input("head count: "))
legs = 122#int(input("legs count: "))

for hen in range(1, heads+1):
    cow = heads-hen
    c_heads = hen + cow
    c_legs = (hen*2) + (cow*4)
    if legs == c_legs:
        print(f"hens: {hen}\ncows: {cow}")