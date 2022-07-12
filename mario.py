n = int(input("enter number of height: "))
x = int(input("enter number of width: "))
#for _ in range(n):
#    print("#")

def main():
    print_column(n)

def print_column(height):
    for _ in range(height):
        print("#" * x)

main()