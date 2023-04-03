def f(x,y):
    return x+y

x0 = float(0)
y0 = float(1)
t = float(10)
ranges = int(2)

# Euler's method
def euler(x0,y0,t,n):
    
    h = (t-x0)/n
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
        y0 = yn
        x0 = x0+h
    
    print('\n%.4f,%.4f' %(t,yn))

euler(x0,y0,t,ranges)

#Runge-Kutta method

def rk4(x0,y0,t,n):
    
    h = (t-x0)/n
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        y0 = yn
        x0 = x0+h
    
    print('\n%.4f,%.4f' %(t,yn))


rk4(x0,y0,t,ranges)