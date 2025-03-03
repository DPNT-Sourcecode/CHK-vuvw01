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

        total += (A_counter // 3) * 130 + A_counter % 3 * values["A"]

        total+= (B_counter // 2) * 45 + B_counter % 2 * values["B"]

        total += C_counter * values["C"] + D_counter * values["D"]
        return total
    else:
        return -1

def test_checkout():
    assert checkout('AAAAABBBBCCCCDDDDEE') == 480
    assert checkout('ABCD') ==  155
    assert checkout('EEB') == 80
if __name__ == '__main__':
    test_checkout()

