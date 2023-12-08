from functools import cmp_to_key
values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def compare(hand1, hand2):
    for x in range(6):
        if values.index(hand1[x]) < values.index(hand2[x]):
            return -1
        if values.index(hand1[x]) > values.index(hand2[x]):
            return 1
    return 0

def calculate_strength(hand: str) -> str:
    if len(set(hand)) == 1: return 'five'
    
    if len(set(hand)) == 2:
        if 'J' in hand:
            return 'five'
        elif hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            return 'four'
        else: return 'full'
     
    if len(set(hand)) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            if 'J' in hand: return 'four'
            else: return 'three'
        else: 
            if 'J' in hand:
                if hand.count('J') == 2:
                    return 'four'
                else:
                    return 'full'
            else:
                return 'two' 
    
    if len(set(hand)) == 4: 
        if 'J' in hand:
            return 'three'
        else:
            return 'one'
    
    if len(set(hand)) == 5: 
        if 'J' in hand:
            return 'one'
        else:
            return 'high'


with open('input.txt') as f:
    lines = f.readlines()
    bids = {}
    ranks = []
    total = 0

    fives = []
    fours = []
    full  = []
    threes= []
    two_pair =  []
    one_pair = []
    highs = []

    
    for line in lines:
        [hand, bid] = line.strip().split(' ')

        bids[hand] = int(bid)

        if calculate_strength(hand) == 'five':
            fives.append(hand) 
        elif calculate_strength(hand) == 'four':
            fours.append(hand)
        elif calculate_strength(hand) == 'full':
            full.append(hand)
        elif calculate_strength(hand) == 'three':
            threes.append(hand)
        elif calculate_strength(hand) == 'two':
            two_pair.append(hand)
        elif calculate_strength(hand) == 'one':
            one_pair.append(hand)
        else: 
            highs.append(hand)  

    fives = sorted(fives, key=cmp_to_key(compare))
    fours = sorted(fours, key=cmp_to_key(compare))
    full = sorted(full, key=cmp_to_key(compare))
    threes = sorted(threes, key=cmp_to_key(compare))
    two_pair = sorted(two_pair, key=cmp_to_key(compare))
    one_pair = sorted(one_pair, key=cmp_to_key(compare))
    highs = sorted(highs, key=cmp_to_key(compare))

    for hand in fives:
        ranks.append(hand)
    for hand in fours:
        ranks.append(hand)
    for hand in full:
        ranks.append(hand)
    for hand in threes:
        ranks.append(hand)
    for hand in two_pair:
        ranks.append(hand)
    for hand in one_pair:
        ranks.append(hand)
    for hand in highs:
        ranks.append(hand)
    
    for idx, hand in enumerate(reversed(ranks)):
        total += (idx+1) * bids[hand]
    
    print(total)
