text = input()
encoded_result = ""
current_char = text[0]
count = 1

for i in range(1, len(text)):
  if text[i] == current_char:
    count += 1
  else:
    encoded_result = encoded_result + current_char + str(count)
    current_char = text[i]
    count = 1

encoded_result = encoded_result + current_char + str(count)

print(encoded_result)