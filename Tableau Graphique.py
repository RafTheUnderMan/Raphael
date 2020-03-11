import matplotlib.pyplot as plt

#verticales
'''
for i in range (0,80,10):
    x=[]
    y=[]
    x.append(i)
    y.append(0)
    x.append(i)
    y.append(80)
    plt.plot(x,y,'K')
'''
for i in range (0,80,10):
    plt.plot([i,i],[0,80],'b')

#tableau de meme longueur
plt.plot(x,y)
plt.grid()
plt.show()
