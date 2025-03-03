from collections import Counter
#
# noinspection PyUnusedLocal
# skus = unicode string

discounts = {"A": [(5, 200), (3, 130)],
                 "B": [(2, 45)],
                 "H": [(5, 45), (10, 80)],
                 "K": [(2, 150)],
                 "P": [(5, 200)],
                 "Q": [(3, 80)],
                 "V": [(2, 90), (3, 130)]}
offers = {  "E": [(2, "B")],
            "F": [(2, "F")],
            "N": [(3, "M")],
            "R": [(3, "Q")],
            "U": [(3, "U")],
            }

def apply_offers(offers, skus_count):
    for item, rules in offers.items():
        for rule in rules:
            if isinstance(rule[1], str):
                amount_of_free_items = rule[0]
                free_item = rule[1]
                num_free_items = skus_count[item] // amount_of_free_items
                skus_count[free_item] =  max(0, skus_count.get(free_item, 0) - num_free_items)
    return skus_count

def apply_discounts(discounts: dict, skus_count: dict) -> int:# this function should be called at the beginning OR use OOP.
    total = 0
    for item, rules in discounts.items():
        for rule in rules:
            print("rule", rule)
            print("item:", item)
            print("skus", skus_count[item])
            print("rule[1]:", rule[1])
            # check if there are enough item_count
            total += (skus_count[item] // rule[0]) * rule[1] # 2//5 * 100
            print("total", total)
            skus_count_to_remove =  rule[0]
            skus_count[item] =  max(0, skus_count.get(item, 0) - skus_count_to_remove)
    print("\n\n final total", total)
    print("skus_count_after_removal", skus_count)
    return total



def checkout(skus: str) -> int:
    values = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50, "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}
    A_counter =  B_counter = C_counter = D_counter = E_counter = F_counter = total = 0
    if not set(skus).issubset({"A", "B", "C", "D", "E", "F"}):
        return -1
    skus_count = Counter(skus)
    print("apply offers", apply_offers(offers, skus_count))

    print("skus_count", skus_count)
    print("\n\n APPLY DISCOUNTS\n\n", apply_discounts(discounts, skus_count))
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

print(checkout("AA"))