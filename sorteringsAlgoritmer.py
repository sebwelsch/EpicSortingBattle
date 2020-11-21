import random, math, sys


# def bogoSort(items):
#     # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
#     items = items.copy()
#     isSorted = None # Boolean til markering af, om listen er sorteret
#     attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
#     while not isSorted:
#         attempts += 1
#         if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
#             print('Afbryder på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
#             items.sort()
#             return items
#         random.shuffle(items) # Bland alle elementer helt tilfældigt
#         isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
#         # ...og prøver i denne løkke at bevise det modsatte
#         for index in range(len(items)-1):
#             if items[index] > items[index+1]:
#                 isSorted = False
#                 break # Bryd løkken hvis et eneste element er forkert sorteret
#     print('Sorteret efter {} forsøg'.format(attempts))
#     return items


def InsertionSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    for i in range(0,len(items)): #En pointer der gå fra venstre til højre i hele listen
        for j in range(i,0,-1): #Liste der går fra hvorend i er nået til og tilbage til 0
            if items[j-1] > items[j]:
                items[j-1], items[j] = items[j], items[j-1] #Dette bytter om på værdierne på pladsen j og j-1
    return items


def SelectionSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    for i in range(len(items)): #En pointer der gå fra venstre til højre i hele listen
        indexMin = i #Starter med at sætte den mindste værdi til i
        for j in range(i+1, len(items)): #Herefter tjekker denne løkke om der er nogle mindre tal til højre for i i listen
            if items[j] < items[indexMin]:
                indexMin = j
        items[i], items[indexMin] = items[indexMin], items[i] #Hvis der er en mindre værdi bliver værdierne byttet om.
    return items


# def MergeSort(items):
#     items = items.copy()
#     holder = []
#     for i in range(0,len(items)):
#         if i % len(items)/2 == 0:
#             for j in range(0,int(len(items)/2)):
#                 holder.append(items[j])
#                 print(holder)
#             if holder < len(items):
#                 items[len(items)]
#     return items

def MergeSort(items):
    items = items.copy()
    if len(items) > 1:
        mid = len(items)//2 #Jeg bruger "//" for ikke at få decimaler
        arr1 = items[:mid] #items[:mid] = items[0,mid]
        arr2 = items[mid:]#items[mid:] = items[mid,len(items)]
        
        print(arr1, arr2)

        MergeSort(arr1) #Kører funktionen igennem med to nye arrays som er items splittet op i 2
        MergeSort(arr2)

        a1 = a2 = i = 0
        while a1 < len(arr1) and a2 < len(arr2):
            if arr1[a1] < arr2[a2]:
                items[i] = arr1[a1]
                a1 += 1
            else:
                items[i] = arr2[a2]
                a2 += 1
            i += 1

            print(arr1, arr2, items)

            while a1 < len(arr1):
                items[i] = arr1[a1]
                a1 += 1
                i += 1

            while a2 < len(arr2):
                items[i] = arr2[a2]
                a2 += 1
                i += 1
    return items


if __name__ == '__main__':
    for i in range(2):
        listen = list(range(1, 8))
        random.shuffle(listen)
        sorteret = MergeSort(listen)
        print('Shuffled:\t', listen)
        print('Sorted:\t\t', sorteret)
        print('==============================================================')
