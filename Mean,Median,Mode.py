import csv
from collections import Counter

with open('height-weight.csv',newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

def Mean():
    new_data = []
    for i in range(len(file_data)) : 
        n_num = file_data[i][2]
        new_data.append(float(n_num))

    n = len(new_data)
    total = 0
    for i in new_data:
        total += i

    mean = total/n
    print("Mean : " + str(mean))

def Median():
    new_data = []
    for i in range(len(file_data)) : 
        n_num = file_data[i][2]
        new_data.append(float(n_num))

    n = len(new_data)
    new_data.sort()

    if n%2 == 0 :
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2 - 1])
        median = (median1+median2)/2
    else :
        median = new_data[n//2]

    print("Median : " + str(median))

def Mode():
    new_data = []
    for i in range(len(file_data)) : 
        n_num = file_data[i][2]
        new_data.append(float(n_num))

    data = Counter(new_data)
    modeDataForRange = {
        "75-85" : 0,
        "85-95" : 0,
        "95-105" : 0,
        "105-115" : 0,
        "115-125" : 0,
        "125-135" : 0,
        "135-145" : 0,
        "145-155" : 0,
        "155-165" : 0,
        "165-175" : 0,
    }
    for height, occurence in data.items():
        if 75 < float(height) < 85:
            modeDataForRange["75-85"] += occurence
        elif 85 < float(height) < 95:
            modeDataForRange["85-95"] += occurence
        elif 95 < float(height) < 105:
            modeDataForRange["95-105"] += occurence
        elif 105 < float(height) < 115:
            modeDataForRange["105-115"] += occurence
        elif 115 < float(height) < 125:
            modeDataForRange["115-125"] += occurence
        elif 125 < float(height) < 135:
            modeDataForRange["125-135"] += occurence
        elif 135 < float(height) < 145:
            modeDataForRange["135-145"] += occurence
        elif 145 < float(height) < 155:
            modeDataForRange["145-155"] += occurence
        elif 155 < float(height) < 165:
            modeDataForRange["155-165"] += occurence
        elif 165 < float(height) < 175:
            modeDataForRange["165-175"] += occurence

    mode_range, mode_occurence = 0, 0

    for Range, occurence in modeDataForRange.items():   
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(Range.split("-")[0]), int(Range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode : {mode:2f}")

def main():
    Mean()
    Median()
    Mode()

main()
