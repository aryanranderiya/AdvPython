import csv

def top_3_products(ratings: dict) -> dict:
    try:
        return dict(sorted(ratings.items(), key=lambda x: x[1], reverse=True)[:3])
    except Exception as e:
        print(f"Error in top_3_products: {e}")
        return {}

def create_summary(reviews: list, top3: list, valid_review_count: int, invalid_review_count: int) -> None:
    try:
        with open("summary.txt", "w") as f:
            f.write(f"Number of Reviews: {len(reviews)} \n")
            f.write(f"Number of Valid Reviews: {valid_review_count} \n")
            f.write(f"Number of Invalid Reviews: {invalid_review_count} \n\n")
            f.write(f"Top 3 Rated products: \n")

            for product in top3:
                f.write(f"ID: {product[0]}, Rating: {product[1]}\n")

        print("\nsummary.txt written\n")
    except IOError as e:
        print(f"Error writing summary file: {e}")

def process_files(file_paths: list) -> dict:
    ratings = {}
    valid_review_count: int = 0
    invalid_review_count: int = 0

    for file_path in file_paths:
        try:
            avg_rating = 0
            line_count = 0
            current_productid = None

            with open(file_path, newline='') as csvfile:
                reader = list(csv.DictReader(csvfile))
                if not reader:
                    print(f"No data found in {file_path}")
                    continue
                
                current_productid = reader[0]["Product ID"]

                for row in reader:
                    line_count += 1
                    is_review_valid = check_review_valid(row)
                    valid_review_count += 1 if is_review_valid else 0
                    invalid_review_count += 1 if not is_review_valid else 0
                    avg_rating += int(row['Review Rating'])
                    
                if line_count > 0:
                    ratings[current_productid] = avg_rating / line_count
                else:
                    print(f"No valid lines in {file_path}")

        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except KeyError as e:
            print(f"Missing expected key in file: {e}")
        except ValueError as e:
            print(f"Data conversion error: {e}")
        except Exception as e:
            print(f"Unexpected error processing file {file_path}: {e}")

    return ratings, valid_review_count, invalid_review_count

def check_review_valid(row) -> bool:
    try:
        if not is_valid_date(row["Review Date"]):
            return False
        if len(row["Customer ID"]) != 6 or len(row["Product ID"]) != 10:
            return False
        if not row["Review Rating"].isnumeric() or not 1 <= int(row["Review Rating"]) <= 5:
            return False
        if not row["Review Text"]:
            return False
        
        return True

    except Exception as e:
        print(f"Exception in review validation: {e}")
        return False


def is_valid_date(date_str) -> bool:
    date_parts = date_str.split("-")
    return len(date_parts) == 3 and len(date_parts[0]) == 4 and len(date_parts[1]) == 2 and len(date_parts[2]) == 2


def main():
    try:
        reviews, valid_review_count, invalid_review_count = process_files(["product1.csv", "product2.csv", "product3.csv", "product4.csv", "product5.csv"])
        products = top_3_products(reviews)
        create_summary(reviews, products, valid_review_count, invalid_review_count)
        print("All Ratings: ", reviews, end="\n")
        print("Top 3 Products: ", products, end="\n")
        print("Valid Reviews: ", valid_review_count, end="\n")
        print("Invalid Reviews: ", invalid_review_count, end="\n\n")
    except Exception as e:
        print(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()
