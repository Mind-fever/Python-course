#!/usr/bin/env python3

def detect_ranges(L):
    List= sorted(L)
    new_l=[]
    flag=False
    for i in range(len(List)):
        if i==len(List)-1 and flag==True:
            new_l.append((x,List[i]+1))
            continue
        elif i==len(List)-1 and flag==False:
            new_l.append(List[i])
            continue
        if List[i]+1==List[i+1] and flag==False:
            x=List[i]
            flag=True
        if List[i]+1!=List[i+1] and flag==True:
            new_l.append((x,List[i]+1))
            flag=False
        elif List[i]+1!=1+List[i+1] and flag==False:
            new_l.append(List[i])
    return new_l

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
