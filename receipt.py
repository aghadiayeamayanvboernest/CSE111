#My creativity in this project includes implementing a 10% discount on product prices if today is Tuesday or Wednesday to encourage weekday shopping, and adding an invitation for customers to complete an online survey at the bottom of the receipt to gather valuable feedback
import csv  # Import the csv module to work with CSV files
from datetime import datetime  # Import datetime module to work with dates and times

store_name = "Ernesto's Daily Groceries"  # Store name

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}  # Initialize an empty dictionary to store the data

    with open(filename, "rt") as csv_file:  # Open the CSV file for reading in text mode
        reader = csv.reader(csv_file)  # Create a CSV reader object
        next(reader)  # Skip the header row
        for row_list in reader:  # Iterate over each row in the CSV file
            if len(row_list) != 0:  # Check if the row is not empty
                key = row_list[key_column_index]  # Use the specified column index as the key
                dictionary[key] = row_list  # Add the row to the dictionary with the key
    return dictionary  # Return the populated dictionary

def main():
    try:
        sales_tax_rate = 0.06  # Define the sales tax rate
        subtotal = 0.0  # Initialize subtotal
        total_items = 0  # Initialize total items count

        # Check for discount based on the day of the week
        current_date_and_time = datetime.now()  # Get the current date and time
        current_day = current_date_and_time.strftime("%A")  # Get the current day of the week
        discount = 0.10 if current_day in ["Tuesday", "Wednesday"] else 0.0  # Apply a 10% discount if today is Tuesday or Wednesday

        dictionary = read_dictionary('products.csv', 0)  # Call read_dictionary to read products.csv and store the result in dictionary
        print()
        print(store_name)  # Print the store name
        print()
        print("Requested Items")  # Print a header for requested items

        with open('request.csv', 'rt') as csv_file:  # Open the request.csv file for reading in text mode
            reader = csv.reader(csv_file)  # Create a CSV reader object
            next(reader)  # Skip the header row

            for row in reader:  # Iterate over each row in the request CSV file
                if len(row) < 2:  # Skip rows that don't have enough columns
                    continue
                product_number = row[0]  # Get the product number from the first column
                quantity = int(row[1])  # Get the quantity from the second column and convert it to an integer
                product = dictionary[product_number]  # Retrieve the product details from the dictionary using the product number
                product_name = product[1]  # Get the product name from the product details
                product_price = float(product[2])  # Get the product price from the product details and convert it to a float

                # Apply discount if applicable
                if discount > 0:
                    product_price -= product_price * discount  # Apply the discount to the product price

                total_items += quantity  # Add the quantity to the total items count
                subtotal += product_price * quantity  # Add the total price of this product to the subtotal

                # Print the product name, quantity, and price in the specified format
                print(f"{product_name}: {quantity} @ ${product_price:.2f}")

        sales_tax = subtotal * sales_tax_rate  # Calculate the sales tax
        total = subtotal + sales_tax  # Calculate the total amount

        print()
        print(f"Number of items: {total_items}")  # Print the total number of items
        print(f"Subtotal: ${subtotal:.2f}")  # Print the subtotal amount
        print(f"Sales Tax: ${sales_tax:.2f}")  # Print the sales tax amount
        print(f"Total: ${total:.2f}")  # Print the total amount
        print()
        print(f"Thank you for shopping at {store_name}")  # Print a thank you message with the store name
        print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))  # Print the current date and time in the specified format
        print()
        print("Please visit our website to complete a survey about your shopping experience!")  # Print a survey invitation
        print("Your feedback is valuable to us.")  # Print a message emphasizing the value of feedback
        print("Survey URL: www.ernestosgroceries.com/survey")  # Print the survey URL
        print()
    except KeyError as key_err:  # Handle KeyError exceptions
        print(f"Error: Unknown product ID in the request.csv {key_err}")  # Print an error message for unknown product IDs
    except FileNotFoundError as not_found_err:  # Handle FileNotFoundError exceptions
        print(f"Error: Missing file {not_found_err}")  # Print an error message for missing files
    except PermissionError as perm_err:  # Handle PermissionError exceptions
        print(f"Error: Permission denied {perm_err}")  # Print an error message for permission errors

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
