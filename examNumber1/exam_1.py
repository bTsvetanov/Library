first_list = []
for i in range(4):
    i = int(input("Въведете цяло число: "))
    first_list.append(i)
print("first list:")
print(first_list)
max_first_list = max(first_list)
min_first_list = min(first_list)
print("Sum of max and min:", max_first_list + min_first_list)
odd_num_count = 0
for num in first_list:
    if num % 2 != 0:
        odd_num_count += 1
print("Count of odd numbers:", odd_num_count)

second_list = []
for n in first_list:
    if n % 5 == 0:
        second_list.append(n)
print("second list:")
print(second_list)

max_second_list = max(second_list)
avr = sum(second_list)/len(second_list)
print("Razlikata mejdu maksimalniq element i sredno aritmeti4niq e:",max_second_list - avr)

second_list.append(second_list[0] + second_list[len(second_list)-1])
print("second list:")
print(second_list)