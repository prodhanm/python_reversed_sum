nums = [5, 15, 7, 4, 8, 12, 9, 3]

def num_even(nums):
    even_nums = []
    for elem in reversed(nums):
        if elem%2 == 0:
            even_nums.append(elem)
            total = sum(even_nums)
    return total

def main():
    print(num_even(nums))

if __name__ == "__main__":
    main()