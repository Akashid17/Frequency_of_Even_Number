
def EvenCount(iArr):

    iCount = 0

    for y in range(0,len(iArr)):

        if iArr[y] % 2 == 0:
            iCount += 1

    return iCount
            
def main():

    print("Enter Count of Elements")

    iSize = int(input())

    iElements = [0]*iSize

    if len(iElements) == 0:
        print("Unable to Allocate Memory")
        return

    print("Enter ",iSize," Elements")

    for x in range (0,iSize):
        iElements[x] = int(input())

    iResult = EvenCount(iElements)

    print("Frequency of Even Number = ",iResult)

if __name__ == "__main__":
    main()