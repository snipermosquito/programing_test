import sys
import utils
import math

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
    
new_lines = []
sn_time_list = []
sn_list = []
sv_dic = {}
sn_dic = {}
sn_num = 0
num = 0
for line in list:
    sn = ""
    npf = int(line.split("/")[1])
    for i in range(0,math.ceil(npf/8)):
        sn = (sn + "." +  line.split(".")[i]).strip(".")
    if not sn in sn_list:
        sn_list.append(sn)
        sn_dic[sn] = "No" + str(sn_num)
        exec("{} = False".format(sn_dic[sn] + "_check"))
        exec("{} = []".format(sn_dic[sn]))
        sn_num += 1
    sv_dic[line] = sn_dic[sn] + "_" + str(num)
    exec("{} = False".format(sv_dic[line] + "_check"))
    exec("tmp_list = {}".format(sn_dic[sn]))
    if not dic[line] in tmp_list:
        exec("{}.append(sv_dic[line])".format(sn_dic[sn]))
    num += 1
for line in time_list:
    sv = line[0]
    fr = line[1].split("-")[0]
    if line[1].split("-")[1] != "":
        unt = line[1].split("-")[1]
    else:
        unt = "99999999999999"
    new_lines.append([sv,fr,unt])
new_lines = sorted(new_lines, key=lambda x: x[1])
for line in new_lines:
    sn = ""
    npf = int(line[0].split("/")[1])
    for i in range(0,math.ceil(npf/8)):
        sn = (sn + "." +  line[0].split(".")[i]).strip(".")
    now = int(line[1])
    for svs in list:
        sv_No = sv_dic[svs]
        exec("check = {}".format(sv_No + "_check"))
        if check:
            exec("end = {}".format(sv_No + "_end"))
            if int(now) >= int(end):
                exec("{} = False".format(sv_No + "_check"))
    sv_No = sv_dic[line[0]]
    exec("{} = int(line[1])".format(sv_No + "_start"))
    exec("{} = int(line[2])".format(sv_No + "_end"))
    exec("{} = True".format(sv_No + "_check"))
    sn_No = sn_dic[sn]
    sn_check = True
    exec("tmp_list = {}".format(sn_No))
    for svs in tmp_list:
        exec("check = {}".format(svs + "_check"))
        if not check:
            sn_check = False
    if sn_check:
        max = 0
        min = 99999999999999
        for svs in tmp_list:
            exec("start = {}".format(svs + "_start"))
            exec("end = {}".format(svs + "_end"))
            if start > max:
                max = start
            if end < min:
                min = end
                end_check = svs
        exec("{} = False".format(end_check + "_check"))
        if min == 99999999999999:
            max_min = str(max) + "-"
            sn_time_list.append([sn,max_min])
        else:
            max_min = str(max) + "-" + str(min)
            dt = utils.time_calc(max_min)
            sn_time_list.append([sn,max_min,dt])

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

