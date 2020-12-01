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
    for i in range(0,len(items)): # En pointer der gå fra venstre til højre i hele listen
        for j in range(i,0,-1): # Liste der går fra hvorend i er nået til og tilbage til 0
            if items[j-1] > items[j]:
                items[j-1], items[j] = items[j], items[j-1] #Dette bytter om på værdierne på pladsen j og j-1
    return items



def SelectionSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    for i in range(len(items)): # En pointer der går fra venstre til højre i hele listen
        indexMin = i # Starter med at sætte den mindste værdi til i
        for j in range(i+1, len(items)): # Herefter tjekker denne løkke om der er nogle mindre tal til højre for i i listen
            if items[j] < items[indexMin]:
                indexMin = j
        items[i], items[indexMin] = items[indexMin], items[i] #Hvis der er en mindre værdi bliver værdierne byttet om.
    return items



def MergeSort(items):
    items = items.copy()
    if len(items) > 1:
        mid = len(items)//2 # Jeg bruger "//" for ikke at få decimaler
        arr1 = items[:mid] # items[:mid] = items[0,mid]
        arr2 = items[mid:]# items[mid:] = items[mid,len(items)]

        MergeSort(arr1) # Kører funktionen igennem med to nye arrays som er items splittet op i 2
        MergeSort(arr2)

        out = [] #laver en ny tom liste.
        while len(out) < len(items): #Og holder en løkke igang så længe out listen er kortere end den originale liste

            if len(arr1) > 2: #Det grimme fiks der gør at hvis længden af listen er 2 så skal den bytte talene rundt.
                arr1 = MergeSort(arr1)
            elif len(arr1) == 2 and arr1[0] > arr1[1]:
                arr1[0], arr1[1] = arr1[1], arr1[0]

            if len(arr2) > 2:
                arr2 = MergeSort(arr2)
            elif len(arr2) == 2 and arr2[0] > arr2[1]:
                arr2[0], arr2[1] = arr2[1], arr2[0] #Fikset går her til

            if len(arr1) > 0 and len(arr2) > 0: #Så længe der er noget i listerne
                if arr1[0] < arr2[0]: #Hvis array 1 er mindre end array 2
                    out.append(arr1.pop(0)) #Sæt den første værdi af array 1 ind i out listen
                else:
                    out.append(arr2.pop(0)) #ellers sæt den første værdi af array 2 ind i out listen
            else: #Hvis den ene af listerne har ramt nul skal resten af den anden liste ind
                if len(arr1) == 0: #Hvis array 1 er tom
                    out.append(arr2.pop(0)) #Sæt array 2 ind
                elif len(arr2) == 0: #Repeat men med array 2
                    out.append(arr1.pop(0))
        return out



def BubbleSort(items):
    items = items.copy() # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    for i in range(len(items)): # En pointer der går fra venstre til højre i hele listen
        for j in range(0, len(items)-i-1): # Liste der går fra plads 0 og ?
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j] # Bytter om på værdierne hivs j er større end j+1
    return items



if __name__ == '__main__':
    for i in range(1):
        listen = list(range(1, 8))
        random.shuffle(listen)
        sorteret = MergeSort(listen)
        print('Shuffled:\t', listen)
        print('Sorted:\t\t', sorteret)
        print('==============================================================')
