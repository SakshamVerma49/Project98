print('Starting the program')
def swapFileData():
    # Reading data from files
    fileName1 = input("Enter The File Name: ")
    file_a = open(fileName1, 'r')
    data_a = file_a.read()

    fileName2 = input("Enter The File Name: ")
    file_b = open(fileName2, 'r')
    data_b=file_b.read()

# Swapping data to files
    file_a=open(fileName1, 'w')
    file_a.write(data_b)
    
    file_b=open(fileName2,'w')
    file_b.write(data_a)

    file_a.close()
    file_b.close()

swapFileData()
print('End of the program')