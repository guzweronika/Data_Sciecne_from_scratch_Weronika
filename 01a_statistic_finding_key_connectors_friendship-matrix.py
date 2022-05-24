from __future__ import division
from collections import Counter
import matplotlib.pyplot as plt
import math

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

            #   0  1  2  3  4  5  6  7  8  9
friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9


#------------------------------------------------------------------------

num_friends = [68, 37, 31, 38, 8, 99, 35, 27, 35, 5, 10, 32, 6, 6, 36, 5, 37, 5, 61, 47, 7, 40, 2, 5, 37, 6, 5, 11, 27, 28, 38, 12, 5, 18, 11, 18, 10, 18, 1, 29, 11, 24, 24, 4, 37, 9, 39, 7, 17, 8, 21, 14, 4, 15, 28, 2, 17, 23, 8, 4, 3, 3, 22, 35, 37, 16, 5, 17, 37, 19, 10, 6, 9, 9, 1, 1, 36, 1, 36, 5, 3, 1, 1, 37, 2, 2, 1, 2, 18, 3, 11, 4, 13, 14, 2, 5, 6, 1, 6, 8, 3, 6, 3, 2, 9, 6, 9, 4, 9, 6, 6, 5, 3, 6, 14, 9, 6, 9, 7, 8, 6, 6, 9, 6, 15, 8, 4, 3, 4, 6, 19, 4, 24, 1, 17, 28, 27, 35, 18, 3, 25, 16, 17, 15, 11, 2, 19, 14, 2, 10, 17, 17, 1, 26, 11, 24, 16, 7, 4, 10, 17, 1, 10, 9, 14, 24, 4, 8, 8, 20, 18, 10, 20, 25, 18, 8, 9, 2, 6, 27, 24, 3, 6, 8, 6, 3, 6, 6, 5, 8, 9, 10, 16, 6, 12, 3, 10, 24, 27, 11, 11, 14, 14, 7, 18, 13, 14, 18, 8, 6, 8, 27, 21, 21, 14, 15, 7, 7, 10, 1, 8, 6, 4, 18, 6, 7, 1, 15, 10, 5, 21, 4, 3, 21, 18, 4, 12, 12, 11, 14, 8, 5, 7, 3, 7, 6, 3, 9, 5, 5, 1, 6, 6, 3, 4, 20, 9, 34, 18, 5, 1, 15, 19, 14, 17, 8, 7, 18, 6, 14, 18, 18, 24, 7, 7, 8, 6, 15, 8, 3, 9, 6, 6, 7, 4, 1, 10, 17, 10, 17, 16, 10, 8, 13, 9, 15, 4, 6, 20, 21, 5, 38, 16, 8]

daily_minutes = [37, 71, 72, 41, 74, 45, 49, 73, 70, 68, 68, 39, 80, 52, 33, 61, 36, 73, 60, 33, 45, 55, 70, 51, 42, 70, 46, 72, 61, 70, 46, 80, 58, 80, 77, 42, 31, 61, 32, 61, 42, 45, 52, 47, 80, 70, 77, 55, 50, 60, 59, 48, 56, 79, 49, 60, 63, 45, 71, 32, 34, 33, 60, 70, 54, 62, 46, 44, 42, 46, 70, 30, 67, 34, 35, 52, 72, 49, 69, 75, 57, 57, 80, 30, 43, 34, 73, 64, 33, 43, 77, 62, 79, 79, 41, 48, 34, 56, 48, 38, 45, 59, 64, 33, 61, 31, 72, 39, 37, 54, 66, 39, 35, 56, 64, 71, 59, 58, 61, 65, 52, 57, 80, 31, 41, 76, 41, 53, 68, 36, 44, 78, 52, 49, 67, 46, 31, 70, 47, 59, 37, 65, 34, 50, 52, 45, 79, 69, 52, 53, 70, 66, 64, 52, 61, 37, 64, 77, 69, 39, 63, 62, 60, 71, 34, 44, 47, 41, 69, 55, 46, 62, 55, 64, 61, 39, 75, 36, 65, 69, 54, 62, 36, 37, 47, 34, 76, 45, 72, 56, 40, 40, 61, 55, 76, 75, 37, 74, 70, 39, 68, 71, 77, 71, 73, 42, 62, 74, 36, 60, 71, 75, 49, 74, 67, 59, 69, 57, 62, 46, 74, 49, 70, 32, 56, 37, 79, 58, 72, 73, 36, 78, 71, 75, 71, 67, 41, 64, 58, 67, 33, 68, 69, 41, 39, 60, 39, 36, 58, 55, 37, 52, 37, 36, 50, 77, 60, 73, 43, 66, 46, 76, 63, 44, 62, 34, 73, 59, 57, 68, 77, 60, 53, 70, 79, 47, 51, 79, 31, 58, 69, 51, 38, 69, 46, 41, 40, 70, 41, 50, 34, 36, 77, 75, 56, 69, 38, 51, 42, 44, 62, 75, 73, 40]


friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 40])
plt.title("History of Friend Counts")
plt.xlabel("# of friend")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)   # 304
largest_value = max(num_friends)    #99
smallest_value = min(num_friends)   # 1

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]   # 1
second_smallest_value = sorted_values[1]    # 1
second_largest_value = sorted_values[-2]    # 68


def mean(x: list) -> float:
    return sum(x)/len(x)


print(f"Mean: {mean(num_friends):0.2f}")     # 12.98


def median(v: list) -> float:
    """find middle value of v-list"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


print(f"Median: {median(num_friends)}")     # 9.0


def quantile(x: list, p: float) -> int:
    """return the pth-percentile value in x"""
    p_index = int(p*len(x))
    return sorted(x)[p_index]


print(f"Quantile 10%: {quantile(num_friends, 0.10)}")    # 3
print(f"Quantile 25%: {quantile(num_friends, 0.25)}")    # 6
print(f"Quantile 50%: {quantile(num_friends, 0.50)}")    # 9
print(f"Quantile 75%: {quantile(num_friends, 0.75)}")    # 18
print(f"Quantile 90%: {quantile(num_friends, 0.90)}")    # 27


def mode(x: list) -> list:
    """return a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


print(f"Mode: {mode(num_friends)}")     # [6]


# "range" already means something in Python, so we'll use a different name
def data_range(x: list) -> int:
    return max(x) - min(x)


print(f"Data Range: {data_range(num_friends)}")     # 98


def de_mean(x: list) -> list:
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def dot(v: list, w: list) -> int:
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_square(v: list) -> int:
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def variance(x: list) -> float:
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_square(deviations) / (n - 1)


print(f"Variance: {variance(num_friends):.2f}")     # 137.19


def standard_deviations(x: list) -> float:
    return math.sqrt(variance(x))


print(f"Standard deviation: {standard_deviations(num_friends):.2f}")     # 11.71


def interquantile_range(x: list) -> int:
    return quantile(x, 0.75) - quantile(x, 0.25)


print(f"Inter quantile range: {interquantile_range(num_friends)}")        # 12


def covariance(x: list, y: list) -> float:
    """
    :params x: list of number of friends
    :params y: list of minutes, which each user spend on DataSciencester
    len(x) == len(y)"""

    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

print(f"Convarience: {covariance(num_friends, daily_minutes):.2f}")     # 4.27 - num_friends tends to be big when daily_minutes is small


def correlation(x: list, y: list) -> float:
    stdev_x = standard_deviations(x)
    stdev_y = standard_deviations(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero


print(f"Correlation: {correlation(num_friends, daily_minutes):.2f}")    # 0.03 - correlation in range (-1, 1) is desired


# Correlation with an outliner
plt.scatter(num_friends, daily_minutes)
plt.axis([0, 101, 0, 101])
plt.title("Correlation with an Outliner")
plt.xlabel("of friends")
plt.ylabel("minutes per day")
plt.show()


outliners = [num_friends.index(out) for out in num_friends if out < 41]     # indexs of outliners
num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i not in outliners]
daily_minutes_good = [x
                    for i, x in enumerate(daily_minutes)
                    if i not in outliners]


print(f"Correlation after clean up: {correlation(num_friends_good, daily_minutes_good):.2f}")    # 0.02 - correlation in range (-1, 1) is desired, and the best is when is close to 0


# Correlation after removing the outliners
plt.scatter(num_friends_good, daily_minutes_good)
plt.axis([0, 45, 0, 85])
plt.title("Correlation with an Outliner")
plt.xlabel("of friends")
plt.ylabel("minutes per day")
plt.show()