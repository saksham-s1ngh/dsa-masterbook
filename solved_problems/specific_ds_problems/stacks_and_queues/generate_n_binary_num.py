from Queue import MyQueue


# def find_bin(n):

    # Replace this placeholder return statement with your code
    # result = []
    # bin_q = MyQueue()
    # for i in range(1, n+1):
    #     mul = bin = 1
    #     while i > 1:
    #         bin = (i % 2) * mul
    #         mul *= 10
    #         i /= 2
    #     bin_q.enqueue(bin)
    
    # return bin_q

def find_bin(n):

    if n < 1:
        return [1]

    result = []
    bin_q = MyQueue()
    bin_q.enqueue(1) # start with 1 in queue

    for i in range(n):

        # dequeue the front element from the queue
        #   then append it to the resultant list
        result.append(str(bin_q.dequeue()))
        
        # generate new binary nos. by appending '0' and '1' to the dequeued number
        #   which is the last element in the 'result' list
        s1 = result[-1] + "0"
        s2 = result[-1] + "1"

        # enqueue the new generated nos. to the queue
        bin_q.enqueue(s1)
        bin_q.enqueue(s2)

    return result


def main():
    inputs = [1, 3, 5, 9, 11]
    for i in range(len(inputs)):
        print(i+1, ".\tn: ", inputs[i], sep="")
        print("\n\tBinary numbers ", find_bin(inputs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()