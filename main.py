# --------------------------format(%)----------------------

# ([key],[flag],[w],[.p],[type])
# y = 3.213245;
# x = int(input("inter your float:"));
# z = int(input("inter your width:"));
# print("%*.*f"%(z,x,y));

#--------------------------format({})-------------------------

# x = 6
# y = 5.3121265
# d = {'x':5 , 'y':6, 'z':5.31256}

#[[fill]align][sign][#][width][grouping_option][.precision][type]

# print("my x is:{x}\nmy y is:{y}\nmy z is:{z}".format(**d))
# y = 5.3121265
# print("y is:{0:{sign}{width}{align}}".format(y,sign="-",width=20,align="<"))

# y = input("inter your align: ")
# x = 10
# print("my y is: {0:{align}{sign}{width}}".format(10,align=y,width=20,sign="+"))


# print("x is {0:{aling}{sign}}".format(12,align="^",sign="+"))

# print(type(5/2))
# print(type(6//2))

# x = 10;
# y = 5.2445;
# print("my age is {0}".format("mamad"))