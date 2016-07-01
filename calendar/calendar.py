from operator import mod

def isLeapYear(year):
	"""判断是否是闰年"""
	if(year%4 is 0 or (year%400 is 0 and year%100 is 0)):
		return True
	return False

def getYearDays(year):
	"""获取年的天数"""
	if(isLeapYear(year)):
		return 366
	return 365

def getMonthDays(year,month):
	"""获取月的天数"""
	month_list = [1,3,5,7,8,10,12]
	for m in month_list:
		if month is m:
			return 31
	if month is 2:
		if(isLeapYear(year)):
			return 29
		return 28
	return 30

def getDateToDateDays(year1,month1,day1,year2,month2,day2):
	"""获取两个日期的天数差"""
	if(year1 > year2):
		print("请输入年份year1大于year2")
	#获取两个完整年份的天数
	fullYearDays = 0
	for y in range(year1,year2+1):
		fullYearDays = fullYearDays + getYearDays(y)
	# 获取小年份多补充的天数
	beforeDays = 0
	for m1 in range(1,month1):
		beforeDays = beforeDays + getMonthDays(year1,m1)
	beforeDays = beforeDays + day1
	# 获取大年份多补充的天数
	afterDays = 0
	for m2 in range(month2,12+1):
		afterDays = afterDays + getMonthDays(year2,m2)
	afterDays = afterDays - day2
	return fullYearDays - beforeDays - afterDays
	#print(fullYearDays - beforeDays - afterDays)

def getWeekDay(year,month,day):
	"""打印星期几"""
	#知道固定的一天是星期几，1990,1,1 星期一
	#星期一：1 星期二：2 星期三：3 星期四：4 星期五：5 星期六：6 星期日：7
	weekDay = 1 + mod(getDateToDateDays(1990,1,1,year,month,day),7)
	return weekDay

def printWeekDays(year,month):
	"""打印月份的日期"""
	#获取该月1号是星期几
	currentMonthWeekDay = getWeekDay(year,month,1)
	countdays = 0
	print("yi\ter\tsan\tsi\twu\tliu\tqi\n")
	print("\n")
	if currentMonthWeekDay != 0:
		for space in range(currentMonthWeekDay-1):
			print("\t")
			countdays =countdays + 1
	for day in range(1,getMonthDays(year,month)+1):
		if(countdays % 7 is 0):
			print("\n")
		print(day)
		countdays =countdays + 1

printWeekDays(2016,6)