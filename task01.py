file_one = open("Book1.txt","r")
file_two = open("Book2.txt","r")
file_three = open("Book3.txt","r")


def values_split(file):
    for aline in file:
        values = aline.split()
        return values

def max_value(values):
    for value in values:
        return max(value)

max_results=[max_value(values_split(file_one)),max_value(values_split(file_two)),max_value(values_split(file_three))]

print(max(max_results))

