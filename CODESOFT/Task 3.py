import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item matrix (users in rows, items in columns)
# Rows represent users and columns represent items (movies in this case)
user_item_matrix = np.array([
    [5, 3, 0, 0, 4],
    [4, 0, 0, 0, 0],
    [0, 4, 0, 5, 0],
    [0, 0, 3, 0, 0]
])

# Calculate item-item similarity using cosine similarity
item_similarity = cosine_similarity(user_item_matrix.T)

# Let's say we want to recommend items for user 2
target_user_ratings = user_item_matrix[1]  # Ratings for user 2

# Calculate predicted ratings for the target user
predicted_ratings = np.dot(item_similarity, target_user_ratings) / np.sum(np.abs(item_similarity), axis=1)

# Exclude movies the user has already rated
predicted_ratings[target_user_ratings.nonzero()] = 0

# Recommend top N movies
num_recommendations = 3
top_recommendations = np.argsort(predicted_ratings)[::-1][:num_recommendations]

print("Top recommended movies for user 2:")
for movie_index in top_recommendations:
    print(f"Movie {movie_index + 1}, Predicted Rating: {predicted_ratings[movie_index]:.2f}")
