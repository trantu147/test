def total_sum(s):
    total = 0
    for num in (s):
        total += int(num)
    return total

def main():
    s = input("Please input a series of number without space: ")
    print(total_sum(s))

main()
