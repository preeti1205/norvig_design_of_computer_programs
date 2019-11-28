def poker(hands):
	return max(hands, key=hand_rank)

def hand_rank(hand):
	ranks = card_ranks(hand)    #returns in sorted order
	if straight(ranks) and flush(hand): #straight flush
		return (8, max(ranks))
	elif kind(4, hands):
		return (7, kind(4, hands), kind(1,hands))
	elif kind(3, ranks) and kind(2, ranks):        # full house
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):                              # flush
		return (5, ranks )
	elif straight(ranks):                          # straight
		return (4, max(ranks))
	elif kind(3, ranks):                           # 3 of a kind
		return (3, kind(3, max(ranks)), ranks)
	elif two_pair(ranks):                          # 2 pair
		return (2, two_pair(ranks), ranks)
	elif kind(2, ranks):                           # kind
		return (1, kind(2, ranks), ranks)
	else:                                          # high card
		return (0, ranks)


def card_ranks(cards):
	ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
	ranks.sort(reverse = True)
	return ranks

def straight(ranks):
	return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
	suits = [s for r,s in hand]
	return len(set(suits)) == 1

def kind(n, ranks):
	"""Return the first rank that this hand has exactly n of.
	Return None if there is no n-of-a-kind in the hand."""
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None

def two_pairs(ranks):
	"""If there are two pair, return the two ranks as a
	tuple: (highest, lowest); otherwise return None."""
	pair_1 = kind(2, ranks)
	pair_2 = kind(2, list(reversed(ranks)))
	if pair_1 and pair_1 != pair_2:
		return (pair_1, pair_2)
	return None


def test():
	"Test cases for the functions in poker program"
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House	
	assert poker([sf, fk, fh]) == sf
	assert poker([fk, fh]) == fk
	assert poker([fh, fh]) == fh
	assert poker([sf]) == sf
	assert poker([sf] + 99*[fh]) == sf

	assert hand_rank(sf) == (8, 10)
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10,7) 

	assert card_rank(sf) == [10, 9, 8, 7, 6]
	assert card_rank(fk) == [9, 9, 9, 9, 7]
	assert card_rank(fh) == [10, 10, 10, 7, 7]

	assert straight([9, 8, 7, 6, 5]) == True
	assert straight([9,8,7,6,6]) == False
	assert flush(sf) == True
	assert flush(fh) == False
	return 'tests passed'