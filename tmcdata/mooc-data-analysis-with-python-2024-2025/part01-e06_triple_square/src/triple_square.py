#!/usr/bin/env python3

def triple(a):
    return a*3

def square(a):
    return a*a

def main():
    for i in range(1,11):
        a=triple(i)
        b=square(i)
        if  b>a:
            break
        print(f"triple({i})=={a} square({i})=={b}")

if __name__ == "__main__":
    main()
