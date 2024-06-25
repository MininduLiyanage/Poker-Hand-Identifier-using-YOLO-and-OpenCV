def findPokerHand(hand):
    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]

        #convert ranks to int values for the ease of sorting
        if rank == "A":
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11

        ranks.append(int(rank))
        suits.append(suit)

    sortedRanks = sorted(ranks)

    # Identify Royal Flush and Straight Flush and Flush
    if suits.count(suits[0]) == 5:  # Check for Flush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks:
            possibleRanks.append(10)  # Royal Flush
        elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(9)   # Straight Flush
        else:
            possibleRanks.append(6)  # Flush

    handUniqueVals = list(set(sortedRanks))

    # Identify Four of a kind and Full House
    # 3 3 3 3 5 -- set= 3 5 - Four of a kind
    # 3 3 3 5 5 -- set= 3 5 - Full house
    if len(handUniqueVals) == 2:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 4:
                possibleRanks.append(8)     # Four of a kind
            if sortedRanks.count(val) == 3:
                possibleRanks.append(7)     # Full house

    # Identify Three of a Kind and Two Pair
    # 5 5 5 6 7 -- set= 5 6 7 - three of a kind
    # 8 8 7 7 2 -- set= 8 7 2 - two pair
    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 3:
                possibleRanks.append(4)       # three of a kind
            if sortedRanks.count(val) == 2:
                possibleRanks.append(3)       # two pair

    # Identify Pair
    # 5 5 3 6 7 -- set= 5 3 6 7 - Pair
    if len(handUniqueVals) == 4:
        possibleRanks.append(2)     # pair


    # Identify Straight
    if all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(5)     # Straight

    if not possibleRanks:
        possibleRanks.append(1)     # High Card

    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush",
                      5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}

    output = pokerHandRanks[max(possibleRanks)]

    print(hand, output)
    return output


if __name__ == "__main__":
        findPokerHand(["KH", "AH", "QH", "JH", "10H"])  # Royal Flush
        findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
        findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
        findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
        findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
        findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
        findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
        findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
        findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
        findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card