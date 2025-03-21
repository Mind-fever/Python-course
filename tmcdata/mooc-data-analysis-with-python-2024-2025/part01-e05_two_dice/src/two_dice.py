#!/usr/bin/env python3

def main():
    for i in range(1,7):
        for x in range(1,7):
            if i+x==5:
                print(f"({i},{x})")
if __name__ == "__main__":
    main()
