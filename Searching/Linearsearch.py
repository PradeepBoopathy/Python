from timeit import default_timer as timer
import random
def Linearsearch(elements,searchvalue):
    ind = []
    for i in range(len(elements)):
        if elements[i] == searchvalue:
            ind.append(i)
    return 'Not Found' if len(ind) == 0 else ('Found at index:', ind)

if __name__ == '__main__':
    elements = []
    for i in range(0, 10000000):
        n = random.randint(1, 10000)
        elements.append(n)
    elements.append(999)
    print(len(elements))
    elements.sort()
    newelements = list(set(elements))
    print(len(newelements))
    start = timer()
    search = 999
    l = Linearsearch(newelements, search)
    print(l)
    end = timer()
    print("Time taken:", end - start)