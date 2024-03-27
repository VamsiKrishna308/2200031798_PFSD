#program-1
import random
import string

print("Random Color Hex:", "#{:06x}".format(random.randint(0, 0xFFFFFF)))
print("Random Alphabetical String:", ''.join(random.choice(string.ascii_lowercase) for _ in range(8)))
print("Random Value Between 10 and 20:", random.randint(10, 20))
print("Random Multiple of Seven between 7 and 70:", random.randint(1, 10) * 7)

#program-2
import random
from datetime import datetime, timedelta

print("Random Integer between 0 and 5 (excluding 6):", random.randrange(0, 6))
print("Random Integer between 5 and 9 (excluding 10):", random.randrange(5, 10))
print("Random Integer between 0 and 10 with a step of 3:", random.randrange(0, 11, 3))

start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)
random_date = start_date + timedelta(days=random.randrange((end_date - start_date).days))
print("Random Date between {} and {}: {}".format(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), random_date.strftime("%Y-%m-%d")))


#program-3
import pandas as pd
import matplotlib.pyplot as plt
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df
def generate_graph(data_frame):
    x_values = data_frame['REGNUM']
    y_columns = data_frame.columns[1:]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i,column in enumerate(y_columns):
        y_values = data_frame[column]
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=column, color = colors[i])
    # plt.plot(x_values, y_values, marker='o', linestyle='-', color=colors)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('CSV Data Plot')
    plt.grid(True)
    plt.legend()
    plt.savefig("a1.png")
    plt.show()

if __name__ == "__main__":
    file_path = "TRY1.csv"
    data_frame = read_csv_file(file_path)
    generate_graph(data_frame)