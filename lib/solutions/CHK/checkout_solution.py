from collections import Counter
#
# noinspection PyUnusedLocal
# skus = unicode string

def apply_offers(skus_count: dict) -> dict:
    """
    Removes Skus from skus count when an offer is applicable by applying the offers
    """
    offers = {"E": [(2, "B")],
              "F": [(2, "F")],
              "N": [(3, "M")],
              "R": [(3, "Q")],
              }
    for item, rules in offers.items():
        for rule in rules:
            if isinstance(rule[1], str):
                amount_of_free_items = rule[0]
                free_item = rule[1]
                num_free_items = skus_count[item] // amount_of_free_items
                skus_count[free_item] =  max(0, skus_count.get(free_item, 0) - num_free_items)
    return skus_count

def apply_discounts(skus_count: dict) -> int:
    """
    Applies discount to total and removes Skus used for that discount.
    """
    discounts = {"A": [(5, 200), (3, 130)],
                 "B": [(2, 45)],
                 "H": [(5, 45), (10, 80)],
                 "K": [(2, 150)],
                 "P": [(5, 200)],
                 "Q": [(3, 80)],
                 "V": [(2, 90), (3, 130)]}
    total = 0
    for item, rules in discounts.items():
        if item not in skus_count:
            for rule in rules:
                total += (skus_count[item] // rule[0]) * rule[1] # this is correct
                skus_count[item] -= skus_count[item] // rule[0] * rule[0]
    return total



def checkout(skus: str) -> int:
    values = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50, "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}
    A_counter =  B_counter = C_counter = D_counter = E_counter = F_counter = total = 0
    if not set(skus).issubset({"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}):
        return -1
    skus_count = Counter(skus)
    apply_offers(skus_count)
    total = apply_discounts(skus_count)
    for item, remaining_skus_number in skus_count.items():
        total+= values[item]*remaining_skus_number
    return total

print(checkout("HHHHHHHHHH"))
