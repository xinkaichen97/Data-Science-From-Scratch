from matplotlib import pyplot as plt
from collections import Counter

"""
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title('Nominal GDP')
plt.ylabel('Billions of $')
plt.show()
"""

"""
# --------------------------- Bar Chart ---------------------------
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(range(len(movies)), num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
plt.xticks(range(len(movies), movies)
plt.show()
"""

"""
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]


# decile = lambda grade: grade // 10 * 10
def decile(grade):
    return grade // 10 * 10


histogram = Counter(decile(grade) for grade in grades)
print(histogram)
plt.bar([x for x in histogram.keys()], histogram.values(), 8)
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Exam 1 Grades")
plt.show()
"""

"""
mentions = [500, 505]
years = [2013, 2014]
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
#plt.axis([2012.5, 2014.5, 499, 506]) # Huge difference
plt.axis([2012.5, 2014.5, 0, 550])
plt.title("Look at the not so huge Increase!")
plt.show()
"""

"""
# --------------------------- Line Chart ---------------------------
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label='variance')  # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')  # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error')  # blue dotted line
plt.legend(loc=9)  # 9 means top center
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
"""

"""
# --------------------------- Scatterplot ---------------------------
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
# for i, txt in enumerate(labels):
#    plt.annotate(txt, xy=(friends[i], minutes[i]), xytext=(5, -5), textcoords='offset points')
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, xy=(friend_count, minute_count),  # put the label with its point
                 xytext=(5, -5),  # but slightly offset
                 textcoords='offset points')
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()
"""

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.axis("equal")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()

