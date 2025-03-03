from collections import Counter
#
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    values = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50, "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}
    discounts = {"A": [(5, 200), (3, 130)],
                 "B": [(2, 45)],
                 "E": [(2, "B")],
                 "F": [(2, "F")],
                 "H": [(5, 45), (10, 80)],
                 "K": [(2, 150)],
                 "N": [(3, "M")],
                 "P": [(5, 200)],
                 "Q": [(3, 80)],
                 "R": [(3, "Q")],
                 "U": [(3, "U")],
                 "V": [(2, 90), (3, 130)]}
    A_counter =  B_counter = C_counter = D_counter = E_counter = F_counter = total = 0
    if not set(skus).issubset({"A", "B", "C", "D", "E", "F"}):
        return -1
    skus_count = Counter(skus)
    print(skus_count)
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
        if i == 'F':
            F_counter += 1
    amount_of_discounts = E_counter // 2
    B_counter = max(0, B_counter - amount_of_discounts)
    total += (B_counter // 2) * 45
    B_counter %=2
    total += B_counter * values["B"]
    total += (A_counter // 5) * 200
    A_counter %= 5
    total += (A_counter // 3) * 130
    A_counter %= 3
    total+= A_counter * values["A"]
    total += C_counter * values["C"] + D_counter * values["D"] + E_counter * values["E"]
    total += (F_counter // 3) * (2 * values["F"])
    F_counter %= 3
    total += F_counter * values["F"]

    return total

print(checkout("AAABBCCDD"))

