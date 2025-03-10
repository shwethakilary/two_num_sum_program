def sums(no, target):
    for i in range(len(no)):
        for j in range(i+1, len(no)):
            for k in range(j+1, len(no)):
                if no[i]+no[j]+no[k]==target:
                    return [i,j,k]
    return None
            
intp = input("Enter the numbers separated by spaces: ")
no = list(map(int, intp.split()))  # Convert input to a list of integers
target = int(input("Enter the target value: "))

output= sums(no, target)
print(output)