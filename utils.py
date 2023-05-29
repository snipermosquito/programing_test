def time_calc(time12):
  import re
  import datetime
  time1 = time12.split("-")[0]
  time2 = time12.split("-")[1]
  time1_sp = re.split('(..)',time1)[1::2]
  time2_sp = re.split('(..)',time2)[1::2]
  year1 = int(time1_sp[0]+time1_sp[1])
  year2 = int(time2_sp[0]+time2_sp[1])
  dt1 = datetime.datetime(year=year1, month=int(time1_sp[2]), day=int(time1_sp[3]), hour=int(time1_sp[4]),minute=int(time1_sp[5]),second=int(time1_sp[6]))
  dt2 = datetime.datetime(year=year2, month=int(time2_sp[2]), day=int(time2_sp[3]), hour=int(time2_sp[4]),minute=int(time2_sp[5]),second=int(time2_sp[6]))
  dt = dt2 - dt1
  return("(" + str(dt) + ")")
