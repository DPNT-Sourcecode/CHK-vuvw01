import unittest

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    values = {"A": 50, "B": 30, "C": 20, "D": 15}
    A_counter = 0
    B_counter = 0
    C_counter = 0
    D_counter = 0
    total = 0
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
            total += (A_counter // 3) * 130 + A_counter % 3 * values["A"]
            print("total:" , total)
        if B_counter > 3:
            total+= (B_counter // 2) * 45 + B_counter % 2 * values["B"]
            print("total 1:", total)
        total += C_counter * values["C"] + D_counter * values["D"]
        print("total 3:", total)
        return total
    else:
        return -1

print(checkout("AAABBBCD"))
def test_checkout():
    assert checkout("AAAAAAAA") == 360
    assert checkout("BBBBBBAAAA") == 315
    assert checkout("AAABBBCD") == 240
    assert checkout("ABCD") == 115
    assert checkout("8") == -1


# if __name__ == '__main__':
#     test_checkout()

