import sys

if len(sys.argv) == 5:
    output = sys.argv[4]
else:
    output = ""
N = int(sys.argv[1])
m =int(sys.argv[2])
t = int(sys.argv[3])
log = "log.txt"
list = []
time_list = []
ol_time_list = []
dic = {}
toc_dic = {}
c_dic = {}
ol_dic = {}
olc_dic = {}
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
        ol_dic[line.split(",")[1]] = "ol_No" + str(num)
        olc_dic[line.split(",")[1]] = "No" + str(num) + "_OLCheck"
        exec("{} = False".format(toc_dic[line.split(",")[1]]))
        exec("{} = 0".format(c_dic[line.split(",")[1]]))
        exec("{} = []".format(ol_dic[line.split(",")[1]]))
        exec("{} = False".format(olc_dic[line.split(",")[1]]))
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
    exec("{}.append([line.split(',')[0],line.split(',')[2].strip()])".format(ol_dic[line.split(',')[1]]))
    exec("length = len({})".format(ol_dic[line.split(',')[1]]))
    if length == m:
        exec("tmp_list = {}".format(ol_dic[line.split(',')[1]]))
        M = 0
        sum = 0
        for i in tmp_list:
            if i[1] != "-":
                M += 1
                sum += int(i[1])
        if M != 0:
            avg = sum/M
            if avg > t:
                exec("check = {}".format(olc_dic[line.split(",")[1]]))
                if not check:
                    exec("{} = True".format(olc_dic[line.split(",")[1]]))
                    exec("{} = tmp_list[0][0]".format(dic[line.split(',')[1]] + '_ol_time'))
            else:
                exec("check = {}".format(olc_dic[line.split(",")[1]]))
                if check:
                    exec("{} = False".format(olc_dic[line.split(",")[1]]))
                    exec("ol_recov_time = {} + '-' + str(line.split(',')[0])".format(dic[line.split(",")[1]] + "_ol_time"))
                    ol_time_list.append([line.split(",")[1],ol_recov_time])
        exec("{}.pop(0)".format(ol_dic[line.split(',')[1]]))
for i in list:
    exec("var = {}".format(toc_dic[i]))
    exec("c_var = {}".format(c_dic[i]))
    if var and c_var >= N:
        exec("recov_time = {} + '-'".format(dic[i] + "_time"))
        time_list.append([i,recov_time])
    exec("check = {}".format(olc_dic[i]))
    if check:
        exec("ol_recov_time = {} + '-'".format(dic[i] + "_ol_time"))
        ol_time_list.append([i,ol_recov_time])
if output == "":
    print("[timeout]")
    for i in time_list:
        if i[1].split("-")[1] != "":
            end = " until " + i[1].split("-")[1] + "."
        else:
            end = "."
        print(i[0]  + ": out of order from " + i[1].split("-")[0] + end)
    print("[overload]")
    for i in ol_time_list:
        if i[1].split("-")[1] != "":
            end = " until " + i[1].split("-")[1] + "."
        else:
            end = "."
        print(i[0]  + ": under heavy load from " + i[1].split("-")[0] + end)
else:
    with open(output,'w') as f:
        f.write("[timeout]\n")
        for i in time_list:
            if i[1].split("-")[1] != "":
                end = " until " + i[1].split("-")[1] + ".\n"
            else:
                end = ".\n"
            f.write(i[0]  + ": out of order from " + i[1].split("-")[0] + end)
        f.write("[overload]\n")
        for i in ol_time_list:
            if i[1].split("-")[1] != "":
                end = " until " + i[1].split("-")[1] + ".\n"
            else:
                end = ".\n"
            f.write(i[0]  + ": under heavy load from " + i[1].split("-")[0] + end)
    
