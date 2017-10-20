infile = open("running-config.cfg", "r")
outfile = open("running-config.cfg", "w")

aline = infile.readline()
while aline:
    items = aline.split()
    for n in len(items):
        dataline = items[n]
        if item[n]== str(192):
            item[n]=item[n].replace("192","172") 
        outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()

