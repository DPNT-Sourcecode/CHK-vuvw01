

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    values = {"A": 50, "B": 30, "C": 20, "D": 15}
    A_counter = 0
    B_counter = 0
    C_counter = 0
    D_counter = 0
    if set(skus).issubset("ABCD"):
        for i in skus:
            if i == 'A':
                A_counter += 1
            if i == 'B':
                B_counter += 1
            if i == 'C':
                C_counter += 1
            if i == 'D':
                D_counter += 1
        if A_counter == 3:
            values["A"] = 130
        if B_counter == 2:
            values["B"] = 45
        return A_counter * values["A"] + B_counter * values["B"] + C_counter * values["C"] + D_counter * values["D"]
    else:
        return -1


print(checkout("ABCD"))

def test_checkout():
    assert checkout("ABC8") == -1
    assert checkout("ABCD") == 50+30+20+15
    assert checkout("AABCD") == 50+30+20+15
    assert checkout("AAABCD") == 130+30+20+15
    assert checkout("AABBCD") == 50+45+20+15
    assert checkout("AABCCDD") == 50+50+45+20+20+15+15

if __name__ == "__main__":
    test_checkout()