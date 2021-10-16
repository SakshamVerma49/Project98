print("Starting The Program")

def swapFileData():
    #Reading Data From Random Files
    fileName1 = input("Enter The File Name")
    file_a = open(fileName1, 'w')
    data_a = file_a.read()

    fileName2 = input("Enter The File Name")
    file_b = open(fileName2, 'w')
    data_b = file_b.read()