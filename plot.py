# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = [1, 2, 6, 8]
# ypoints = [3, 8, 1, 10]

# plt.plot(xpoints, ypoints)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = [1, 2, 6, 8]
# ypoints = [3, 8, 1, 10]

# plt.plot(xpoints, ypoints,'o')
# plt.show()


# plt.plot(xpoints, ypoints,"*")
# plt.show()


# 4, 
# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = [1,2,3,4]
# ypoints = [1,2,3,4]
# plt.plot(xpoints,ypoints)
# plt.show()



# 5,
# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = [1,3,4,5]
# ypoints = [3,4,9,8,8]
# plt.plot(xpoints,ypoints)
# plt.show()


# output:-ValueError: x and y must have same first
# dimension but have shapes (4,) and (5,)


# 6,
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

 # by default xpoints = [0,1,2,3,4,5 and so on ]
# plt.plot(ypoints, marker = '+')
# plt.show()



# 7-

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 'o--r')
# plt.show()



# 8-
# import matplotlib.pyplot as plt 
# data = [2,3,4,5]
# data1 = [6,5,3,6]

# plt.plot(data,data1, "o:")
# plt.show()


# 9-

# import matplotlib.pyplot as plt 

# data = [100,300,355,224]

# plt.plot(data,"*",ms="20")   #ms stands for marker size
# plt.show()



# 10 =

# import matplotlib.pyplot as plt 
# # 
# data = [342,542,345,456,335,334]
# plt.plot(data,marker = "*",ms = 14,mec= "pink")  #'markeredgecolor
# plt.plot(data,marker="*",ms ="20",mfc ="yellow",mec = "black") #markerfacecolor
# plt.show()


# 11 = 
# import matplotlib.pyplot as plt 
# data =[56,46,34,75,99]
# plt.plot(data,color="blue",ls =":")  #ls = line style
# plt.show()



# 12:=
# import matplotlib.pyplot as plt 
# data =[4,4,8,34,54]
# plt.plot(data,lw ="20" , color = "red")
# data2 =[7,5,64,45,5]
# plt.plot(data2,lw="20",color="green")
# plt.show()


# # 13:=  create labels
# import matplotlib.pyplot as plt
# data = [47,54,64,74,43]
# data2 = [85,78,44,66,35]
# plt.xlabel("kismis")
# plt.ylabel("laddu")
# plt.plot(data,color = "red",mec="green",mfc="black",marker="o",ls ="--",lw="5")
# plt.plot(data2)
# plt.show()


# 14:=kismis

# import matplotlib.pyplot as plt
# x=[6,5,7,4,6]
# plt.plot(x)
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
# plt.title("sweats",fontdict = font1)
# plt.xlabel("laddu",fontdict = font2)
# plt.ylabel("kismis",fontdict = font2)
# plt.show()


# 15-
# import matplotlib.pyplot as plt
# data = [7,5,3,5,5,3,5,3]
# plt.title("time", loc = 'left')
# plt.plot(data)
# plt.grid()    #grid
# plt.show()


# 16:-
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.grid()
plt.grid(color = 'green', linestyle = '--', linewidth = 5)
plt.plot(x)
# plt.plot(y)
plt.show()




