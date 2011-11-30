from matplotlib.pyplot import figure, show
from numpy import pi, sin, linspace
from matplotlib.mlab import stineman_interp
def plot_interp(x,y):
    x = [float(x_step) for x_step in x]
    yp = None
    xi = linspace(x[0],x[-1],100);
    yi = stineman_interp(xi,x,y,yp);
    
    fig = figure()
    ax = fig.add_subplot(111)
    ax.plot(x,y,'r-')
    show()
