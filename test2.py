def count_equal_color_subsets(arr):
    from collections import Counter

    # Count the occurrences of each color
    color_count = Counter(arr)
    total_r = color_count['r']
    total_b = color_count['b']
    total_g = color_count['g']

    # The number of each color must be the same for valid subsets
    if total_r != total_b or total_b != total_g:
        return 0

    valid_splits = 0
    n = len(arr)

    # Iterate over possible lengths of the subsets
    for subset_size in range(1, n + 1):
        if (total_r * subset_size) % n == 0:
            target_r = (total_r * subset_size) // n
            target_b = (total_b * subset_size) // n
            target_g = (total_g * subset_size) // n

            running_r = 0
            running_b = 0
            running_g = 0

            for i in range(n):
                if arr[i] == 'r':
                    running_r += 1
                elif arr[i] == 'b':
                    running_b += 1
                elif arr[i] == 'g':
                    running_g += 1

                # Check if we have a valid subset
                if (i + 1) % subset_size == 0:
                    if running_r == target_r and running_b == target_b and running_g == target_g:
                        valid_splits += 1
                    running_r = running_b = running_g = 0

    return valid_splits

print(count_equal_color_subsets(['r', 'r', 'b', 'b', 'g', 'g']))  # Output: 1
print(count_equal_color_subsets(['r', 'r', 'b', 'b', 'g']))       # Output: 0
print(count_equal_color_subsets(['r', 'b', 'g', 'g', 'b', 'r']))   # Output: 3
