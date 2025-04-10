#!/usr/bin/env python3

def merge(L1, L2):
    L=L1+L2
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
    return L

def main():
    L1 = [1, 5, 7]
    L2 = [2, 3, 6]
    print(merge(L1, L2))
    pass

if __name__ == "__main__":
    main()
