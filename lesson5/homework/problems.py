# Problem 1
# Search the list and print whether "tiger" is found.
animals = ["cat", "dog", "tiger", "lion"]

if "tiger" in animals:
    print("tiger found")
else:
    print("tiger not found")
# Problem 2
# Count how many words have length greater than 5.
words = ["python", "cat", "elephant", "dog", "computer"]
count = 0
for word in words:
    if len(word) > 5:
                count += 1
print(count)
# Problem 3
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
total_sum = 0
for number in numbers:
    if number >25:
          total_sum += number
print(total_sum)
# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
biggest = numbers[0]
for number in numbers:
    if number >biggest:
      biggest = number
print(biggest)
# Problem 5
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
biggest = 0
for number in numbers:
     if number > 100 and number > biggest:
        biggest = number
print(biggest)