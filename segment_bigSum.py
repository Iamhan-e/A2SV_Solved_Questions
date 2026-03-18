import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    s = int(input_data[1])
    a = list(map(int, input_data[2:]))

    count = 0
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += a[right]
        while current_sum >= s:
            count += (n - right)
            current_sum -= a[left]
            left += 1

    sys.stdout.write(str(count) + '\n')