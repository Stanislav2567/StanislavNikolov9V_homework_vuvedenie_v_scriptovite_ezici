encoded_text = input()

decoded_result = ""

i = 0

while i < len(encoded_text):
  char = encoded_text[i]
  count = int(encoded_text[i + 1])

  decoded_result = decoded_result + (char * count)

  i += 2

print(decoded_result)