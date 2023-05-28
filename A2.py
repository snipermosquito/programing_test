import sys

N = int(sys.argv[1])
log = "log.txt"
list = []
time_list = []
dic = {}
toc_dic = {}
c_dic = {}
num = 0
with open(log,'r') as f:
    lines = f.readlines()
for line in lines:
    if line.isspace():
        break
    elif not line.split(",")[1] in list:
        list.append(line.split(",")[1])
        dic[line.split(",")[1]] = "No" + str(num)
        toc_dic[line.split(",")[1]] = "No" + str(num) + "_TOCheck"
        c_dic[line.split(",")[1]] = "c_No" + str(num)
        exec("{} = False".format(toc_dic[line.split(",")[1]]))
        exec("{} = 0".format(c_dic[line.split(",")[1]]))
        num += 1
    exec("var = {}".format(toc_dic[line.split(",")[1]]))
    if var:
        if line.split(",")[2].strip() != "-":
            exec("{} = False".format(toc_dic[line.split(",")[1]]))
            exec("recov_time = {} + '-' + str(line.split(',')[0])".format(dic[line.split(",")[1]] + "_time"))
            exec("c_var = {}".format(c_dic[line.split(",")[1]]))
            if c_var >= N:
                time_list.append([line.split(",")[1],recov_time])
            exec("{} = 0".format(c_dic[line.split(",")[1]]))
        else:
            exec("{} += 1".format(c_dic[line.split(",")[1]]))
    elif line.split(",")[2].strip() == "-":
        exec("{} = True".format(toc_dic[line.split(",")[1]]))
        exec("{} = line.split(',')[0]".format(dic[line.split(',')[1]] + '_time'))
        exec("{} = 1".format(c_dic[line.split(",")[1]]))
for i in list:
    exec("var = {}".format(toc_dic[i]))
    exec("c_var = {}".format(c_dic[i]))
    if var and c_var >= N:
        exec("recov_time = {} + '-'".format(dic[i] + "_time"))
        time_list.append([i,recov_time])

for i in time_list:
    if i[1].split("-")[1] != "":
        end = " until " + i[1].split("-")[1] + "."
    else:
        end = "."
    print(i[0]  + ": out of order from " + i[1].split("-")[0] + end)


