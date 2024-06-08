def binary_to_decimal(binary_number):
  """Converts a binary number (string) to its decimal equivalent."""
  decimal_value = 0
  for i, digit in enumerate(binary_number[::-1]):  # Iterate through digits in reverse order
    decimal_value += int(digit) * 2**i  # Multiply digit by its corresponding power of 2 and add

  return decimal_value

# Example usage
binary_string = "1101"
decimal = binary_to_decimal(binary_string)
print(f"{binary_string} in decimal: {decimal}")
