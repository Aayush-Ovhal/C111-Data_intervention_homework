import pandas as pd
import csv
import plotly.figure_factory as  pff
import plotly.graph_objects as go
import random as rand
import statistics as st

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

def array_of_hundred_mean(counter):
     dataset = []
     for i in range(0, counter):
         random_index = rand.randint(0, len(data) - 1)
         value = data[random_index]
         dataset.append(value)
     mean = st.mean(dataset)
     return mean

mean_list = []
for i in range(0, 1000):
    aohm = array_of_hundred_mean(100)
    mean_list.append(aohm)

std_deviation = st.stdev(mean_list)
mean = st.mean(mean_list)
print("mean of sampling distribution: " + str(mean))
print("standard deviation of sampling distibution: " + str(std_deviation))

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * std_deviation), mean + (2 * std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3 * std_deviation), mean + (3 * std_deviation)

# Mafs Lab
df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
sample1_mean = st.mean(data)
print("mean of sample1:- " + str(sample1_mean))
graph = pff.create_distplot([mean_list], ["student marks"], show_hist=False)
graph.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
graph.add_trace(go.Scatter(x=[sample1_mean, sample1_mean], y=[0, 0.17], mode="lines", name="MATH LAB"))
graph.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "standard deviation 1" ))
graph.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="standard deviation 2"))
graph.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="standard deviation 3"))
graph.show()

# Mafs Practice Lab
df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
sample2_mean = st.mean(data)
print("mean of sample2:- " + str(sample2_mean))
graph = pff.create_distplot([mean_list], ["student marks"], show_hist=False)
graph.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
graph.add_trace(go.Scatter(x=[sample2_mean, sample2_mean], y=[0, 0.17], mode="lines", name="MATH PRACTICE LAB"))
graph.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "standard deviation 1" ))
graph.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="standard deviation 2"))
graph.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="standard deviation 3"))
graph.show()

# Mafs Forced with Register
df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
sample3_mean = st.mean(data)
print("mean of sample3:- " + str(sample3_mean))
graph = pff.create_distplot([mean_list], ["student marks"], show_hist=False)
graph.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
graph.add_trace(go.Scatter(x=[sample3_mean, sample3_mean], y=[0, 0.17], mode="lines", name="FORCED WITH REGISTER"))
graph.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "standard deviation 1" ))
graph.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="standard deviation 2"))
graph.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="standard deviation 3"))
graph.show()


