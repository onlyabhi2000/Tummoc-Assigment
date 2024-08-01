
# Voter  assignment
def vote(name, candidates_votes):
    if name in candidates_votes:
        candidates_votes[name] += 1
        return True
    else:
        return False


def print_winner(candidates_votes):
    max_votes = max(candidates_votes.values())
    winners = [name for name, votes in candidates_votes.items() if votes == max_votes]

    for winner in winners:
        print(winner)


candidates_votes = {
    'Abhishek': 0,
    'Kumar ': 0,
    'Sharma': 0,
}

votes = ['Abhishek', 'Kumar', 'Abhishek', 'Abhishek', 'Kumar', 'Sharma', 'Sharma', 'Abhishek']
for vote_name in votes:
    vote(vote_name, candidates_votes)

sorted_candidates = dict()
for candidate in sorted(candidates_votes, key=candidates_votes.get, reverse=True):
    sorted_candidates[candidate] = candidates_votes[candidate]

print(f"Votes gievn by", sorted_candidates)

print("Winner is :")
print_winner(sorted_candidates)
