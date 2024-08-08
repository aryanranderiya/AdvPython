import csv
import os


def load_train_data(filename="trains.csv"):
    trains = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                trains[row["Train ID"]] = {
                    "Train Name": row["Train Name"],
                    "Source Station": row["Source Station"],
                    "Destination Station": row["Destination Station"],
                    "Total Seats": int(row["Total Seats"]),
                    "Available Seats": int(row["Available Seats"]),
                    "Fare Per Ticket": int(row["Fare Per Ticket"]),
                    "Total Revenue": 0
                }
        print("Train data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error loading train data: {e}")
    return trains


def load_passenger_data(filename="passengers.csv"):
    passengers = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                passengers.append({
                    "Passenger Name": row["Passenger Name"],
                    "Train ID": row["Train ID"],
                    "Number of Tickets": int(row["Number of Tickets"])
                })
        print("Passenger data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error loading passenger data: {e}")
    return passengers


def check_seat_availability(trains, train_id, num_tickets):
    if train_id in trains:
        if trains[train_id]["Available Seats"] >= num_tickets:
            return True
        else:
            print(f"Not enough seats available on train {train_id}.")
            return False
    else:
        print(f"Train ID {train_id} not found.")
        return False


def update_seat_availability(trains, train_id, num_tickets):
    if check_seat_availability(trains, train_id, num_tickets):
        trains[train_id]["Available Seats"] -= num_tickets
        total_fare = num_tickets * trains[train_id]["Fare Per Ticket"]
        trains[train_id]["Total Revenue"] += total_fare
        print(f"Booking confirmed for {num_tickets} tickets on train {
              train_id}. Total fare: ${total_fare}.")
    else:
        print(f"Booking failed for train {
              train_id} for {num_tickets} tickets.")


def generate_report_1(trains):
    with open("report_1.txt", "w") as file:
        file.write("Report 1: Train Details\n")
        file.write(
            "Train ID, Train Name, Source Station, Destination Station, Total Seats, Available Seats\n")
        for train_id, details in trains.items():
            file.write(f"{train_id}, {details['Train Name']}, {details['Source Station']}, {
                       details['Destination Station']}, {details['Total Seats']}, {details['Available Seats']}\n")
    print("Report 1 generated: report_1.txt")


def generate_report_2(trains):
    with open("report_2.txt", "w") as file:
        file.write("Report 2: Revenue Details\n")
        file.write("Train ID, Total Revenue\n")
        for train_id, details in trains.items():
            file.write(f"{train_id}, ${details['Total Revenue']}\n")
    print("Report 2 generated: report_2.txt")


def main():
    directory = os.getcwd()
    trains = load_train_data(os.path.join(directory, "trains.csv"))
    passengers = load_passenger_data(os.path.join(directory, "passengers.csv"))

    for passenger in passengers:
        train_id = passenger["Train ID"]
        num_tickets = passenger["Number of Tickets"]
        if check_seat_availability(trains, train_id, num_tickets):
            update_seat_availability(trains, train_id, num_tickets)

    generate_report_1(trains)
    generate_report_2(trains)


if __name__ == "__main__":
    main()
