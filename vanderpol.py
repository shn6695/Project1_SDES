import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.linspace(0.0,50.0, 100000)

def damping_factor(mu):
    def van_der_pol_dynamics(x, t):
        """Defines system dynamics"""
        x1 = x[1]
        x2 = -mu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
        result = np.array([x1, x2])
        return result
    return van_der_pol_dynamics

def state_trajectories(damp,init_condtns,t):
    """Solves differential equations to return trajectories"""
    states=odeint(damp,init_condtns,t)
    return states


damp_coeff=[-0.1,5,-0.05,5,3]
damp=[]
for i in range(5):
    damp.append(damping_factor(damp_coeff[i]))

ic=[[1,0.5],[3,0.5],[2,0.5],[1,0.5],[-2.5,-2]]
x=[state_trajectories(damp[0],ic[0],t)]
for i in range(1,5):
    x.append(state_trajectories(damp[i],ic[i],t))

##State trajectories
labels=['$x_1$','$x_2$']
for i in range(5):
    plt.figure(figsize=(15.0, 8.0))
    plt.plot(t,x[i][:,0],label=labels[0])
    plt.plot(t,x[i][:,1],label=labels[1])
    plt.legend()
    Title='State Trajectories for Damping = '+str(damp_coeff[i])+' and Initial Conditions = '+str(ic[i])
    plt.title(Title,fontweight='bold', fontsize=20)
    plt.xlabel("Time in seconds",fontsize=18)
    filename='Tex/vanderpol_trajectories'+str(i)+'.png'
    plt.savefig(filename)

## Phase Plot for all trajectories
labels=['Damping=-0.1,IC=[1,0.5]','Damping=5,IC=[3,0.5]','Damping=-0.05,IC=[2,0.5]','Damping=5,IC=[1,0.5]','Damping=3,IC=[-2.5,-2]']
plt.figure(figsize=(15.0, 8.0))
for i in range(5):
    plt.plot(x[i][:,0], x[i][:,1],label=labels[i])
plt.legend()
plt.title('Phase Plots of Solutions to the Van der Pol Equation',fontweight='bold', fontsize=20)
plt.xlabel("x_1",fontsize=18)
plt.ylabel("x_2",fontsize=18)
plt.savefig('Tex/vanderpol_equation.png')

plt.show()
