#Class 第一個字大寫
#數字符號通常全部大寫
 print("Hello Python!")

 PI = 3.14   
 DAY_OF_YEAR = 365
 first_name = 'Bary'
 last_name = "Fu"

 print(PI)
 print(DAY_OF_YEAR / 3)   #會跑出浮點數而非整數
 print(first_name, last_name)

 print(first_name == "Bary")   # == 比較first name跟"字串內容"是否相同 

 print("day" in "Friday")    #in 為字串中有無"day"

 print(len(first_name))

 print(first_name[::2])    #字串分割


data = """B10231011:x:1067:1000:Su Lin-Ya,,0910-622-175:/home/B10231011:/bin/bash
B10206009:x:1068:1000:JI-BING-CHEN,,0910246189:/home/B10206009:/bin/bash
B10206035:x:1070:1000:ZHANG-JIE-KAI,,0970663675:/home/B10206035:/bin/bash
B10206031:x:1071:1000:LI ZHE-CHENG,,0903008989:/home/B10206031:/bin/bash
D10406811:x:1072:1000:jemal yimer damte,,0965668144:/home/D10406811:/bin/bash
M10406013:x:1073:1000:wang kai-ting,,0988148729:/home/M10406013:/bin/bash
B10206022:x:1074:1000:SU-BO-CHENG,,0970623878:/home/B10206022:/bin/bash
M10406009:x:1075:1000:Yu Ching,,0987930004:/home/M10406009:/bin/bash
tino:x:1076:1000:Kaiting wang,,0988148729:/home/tino:/bin/bash
ychungn:x:1077:1000:Hung Ying Chieh,,0975207247:/home/ychungn:/bin/bash
D10306103:x:1078:1000:Yu-Cheng Liu,,0960537760:/home/D10306103:/bin/bash
D10406817:x:1079:1000:Dhana Lakshmi Busipalli,0966747020:/home/D10406817:/bin/bash
chya:x:1080:1000:chya,0956015982:/home/chya:/bin/bash"""










 weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
 for day in weeks:
     if day == "Saturday" or day == "Sunday":
         print("Holiday is : " + day)
     else:
         print("Workday is : " + day )
找Holiday，令出day在weeks後，如果day是saturday或sunday，列出"Holiday is " saturday
 input_day = "FRI"

 for day in weeks:
     if input_day.lower() in day.lower():    #藉由把字串先轉成小寫再來比對字串是否存在
         print(day)
     else:
         print(None)



 week = {'mon': "Monday",
         'tues': "Tuesday",
         'wed': "Wednesday",
         'thur': "Thursday",
         'fri': "Friday",
         'sat': "Saturday",
         'sun': "Sunday"}

 week.setdefault(input_day.lower(), 'None')
 print(week[input_day.lower()])
#setdefault的寫法，列完簡寫及全名後以冒號來代表前後對應，若input的字串不在其中之一，其他則是None。
#不需要跑回圈





 pork = {'A': 1, 'K': 13, 'Q':12}
一樣前面是key後面value
 print(pork['J'] )
 pork_number = 'N'
 default_val=0

 pork.setdefault(pork_number, default_val)
 if not(pork_number in pork.keys()):
     pork[pork_number] = default_val

 print(pork[pork_number])
