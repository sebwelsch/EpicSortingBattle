import random, math, sys

def bogoSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    isSorted = None # Boolean til markering af, om listen er sorteret
    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
    while not isSorted:
        attempts += 1
        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
            print('Afbryder på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
            items.sort()
            return items
        random.shuffle(items) # Bland alle elementer helt tilfældigt
        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
        # ...og prøver i denne løkke at bevise det modsatte
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                isSorted = False
                break # Bryd løkken hvis et eneste element er forkert sorteret
    print('Sorteret efter {} forsøg'.format(attempts))
    return items

def InsertionSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    for i in range(0,len(items)):
        for j in range(i,0,-1):
            if items[j-1] > items[j]:
                save = items[j-1]
                items[j-1] = items[j]
                items[j] = save
    return items


def SelectionSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    print(items)
    for i in range(0,len(items)):
        print('i',i)
        for j in range(i+1, len(items)):
            print('j',j)
            if items[j] < items[i]:
                save = items[j]
                print('save er',save)
                indexj = j
                if items[j] < save:
                    items[j] = save
                    indexj = j
                    print('save er ',save)
                    print('indexj er ',indexj)
            else:
                save = items[i]
                indexj = i
        items[indexj]=items[i]
        items[i] = save
    return items

def MergeSort(items):
    items = items.copy()
    holder = [None] * len(items)


if __name__ == '__main__':
    for i in range(2):
        listen = list(range(1, 8))
        random.shuffle(listen)
        sorteret = MergeSort(listen)
        print('Shuffled:\t', listen)
        print('Sorted:\t\t', sorteret)
        print('==============================================================')
