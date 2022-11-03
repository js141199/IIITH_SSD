import csv
import errno

fileData = []

def loadCSVFile():
    try:
        with open("lab_11_data.csv", "r") as file:
            data = list(csv.reader(file, delimiter=","))
            file.close()
            for info in data:
                info[1] = info[1].replace(',', '')
                info[2] = info[2].replace(',', '')
                info[3] = info[3].replace(',', '')
                fileData.append(info[0:len(info) - 6])
    except FileNotFoundError as e:
        print(errno,e)
    
    fileData.remove(fileData[0])

loadCSVFile()

# using filter function
filtered = filter(lambda entry: float(entry[-1]) > -3, fileData)

fileData = (list(list(filtered)))

openList = []
highList = []
lowList = []

def generateList():
    for data in fileData:
        openList.append(float(data[1]))
        highList.append(float(data[2]))
        lowList.append(float(data[3]))

generateList()

ls = []
ls.append(openList)
ls.append(highList)
ls.append(lowList)
avg_list = list(map(lambda x : sum(x) / len(x),ls))

f = open("avg_output.txt","w")
f.write("open " + str(avg_list[0]) + "\n")
f.write("high " + str(avg_list[1]) + "\n")
f.write("low " + str(avg_list[2]))
f.close()

def display_stocks():
    f1 = open("stock_output.txt","w")
    ch = input()[0]
    for data in fileData:
        if ch == data[0][0]:
            for x in data:
                f1.write(x + " ")
            f1.write("\n")
    f1.close()
display_stocks()
