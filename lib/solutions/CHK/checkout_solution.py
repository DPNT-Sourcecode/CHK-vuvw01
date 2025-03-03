import unittest

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    values = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    A_counter = 0
    B_counter = 0
    C_counter = 0
    D_counter = 0
    E_counter = 0
    total = 0
    if set(skus).issubset({"A", "B", "C", "D", "E"}):
        for i in skus:
            if i == 'A':
                A_counter += 1
            if i == 'B':
                B_counter += 1
            if i == 'C':
                C_counter += 1
            if i == 'D':
                D_counter += 1
            if i == 'E':
                E_counter += 1
        if (A_counter // 5) >= 1:
            print("TRUE", A_counter // 5)
            total += (A_counter // 5) * 200 + (A_counter % 5 * values["A"])
        else:
            total += (A_counter // 3) * 130 + A_counter % 3 * values["A"]


        total+= (B_counter // 2) * 45 + B_counter % 2 * values["B"]

        total += C_counter * values["C"] + D_counter * values["D"]
        total += E_counter * values["E"]
        print("E_counter",  E_counter)
        if (E_counter // 2)>=1 and B_counter >= 1:
            #
            if (B_counter - (E_counter // 2) >= 0):
                total -= values["B"] * E_counter // 2

        return total
    else:
        return -1
