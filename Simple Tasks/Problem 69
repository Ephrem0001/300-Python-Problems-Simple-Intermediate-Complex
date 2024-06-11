

def read_and_add_numbers(filename):
  try:
    with open(filename, "r") as file:
      first_number = float(file.readline().strip())

      second_number = float(file.readline().strip())

      return first_number + second_number
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None
  except ValueError:
    print(f"Error: Invalid number format in '{filename}'.")
    return None


filename = "numbers.txt"
sum_of_numbers = read_and_add_numbers(filename)

if sum_of_numbers is not None:
  print(f"The sum of the numbers in '{filename}' is: {sum_of_numbers}")
