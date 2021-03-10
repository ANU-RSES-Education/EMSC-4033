import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
from IPython.display import HTML
anim.rcParams['animation.embed_limit']=40

def isSorted(a):
    for i in range(len(a)-1):
        if a[i+1]<a[i]: return False
    return True
def gnomeSort(a):
    states=[a.copy()]
    pairs = []
    while not isSorted(a):
        for i in range(0,len(a)-1):
            if a[i+1]<a[i]:
                pairs+=[(a[i],a[i+1])]
                x = a[i+1]
                a[i+1] = a[i]
                a[i] = x
                break
        states+=[a.copy()]
    return states,pairs
def bubbleSort(a):
    states=[a.copy()]
    pairs = []
    while not isSorted(a):
        for i in range(0,len(a)-1):
            if a[i+1]<a[i]:
                pairs+=[(a[i],a[i+1])]
                x = a[i+1]
                a[i+1] = a[i]
                a[i] = x
                states+=[a.copy()]
    return states,pairs
def selectionSort(a):
    firstUnsorted = 0
    states=[a.copy()]
    pairs = []
    while not isSorted(a):
        i = firstUnsorted+np.argmin(a[firstUnsorted:])
        if i==firstUnsorted:
            firstUnsorted+=1
            continue
        pairs+=[(firstUnsorted,i)]
        x = a[firstUnsorted]
        a[firstUnsorted] = a[i]
        a[i] = x
        firstUnsorted+=1
        states+=[a.copy()]
        
    return states,pairs
def shellSort(a,seq=[10,4,1]):
    states=[a.copy()]
    pairs = []
    for s in seq:
        for i0 in range(0,s):
            j = 0
            done = True
            while True:
                k1 = i0+(j*s)
                k2 = i0+((j+1)*s)
                if k2>=len(a):
                    if done:
                        break
                    else:
                        j=0
                        done=True
                        continue
                if a[k2]<a[k1]:
                    done = False
                    pairs+=[(k1,k2)]
                    x = a[k2]
                    a[k2] = a[k1]
                    a[k1] = x
                    #j = max(j-2,-1)
                    states+=[a.copy()]
                    if isSorted(a): return states,pairs
                j+=1
    return states,pairs

data = np.arange(100)
np.random.shuffle(data)
np.random.shuffle(data)
s_gnome,p_gnome = gnomeSort(data.copy())
s_bubble,p_bubble = bubbleSort(data.copy())
s_selection,p_selection = selectionSort(data.copy())
s_shell,p_shell = shellSort(data.copy(),seq=[50,25,12,6,3,1])
fig=plt.figure(figsize=(8,3))
ax_gnome = plt.subplot(411)
im_gnome=plt.imshow(data.reshape(1,data.shape[0]),aspect=5,cmap=plt.cm.jet)
plt.title("Gnome sort")
plt.xticks([])
plt.yticks([])
plt.ylim(-0.7,0.7)
plt.xlim(-1.5,data.shape[0]+0.5)

ax_bubble = plt.subplot(412)
plt.title("Bubble sort")
im_bubble=plt.imshow(data.reshape(1,data.shape[0]),aspect=5,cmap=plt.cm.jet)
plt.xticks([])
plt.yticks([])
plt.ylim(-0.7,0.7)
plt.xlim(-1.5,data.shape[0]+0.5)
ax_selection = plt.subplot(413)

plt.title("Selection sort")
im_selection=plt.imshow(data.reshape(1,data.shape[0]),aspect=5,cmap=plt.cm.jet)
plt.xticks([])
plt.yticks([])
plt.ylim(-0.7,0.7)
plt.xlim(-1.5,100.5)
ax_shell = plt.subplot(414)
plt.title("Shell sort")
im_shell=plt.imshow(data.reshape(1,data.shape[0]),aspect=5,cmap=plt.cm.jet)
plt.xticks([])
plt.yticks([])
plt.ylim(-0.7,0.7)
plt.xlim(-1.5,100.5)
plt.tight_layout()


def animator(i):
    try:
        im_gnome.set_data(s_gnome[i].reshape(1,100))
    except IndexError:
        im_gnome.set_data(s_gnome[-1].reshape(1,100))
        ax_gnome.set_facecolor('xkcd:mint green')
    try:
        im_bubble.set_data(s_bubble[i].reshape(1,100))
    except IndexError:
        im_bubble.set_data(s_bubble[-1].reshape(1,100))
        ax_bubble.set_facecolor('xkcd:mint green')
    try:
        im_selection.set_data(s_selection[i].reshape(1,100))
    except IndexError:
        im_selection.set_data(s_selection[-1].reshape(1,100))
        ax_selection.set_facecolor('xkcd:mint green')
    try:
        im_shell.set_data(s_shell[i].reshape(1,100))
    except IndexError:
        im_shell.set_data(s_shell[-1].reshape(1,100))
        ax_shell.set_facecolor('xkcd:mint green')
    
ani = anim.FuncAnimation(fig, animator, 100+max([len(s_bubble), len(s_gnome), len(s_shell), 
                                                 len(s_selection)]), interval=25)

html = ani.to_jshtml()
fp = open('tmp.html','w')
fp.write(html)
fp.close()