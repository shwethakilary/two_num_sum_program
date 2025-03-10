def two_sum(nums, target):
    for i in range(len(nums)):  # Iterate over each element
        for j in range(i + 1, len(nums)):  # Check remaining elements
            if nums[i] + nums[j] == target:
                return [i, j]  # Return indices of the two numbers
    print("No solution found")  # Return empty if no solution found

# Taking input from user
inp = input("Enter the numbers separated by spaces: ")
nums = list(map(int, inp.split()))  # Convert input to a list of integers
target = int(input("Enter the target value: "))

# Calling function and printing output
output = two_sum(nums, target)
print("Output:", output)
