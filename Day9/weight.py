from functools import reduce

scores  = [80, 90, 70]
weights = [0.3, 0.5, 0.2]
# Using reduce to calculate the weighted score
weighted_score = reduce(
    lambda acc, pair: acc + pair[0] * pair[1],
    zip(scores, weights),
    0
)
print("Weighted Score (using reduce): ", weighted_score)
# Using sum and a generator expression to calculate the weighted score
score = sum(s * w for s, w in zip(scores, weights))
print("Weighted Score (using sum): ", score)