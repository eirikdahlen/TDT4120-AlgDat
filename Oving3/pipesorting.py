#!/usr/bin/python3

from sys import stdin

#Quicksort
def sort_list(A):
    if len(A) < 2: return A
    else:
        pivot = A.pop()
        smaller, bigger = [], []
        for i in A:
            if i <= pivot:
                smaller.append(i)
            else:
                bigger.append(i)
        return sort_list(smaller) + [pivot] + sort_list(bigger)

def find(A, lower, upper):
    minOutput = binarySearch(A, lower)
    maxOutput = binarySearch(A, upper)
    if A[minOutput] > lower:
        minOutput -= 1
    if A[maxOutput] < upper:
        maxOutput += 1
    if upper > A[-1]:
        maxOutput = len(A) - 1
    if lower < A[0]:
        minOutput = 0
    return [A[minOutput], A[maxOutput]]


def binarySearch(A, value):
    start = 0
    slutt = len(A) - 1
    while True:
        if slutt < start:
            break
        mid = (start + slutt)//2
        if value == A[mid]:
            return mid
        elif value < A[mid]:
            slutt = mid - 1
        else:
            start = mid + 1
    return mid


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
