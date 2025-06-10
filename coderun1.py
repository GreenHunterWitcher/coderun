input_str = input()
numbers = [int(num) for num in input_str.replace(',', ' ').split()]
if len(numbers) != 3:
    print("Please enter exactly 3 numbers!")
else:
    sorted_nums = sorted(numbers)
    print(f"{sorted_nums[1]}")