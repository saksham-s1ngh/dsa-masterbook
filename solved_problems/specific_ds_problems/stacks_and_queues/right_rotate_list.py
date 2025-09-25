from collections import deque

def right_rotate(arr, k):
    
    de = deque(arr)
    for _ in range(k % len(arr)):
        last_el = de.pop()
        de.appendleft(last_el)
    
    return list(de)


def main():
    inputs = [
        ([10, 20, 30, 40, 50]),  
        ([1, -2, 3, 4, 5]),  
        ([-1, 90, -90, 4, 6]),      
        ([3, 6, 9, -12]),          
        ([-100, -200, -300])         
    ]
    k= [3, 2, 6, 2, 1]
    
    for i in range(len(inputs)):
        print(i + 1, ".\tnums: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tRotated list: ", right_rotate(inputs[i], k[i]), sep="")
        print("-" * 70)

if __name__ == "__main__":
    main()

