import sys

if len(sys.argv) == 2:
    output = sys.argv[1]
else:
    output = ""
log = "log.txt"
list = []
time_list = []
dic = {}
toc_dic = {}
num = 0
with open(log,'r') as f:
    lines = f.readlines()
for line in lines:
    if line.isspace():
            break
    elif not line.split(",")[1] in list:
        list.append(line.split(",")[1])
        num += 1
        dic[line.split(",")[1]] = "No" + str(num)
        toc_dic[line.split(",")[1]] = "No" + str(num) + "_TOCheck"
        exec("{} = False".format(toc_dic[line.split(",")[1]]))
        #exec("print({})".format(dic[line.split(",")[1]] + "_TOCheck"))
    exec("var = {}".format(toc_dic[line.split(",")[1]]))
    if var:
        if line.split(",")[2].strip() != "-":
            exec("{} = False".format(toc_dic[line.split(",")[1]]))
            exec("recov_time = {} + '-' + str(line.split(',')[0])".format(dic[line.split(",")[1]] + "_time"))
            dt = utils.time_calc(recov_time)
            time_list.append([line.split(",")[1],recov_time,dt])
    elif line.split(",")[2].strip() == "-":
        exec("{} = True".format(toc_dic[line.split(",")[1]]))
        exec("{} = line.split(',')[0]".format(dic[line.split(',')[1]] + '_time'))
for i in list:
    exec("var = {}".format(toc_dic[i]))
    if var:
        exec("recov_time = {} + '-'".format(dic[i] + "_time"))
        time_list.append([i,recov_time])

if output == "":
    for i in time_list:
        if i[1].split("-")[1] != "":
            end = " until " + i[1].split("-")[1] + ". " + i[2]
        else:
            end = "."
        print(i[0]  + ": out of order from " + i[1].split("-")[0] + end)

else:
    with open(output,'w') as f:
        for i in time_list:
            if i[1].split("-")[1] != "":
                end = " until " + i[1].split("-")[1] + ". " + i[2] + "\n"
            else:
                end = ".\n"
            f.write(i[0]  + ": out of order from " + i[1].split("-")[0] + end)


