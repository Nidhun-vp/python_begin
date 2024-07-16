def main():
    c = 0
    n = int(input())  # Read the value of n

    for i in range(n):
        if i % 2 == 0:
            for j in range(i + 1):
                c += 1
                if j < i:
                    print(f"{c}$", end="")
                else:
                    print(f"{c}", end="")
        else:
            c += i
            for j in range(i + 1):
                if j < i:
                    print(f"{c}$", end="")
                else:
                    print(f"{c}", end="")
                c -= 1
            c = c + i + 1  # Reset c to correct value
        print()  # Print newline after each row

if __name__ == "__main__":
    main()
