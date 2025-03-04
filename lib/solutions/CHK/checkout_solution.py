from collections import Counter
#
# noinspection PyUnusedLocal
# skus = unicode string

def apply_offers(skus_count: dict) -> dict:
    """
    Removes Skus from skus count when an offer is applicable by applying the offers
    When the offer removes the same letter, add 1 more to the offers dictionary.
    """
    offers = {"E": [(2, "B")],
              "F": [(3, "F")],
              "N": [(3, "M")],
              "R": [(3, "Q")],
              "U": [(4, "U")],
              }
    for item, rules in offers.items():
        for rule in rules:
            if item in skus_count:
                amount_of_free_items, free_item = rule
                num_free_items = skus_count[item] // amount_of_free_items
                skus_count[free_item] =  max(0, skus_count.get(free_item, 0) - num_free_items)
    return skus_count

def apply_discounts(skus_count: dict) -> int:
    """
    Applies discount to total and removes Skus used for that discount.
    In the discounts dictionary, make sure larges discount is always first
    """
    discounts = {"A": [(5, 200), (3, 130)],
                 "B": [(2, 45)],
                 "H": [(10, 80), (5, 45)],
                 "K": [(2, 150)],
                 "P": [(5, 200)],
                 "Q": [(3, 80)],
                 "V": [(3, 130), (2, 90)]}
    total = 0
    for item, rules in discounts.items():
        if item not in skus_count or skus_count[item] == 0:
            continue
        for rule in rules:
            amount_of_free_items, amount = rule
            total += (skus_count[item] // amount_of_free_items) * amount
            skus_count[item] -= (skus_count[item] // amount_of_free_items) * amount_of_free_items
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
        if remaining_skus_number > 0:
            total+= values[item]*remaining_skus_number
    return total








