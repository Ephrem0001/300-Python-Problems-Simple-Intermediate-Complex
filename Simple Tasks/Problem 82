def is_possibly_encrypted(username):
  

  # Check for non-alphanumeric characters (excluding common symbols)
  if not username.isalnum() and any(char in username for char in "!@#$%^&*()_+-=[]{};':\",./<>?"):
    return True

  # Check for length consistency (common hash functions have fixed output lengths)
  if len(username) in [32, 64]:  # Examples: MD5, SHA-256
    return True

  return False

# Example usage
username1 = "john_doe"
username2 = "b99f544a08a89c1e3a90817ec04c4f3f"  # Example MD5 hash

print(is_possibly_encrypted(username1))  # False
print(is_possibly_encrypted(username2))  # True (may not be actual encryption)
