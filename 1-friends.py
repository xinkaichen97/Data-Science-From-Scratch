from __future__ import division
from collections import Counter
from collections import defaultdict

users = [{"id": 0, "name": "Hero"}, {"id": 1, "name": "Dunn"}, {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"}, {"id": 4, "name": "Thor"}, {"id": 5, "name": "Clive"}, {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"}, {"id": 8, "name": "Kate"}, {"id": 9, "name": "Klein"}]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
for u in users:
    u["friends"] = []
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
print(users)


def number_of_friends(user):
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users
print(total_connections, avg_connections)
number_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(number_friends_by_id)
number_friends_by_id = sorted(number_friends_by_id, key=lambda x: x[1], reverse=True)
print(number_friends_by_id)


def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    return all(not_the_same(one_user, other_user) for one_user in user["friends"])


def friends_of_friends_id(user):
    return Counter(foaf["id"] for friend in user["friends"] for foaf in friend["friends"]
            if not_the_same(user, foaf) and not_friends(user, foaf))


#print(users[3]["friends"])
#print([foaf["id"] for friend in users[3]["friends"] for foaf in friend["friends"]])
print(friends_of_friends_id(users[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientist_who_like(target_interest):
    return [user_id for user_id, interest in interests if interest == target_interest]


user_id_by_interest = defaultdict(list)
interest_by_user_id = defaultdict(list)
for user_id, interest in interests:
    user_id_by_interest[interest].append(user_id)
    interest_by_user_id[user_id].append(interest)


def most_common_interests_with(user):
    return Counter(id for interest in interest_by_user_id[user["id"]] for id in user_id_by_interest[interest] if id != user["id"])


random_user_interest = interest_by_user_id[users[0]["id"]]
print(random_user_interest)
print(most_common_interests_with(users[0]))

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {tenure_bucket : sum(salaries) / len(salaries) for tenure_bucket, salaries in salary_by_tenure_bucket.items()}
print(average_salary_by_bucket)


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

words_and_counts = Counter(word for user, interest in interests for word in interest.lower().split())
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)