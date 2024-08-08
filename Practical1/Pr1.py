import os


def top_3_products(ratings: dict) -> list:
    try:
        return sorted(ratings.items(), key=lambda x: x[1], reverse=True)[:3]
    except Exception as e:
        print(f"Error in top_3_products: {e}")
        return []


def create_summary(reviews: int, valid_review_count: int, invalid_review_count: int, top3: list) -> None:
    try:
        with open("summary.txt", "w") as f:
            f.write(f"Total number of Reviews: {reviews} \n")
            f.write(f"Total number of Valid Reviews: {valid_review_count} \n")
            f.write(f"Total number of Invalid Reviews: {
                    invalid_review_count} \n\n")
            f.write(f"Top 3 Rated Products: \n")

            for product in top3:
                f.write(f"Product ID: {product[0]}, Average Rating: {
                        product[1]:.2f}\n")

        print("\nsummary.txt written\n")
    except IOError as e:
        print(f"Error writing summary file: {e}")


def process_files(directory: str) -> tuple:
    ratings = {}
    valid_review_count = 0
    invalid_review_count = 0
    total_reviews = 0

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        total_reviews += 1
                        review_data = line.strip().split(',')

                        if len(review_data) != 5:
                            invalid_review_count += 1
                            continue

                        customer_id, product_id, review_date, review_rating, review_text = review_data

                        if not check_review_valid(customer_id, product_id, review_date, review_rating, review_text):
                            invalid_review_count += 1
                            continue

                        review_rating = int(review_rating)
                        valid_review_count += 1
                        if product_id in ratings:
                            ratings[product_id].append(review_rating)
                        else:
                            ratings[product_id] = [review_rating]

            except FileNotFoundError as e:
                print(f"File not found: {e}")
            except Exception as e:
                print(f"Unexpected error processing file {file_path}: {e}")

    avg_ratings = {product_id: sum(
        ratings[product_id]) / len(ratings[product_id]) for product_id in ratings}
    return avg_ratings, valid_review_count, invalid_review_count, total_reviews


def check_review_valid(customer_id: str, product_id: str, review_date: str, review_rating: str, review_text: str) -> bool:
    try:
        if not is_valid_date(review_date):
            return False
        if len(customer_id) != 6 or len(product_id) != 10:
            return False
        if not review_rating.isnumeric() or not 1 <= int(review_rating) <= 5:
            return False
        if not review_text:
            return False

        return True
    except Exception as e:
        print(f"Exception in review validation: {e}")
        return False


def is_valid_date(date_str: str) -> bool:
    try:
        parts = date_str.split('-')
        if len(parts) != 3 or len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
            return False
        return True
    except Exception as e:
        print(f"Exception in date validation: {e}")
        return False


def main():
    try:
        directory = os.getcwd()
        avg_ratings, valid_review_count, invalid_review_count, total_reviews = process_files(
            directory)
        top3_products = top_3_products(avg_ratings)
        create_summary(total_reviews, valid_review_count,
                       invalid_review_count, top3_products)

        print("Top 3 Products: ", top3_products)
        print("Valid Reviews: ", valid_review_count)
        print("Invalid Reviews: ", invalid_review_count)

    except Exception as e:
        print(f"Unexpected error in main: {e}")


if __name__ == "__main__":
    main()
