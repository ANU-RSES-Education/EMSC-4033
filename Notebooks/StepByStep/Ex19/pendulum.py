import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import scipy.integrate as integ


def simplePendulum(y,t,length,alpha):
    GRAV = 9.81
    return np.array([y[1],-GRAV*np.sin(y[0])/length - alpha*y[1]])

def simplePendulumIntegration(initialAngle = np.pi/4,length=0.1,alpha=0.2,timesteps=None):
    if timesteps is None:
        timesteps = np.linspace(0,10,500)
    y0 = np.array([initialAngle,0.])
    y = integ.odeint(simplePendulum,y0,timesteps,args=(length,alpha))
    return y

def simplePendulumAnimation(initialAngle = np.pi/4,length=0.1,alpha=0.,timesteps=None):
    y = simplePendulumIntegration(initialAngle,length,alpha,timesteps)
    fig = plt.figure()
    plt.gca().set_aspect('equal')
    plt.xlim(-1.5*length,1.5*length)
    plt.ylim(-1.5*length,1.5*length)
    plt.xticks([])
    plt.yticks([])
    pendulumString, = plt.plot([0,-length*np.sin(y[0,0])],[0,-length*np.cos(y[0,0])],'k')
    pendulumBob, = plt.plot(-length*np.sin(y[0,0]),-length*np.cos(y[0,0]),'ok')
    def plotter(i):
        pendulumString.set_data(([0,-length*np.sin(y[i,0])],[0,-length*np.cos(y[i,0])]))
        pendulumBob.set_data((-length*np.sin(y[i,0]),-length*np.cos(y[i,0])))
    a = anim.FuncAnimation(fig,plotter,frames=len(y),interval=30)
    return a
    ## Display with:
    # from IPython.display import HTML
    # HTML(a.to_jshtml())
    
def doublePendulum(y,t,mass,length):
    GRAV = 9.81
    th1,th2,p1,p2 = y    
    th1dot = (6/(mass*length**2))* (2 * p1 - 3*np.cos(th1-th2) *p2)/(16-9*(np.cos(th1-th2)**2))
    th2dot = (6/(mass*length**2))* (8 * p2 - 3*np.cos(th1-th2) *p1)/(16-9*(np.cos(th1-th2)**2))
    p1dot = -0.5*mass*length**2 * (th1dot*th2dot*np.sin(th1-th2) + 3 * GRAV*np.sin(th1)/length)
    p2dot = -0.5*mass*length**2 * (-th1dot*th2dot*np.sin(th1-th2) + GRAV*np.sin(th2)/length)
    return np.array([th1dot,th2dot,p1dot,p2dot])

def doublePendulumIntegration(initialAngles = (7*np.pi/8,-11*np.pi/12),length=0.1,mass=1,timesteps=None):
    if timesteps is None:
        timesteps = np.linspace(0,10,500)
    y0 = np.array([initialAngles[0],initialAngles[1],0.,0.])
    y = integ.odeint(doublePendulum,y0,timesteps,args=(mass,length))
    return y
                    
    
    
def doublePendulumAnimation(initialAngles = (7*np.pi/8,-11*np.pi/12),length=0.1,mass=1,timesteps=None):
    y = doublePendulumIntegration(initialAngles,length,mass,timesteps)
    fig = plt.figure()
    plt.gca().set_aspect('equal')
    plt.xlim(-2.5*length,2.5*length)
    plt.ylim(-2.5*length,2.5*length)
    p, = plt.plot([],[],'r-')
    st1, = plt.plot([0,-length*np.sin(y[0,0])],[0,-length*np.cos(y[0,0])],'k')
    st2, = plt.plot([-length*np.sin(y[0,0]),-length*np.sin(y[0,0])-length*np.sin(y[0,1])],
                    [-length*np.cos(y[0,0]),-length*np.cos(y[0,0])-length*np.cos(y[0,1])])
    def plotter(i):
        px,py = p.get_data()
        #print(px,py,type(px),type(py))
        if not type(px)is type([]):
            px = px.tolist()
        if not type(py) is type([]):
            py = py.tolist()
        i0 = 0#max(0,len(px)-100)
        p.set_data((px[i0:]+[-length*np.sin(y[i,0])-length*np.sin(y[i,1])],
                    py[i0:]+[-length*np.cos(y[i,0])-length*np.cos(y[i,1])]))
        st1.set_data(([0,-length*np.sin(y[i,0])],[0,-length*np.cos(y[i,0])]))
        st2.set_data(([-length*np.sin(y[i,0]),-length*np.sin(y[i,0])-length*np.sin(y[i,1])],
                      [-length*np.cos(y[i,0]),-length*np.cos(y[i,0])-length*np.cos(y[i,1])]))
    a = anim.FuncAnimation(fig,plotter,frames=len(y),interval=30)
    return a
    ## Display with:
    # from IPython.display import HTML
    # HTML(a.to_jshtml())