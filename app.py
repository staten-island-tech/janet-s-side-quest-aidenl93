## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
# print(data)  # Output the list
total_averages = {}
def averages(x):
    for row in x[1:]:
        name = row[0]
        sales = list(map(int,row[1:])) 
        total_averages[name] = sum(sales) / len(sales)
    return total_averages
averages(data)
def sortedavg(x):
    return dict(sorted(total_averages.items(), key = lambda item: item[1], reverse = True))

ee = (sortedavg(total_averages))
print(ee)

a = sum(total_averages.values())
b = len(total_averages)
bro = a/b
print(bro)
newlist = {}
for x, y in total_averages.items():
    if y < bro*0.8:
        newlist[x] = y
print(f"stores: {newlist}")
assert condition, "error message"
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
assert("dominance") 
assert("dominance")
