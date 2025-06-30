def isEmpty(m):
    return bool(m)

def reload(m):
    nc = int(input("Enter how many No of cloths: "))
    m = nc if nc < 5 else 4
    if nc < 5:
        m = nc
        print(f"Wait for {m} rounds\n")
        return m
    else:
        m = 4
        print(f"Wait for {m} rounds and Machine can only Handle Max[4] \n So Have your remaining {nc - 4} cloths\n")
        return m
    
def unload(m):
    return m-1 if isEmpty(m) else m
    
m1 = m2 = m3 = m4 = 0
print("Welcome To Our  Laundary")
while True:
    c = 1
    for i in m1, m2, m3, m4:
        print(f"Machine {c} is Filled with {i} cloths" if isEmpty(i) else f"Machine {c} is Empty")
        c+=1
    c = int(input("\nSelect any empty machine: "))
    if c == 0:
        print(f"\nThank you, Comeback next time")
    elif c == 1:
        if isEmpty(m1):
            print(f"\nThis Machine still have {m1} cloths\n")
            continue
        m1 = reload(m1)
    elif c == 2:
        if isEmpty(m2):
            print(f"\nThis Machine still have {m2} cloths\n")
            continue
        m2 = reload(m2)
    elif c == 3:
        if isEmpty(m3):
            print(f"\nThis Machine still have {m3} cloths\n")
            continue
        m3 = reload(m3)
    elif c == 4:
        if isEmpty(m4):
            print(f"\nThis Machine still have {m4} cloths\n")
            continue
        m4 = reload(m4)
    else:
        print("\nOpen your eyes wide,\nThere is only 4 Machines")
        
    m1 = unload(m1)
    m2 = unload(m2)
    m3 = unload(m3)
    m4 = unload(m4)
    
    if isEmpty(m1) and isEmpty(m2) and isEmpty(m3) and isEmpty(m4):
        print("\nFour Minutes Later!!!\n")
        m1 = m2 = m3 = m4 = 0