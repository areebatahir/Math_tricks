import numpy as np
import matplotlib.pyplot as plt
def generate_random_data(size):
    random_data = np.random.randint.data(0, 10, size)
    return random_data
def analyze_data(data):
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    max_value = np.max(data)
    min_value = np.min(data)
    return mean, median, std_dev, max_value, min_value
def display_result(mean, median, std_dev, max_value, min_value):
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard_Deviation: {std_dev}")
    print(f"maximum_Value:{max_value}")
    print(f"Minimum_Value:{min_value}")
def visualize_data(data):
    plt.hist(data, bins=10, color = 'blue', edgecolor = 'red')
    plt.xlable("range")
    plt.ylable("data,value")
    plt.title("histogram range of data value")
    plt.show
if __name__ == "main":
    display_data = 100
    random_data = generate_random_data(size=100)
    mean, median, std_dev, max_value, min_value = analyze_data(random_data)
    display_data(mean, median, std_dev,max_value, min_value)
    visualize_data(random,data)

