from collections import defaultdict


with open('input.txt') as f:
    lines = f.readlines();
    lines = [line.strip() for line in lines]

    cards = []

    for line in lines:
        _, card = line.split(':')
        cards.append({"copies": 1, "card": card.strip()})
    
    for idx, card in enumerate(cards):
        [winning, mine] = card["card"].split('|')
        winning = winning.split()
        mine = mine.split()

        for _ in range(card["copies"]):
            wins = 0
            for number in mine:
                if number in winning:
                    wins+=1
                    if idx + wins >=len(cards):
                        cards[-1]["copies"] +=1 
                    else:
                        cards[idx+wins]["copies"] += 1
    total = sum([card["copies"] for card in cards])
    print(total)