
# Reading JSON File
import json

# Sample JSON data in "data.json"
# {"name": "John Doe", "age": 30, "city": "New York"}
file_path = "data.json"

# Reading JSON data from the file
with open(file_path, "r") as json_file:
    data = json.load(json_file)

print("Read data from JSON file:", data)

# Writing JSON File
# Sample Python dictionary
data_to_write = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Writing JSON data to a file
output_file_path = "output.json"
with open(output_file_path, "w") as json_file:
    json.dump(data_to_write, json_file)

print("Data written to JSON file successfully.")



import pandas as pd
import matplotlib.pyplot as plt
import json
import os

def read_covid_data(directory):
    all_covid_data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    all_covid_data.append(data)
    return all_covid_data

def calculate_statistics(covid_data):
    statistics = []
    for data in covid_data:
        confirmed_cases = data['confirmed_cases']['total']
        deaths = data['deaths']['total']
        recovered = data['recovered']['total']
        active_cases = confirmed_cases - deaths - recovered
        statistics.append({
            'Country': data['country'],
            'Total Confirmed Cases': confirmed_cases,
            'Total Deaths': deaths,
            'Total Recovered': recovered,
            'Total Active Cases': active_cases
        })
    return statistics

def generate_summary_report(statistics):
    with open('covid19_summary.json', 'w', indent=2) as json_file:
        json.dump(statistics, json_file)

if __name__ == '__main__':
    covid_data_directory = 'covid_data'  # Replace with your directory path

    # Step 1: Read COVID-19 data from all JSON files
    covid_data = read_covid_data(covid_data_directory)

    # Step 2: Calculate statistics for each country
    statistics = calculate_statistics(covid_data)

    # Step 3: Determine the top 5 countries with the highest and lowest confirmed cases
    sorted_statistics = sorted(statistics, key=lambda x: x['Total Confirmed Cases'], reverse=True)
    top_5_highest_cases = sorted_statistics[:5]
    top_5_lowest_cases = sorted_statistics[-5:]

    # Step 4: Generate and save the summary report
    generate_summary_report(statistics)

    # Print the top 5 countries with the highest and lowest confirmed cases
    print("Top 5 Countries with Highest Confirmed Cases:")
    for country in top_5_highest_cases:
        print(f"Country: {country['Country']}, Confirmed Cases: {country['Total Confirmed Cases']}")

    print("\nTop 5 Countries with Lowest Confirmed Cases:")
    for country in top_5_lowest_cases:
        print(f"Country: {country['Country']}, Confirmed Cases: {country['Total Confirmed Cases']}")