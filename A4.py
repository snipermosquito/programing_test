import sys
import math
import utils

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
sn_time_list = []
sn_list = []
dic = {}
toc_dic = {}
c_dic = {}
ol_dic = {}
olc_dic = {}
sn_dic = {}
num = 0
sn_num = 0
with open(log,'r') as f:
    lines = f.readlines()
for line in lines:
    if line.isspace():
        break
    sn = ""
    npf = int(line.split(",")[1].split("/")[1])
    for i in range(0,math.ceil(npf/8)):
        sn = (sn + "." +  line.split(",")[1].split(".")[i]).strip(".")
    if not line.split(",")[1] in list:
        if not sn in sn_list:
            sn_list.append(sn)
            sn_dic[sn] = "No" + str(sn_num)
            exec("{} = False".format(sn_dic[sn] + "_check"))
            exec("{} = []".format(sn_dic[sn]))
            sn_num += 1
        list.append(line.split(",")[1])
        dic[line.split(",")[1]] = sn_dic[sn] + "_" + str(num)
        toc_dic[line.split(",")[1]] = sn_dic[sn] + str(num) + "_TOCheck"
        c_dic[line.split(",")[1]] = "c_" + sn_dic[sn] + "_" + str(num)
        ol_dic[line.split(",")[1]] = "ol_" + sn_dic[sn] + str(num)
        olc_dic[line.split(",")[1]] = sn_dic[sn] + str(num) + "_OLCheck"
        exec("{} = False".format(toc_dic[line.split(",")[1]]))
        exec("{} = 0".format(c_dic[line.split(",")[1]]))
        exec("{} = []".format(ol_dic[line.split(",")[1]]))
        exec("{} = False".format(olc_dic[line.split(",")[1]]))
        exec("tmp_list = {}".format(sn_dic[sn]))
        if not dic[line.split(",")[1]] in tmp_list:
            exec("{}.append(dic[line.split(',')[1]])".format(sn_dic[sn]))
        num += 1
for line in lines:
    if line.isspace():
        break
    sn = ""
    npf = int(line.split(",")[1].split("/")[1])
    for i in range(0,math.ceil(npf/8)):
        sn = (sn + "." +  line.split(",")[1].split(".")[i]).strip(".")
    exec("var = {}".format(toc_dic[line.split(",")[1]]))
    if var:
        if line.split(",")[2].strip() != "-":
            exec("{} = False".format(toc_dic[line.split(",")[1]]))
            exec("recov_time = {} + '-' + str(line.split(',')[0])".format(dic[line.split(",")[1]] + "_time"))
            dt = utils.time_calc(recov_time)
            exec("c_var = {}".format(c_dic[line.split(",")[1]]))
            if c_var >= N:
                time_list.append([line.split(",")[1],recov_time,dt])
                exec("{} = 0".format(c_dic[line.split(",")[1]]))
        else:
            exec("{} += 1".format(c_dic[line.split(",")[1]]))
    elif line.split(",")[2].strip() == "-":
        exec("{} = True".format(toc_dic[line.split(",")[1]]))
        exec("{} = line.split(',')[0]".format(dic[line.split(',')[1]] + '_time'))
        exec("{} = 1".format(c_dic[line.split(",")[1]]))
    exec("tmp_list = {}".format(sn_dic[sn]))
    exec("sn_E_check = {}".format(sn_dic[sn] + "_check"))
    if sn_E_check:
        if line.split(",")[2].strip() != "-":
            exec("{} = False".format(sn_dic[sn] + "_check"))
            sn_max = 0
            for i in tmp_list:
                i += "_time"
                exec("sn_tmp_time = int({})".format(i))
                if sn_max < sn_tmp_time:
                        sn_max = sn_tmp_time
            recov_time = str(sn_max) + '-' + str(line.split(',')[0])
            dt = utils.time_calc(recov_time)
            sn_time_list.append([sn,recov_time,dt])
    else:
        for i in tmp_list:
            i = "c_" + i
            exec("j = {}".format(i))
            if j >= m:
                exec("{} = True".format(sn_dic[sn] + "_check"))
            else:
                exec("{} = False".format(sn_dic[sn] + "_check"))
                break
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
                    dt = utils.time_calc(ol_recov_time)
                    ol_time_list.append([line.split(",")[1],ol_recov_time,dt])
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
    exec("tmp_list = {}".format(sn_dic[sn]))
    exec("sn_E_check = {}".format(sn_dic[sn] + "_check"))
    if sn_E_check:
        exec("{} = False".format(sn_dic[sn] + "_check"))
        sn_max = 0
        for i in tmp_list:
            i += "_time"
            exec("sn_tmp_time = int({})".format(i))
            if sn_max < sn_tmp_time:
                sn_max = sn_tmp_time
        recov_time = str(sn_max) + '-'
        sn_time_list.append([sn,recov_time])

if output == "":
    print("[timeout]")
    for i in time_list:
        if i[1].split("-")[1] != "":
            end = " until " + i[1].split("-")[1] + ". " + i[2]
        else:
            end = "."
        print(i[0]  + ": out of order from " + i[1].split("-")[0] + end)
    print("[overload]")
    for i in ol_time_list:
        if i[1].split("-")[1] != "":
            end = " until " + i[1].split("-")[1] + ". " + i[2]
        else:
            end = "."
        print(i[0]  + ": under heavy load from " + i[1].split("-")[0] + end)
    print("[subnet malfunction]")
    for i in sn_time_list:
        l = 4 - len(i[0].split("."))
        i[0] += ".x"*l
        if i[1].split("-")[1] != "":
            end = " until " + i[1].split("-")[1] + ". " + i[2]
        else:
            end = "."
        print(i[0]  + ": faulty subnet from " + i[1].split("-")[0] + end)
else:
    with open(output,'w') as f:
        f.write("N = " + str(N) + ", m = " + str(m) + ", t = " + str(t) + "\n")
        f.write("[timeout]\n")
        for i in time_list:
            if i[1].split("-")[1] != "":
                end = " until " + i[1].split("-")[1] + ". " + i[2] + "\n"
            else:
                end = ".\n"
            f.write(i[0]  + ": out of order from " + i[1].split("-")[0] + end)
        f.write("[overload]\n")
        for i in ol_time_list:
            if i[1].split("-")[1] != "":
                end = " until " + i[1].split("-")[1] + ". " + i[2] + "\n"
            else:
                end = ".\n"
            f.write(i[0]  + ": under heavy load from " + i[1].split("-")[0] + end)
        f.write("[subnet malfanction]\n")
        for i in sn_time_list:
            l = 4 - len(i[0].split("."))
            i[0] += ".x"*l
            if i[1].split("-")[1] != "":
                end = " until " + i[1].split("-")[1] + ". " + i[2] + "\n"
            else:
                end = ".\n"
            f.write(i[0]  + ": faulty subnet from " + i[1].split("-")[0] + end)


