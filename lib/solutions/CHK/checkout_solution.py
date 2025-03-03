import unittest

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    values = {"A": 50, "B": 30, "C": 20, "D": 15}
    A_counter = 0
    B_counter = 0
    C_counter = 0
    D_counter = 0
    if set(skus).issubset({"A", "B", "C", "D"}):
        for i in skus:
            if i == 'A':
                A_counter += 1
            if i == 'B':
                B_counter += 1
            if i == 'C':
                C_counter += 1
            if i == 'D':
                D_counter += 1
        if A_counter > 3:
            A_result = (A_counter // 3) * 130 + A_counter % 3 * values["A"]
            print()
        if B_counter > 3:
            B_result = (B_counter // 3) * 130 + B_counter % 3 * values["B"]

        return C_counter * values["C"] + D_counter * values["D"] + A_result + B_result

    else:
        return -1

print(checkout("AAAAAAAAAA"), )
