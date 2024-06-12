import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Initialize lists to store data
dates = []
weights = []
ids = []

# CSV Reader
filename = 'csvFiles/AlluserStatistics.csv'
with open(filename, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Append the ID, weight, and date
        ids.append(row[0])  
        weights.append(float(row[-2]))  
        dates.append(row[-1])  

# Convert string dates to datetime objects for better plotting
dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

# Function to filter data by ID
def filter_data_by_id(ids, dates, weights, target_id):
    filtered_ids = []
    filtered_dates = []
    filtered_weights = []
    for id_, date, weight in zip(ids, dates, weights):
        if id_ == target_id:
            filtered_ids.append(id_)
            filtered_dates.append(date)
            filtered_weights.append(weight)
    return filtered_ids, filtered_dates, filtered_weights

# Function to filter data within a specific time range
def filter_data_by_time(dates, weights, start_date, end_date):
    filtered_dates = []
    filtered_weights = []
    for date, weight in zip(dates, weights):
        if start_date <= date <= end_date:
            filtered_dates.append(date)
            filtered_weights.append(weight)
    return filtered_dates, filtered_weights

# Get the current date
current_date = datetime.now()

# Filter data for one week, one month, and one year
one_week_ago = current_date - timedelta(weeks=1)
one_month_ago = current_date - timedelta(days=30)
one_year_ago = current_date - timedelta(days=365)

# Function to plot data
def plot_data(dates, weights, title):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, weights, marker='o', linestyle='--', color='b')
    plt.xlabel('Date')
    plt.ylabel('Weight')
    plt.title(title)
    plt.grid(True, which='both', axis='y')
    min_weight = int(min(weights))
    max_weight = int(max(weights))
    plt.yticks(range(min_weight - 5, max_weight + 5, 1))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Console question menu
def print_lines():
    print("-" * 100)

def weight_choice_options():
    print_lines()
    print("1. Week\n2. Month\n3. Year\n")
    user_input = input("Enter Your Option: ")
    return user_input

# Filter choice
def graph_period_choice(filtered_dates_week, filtered_weights_week, filtered_dates_month, filtered_weights_month, filtered_dates_year, filtered_weights_year):
    while True:
        choice = weight_choice_options()
        if choice == '1':
            plot_data(filtered_dates_week, filtered_weights_week, 'Weight over the Last Week')
            break
        elif choice == '2':
            plot_data(filtered_dates_month, filtered_weights_month, 'Weight over the Last Month')
            break
        elif choice == '3':
            plot_data(filtered_dates_year, filtered_weights_year, 'Weight over the Last Year')
            break
        else:
            print("Invalid choice. Please try again.")



# Main function to run the program
def Weight_main(user_id):

    # Filter data by the given ID
    filtered_ids, filtered_dates, filtered_weights = filter_data_by_id(ids, dates, weights, user_id)

    # Further filter the data by time periods
    filtered_dates_week, filtered_weights_week = filter_data_by_time(filtered_dates, filtered_weights, one_week_ago, current_date)
    filtered_dates_month, filtered_weights_month = filter_data_by_time(filtered_dates, filtered_weights, one_month_ago, current_date)
    filtered_dates_year, filtered_weights_year = filter_data_by_time(filtered_dates, filtered_weights, one_year_ago, current_date)

    # Display the menu to choose the period for the graph
    graph_period_choice(filtered_dates_week, filtered_weights_week, filtered_dates_month, filtered_weights_month, filtered_dates_year, filtered_weights_year)
