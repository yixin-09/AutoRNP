import numpy as np

def get_poly_fit(xdata,ydata,i):
    # get the polynomial fit
    z = np.polyfit(xdata[:-1], ydata, i)
    p = np.poly1d(z)
    return p,z

def generate_idx_list(glob_l):
    num_l = len(glob_l)
    temp_n = 0
    xdata = [temp_n]
    for i in glob_l:
        xdata.append((i[2] + temp_n))
        temp_n = i[2] + temp_n
    ydata = range(0, num_l)
    return xdata,ydata

def pure_line(x,k,i):
    return k*(x-i[0])+i[1]

def generate_fitting(glob_l):
    xdata, ydata = generate_idx_list(glob_l)
    # get the real function of origianal data
    temp_f = lambda x: np.interp(x, xdata[:-1], ydata)

    # get the simple line function
    k = (ydata[-1] - ydata[0]) / (xdata[-2] - xdata[0])
    temp_l = lambda x: pure_line(x, k, [xdata[0], ydata[0]])

    # calculate the least-square
    linesq = 0.0
    for i in xdata:
        linesq = linesq + (temp_l(i) - temp_f(i)) * (temp_l(i) - temp_f(i))
    polysq = 0.0
    p, z = get_poly_fit(xdata, ydata, 3)
    for i in xdata:
        polysq = polysq + (p(i) - temp_f(i)) * (p(i) - temp_f(i))
    if polysq < linesq:
        temp_str = " int idx = floor(fabs(("+"("+str(z[0])+"*n_x"+"+"+str(z[1])+")"+"*n_x"+"+"+str(z[2])+")"+"*n_x"+"+"+str(z[3])+"));"
    else:
        temp_str = ''
    return temp_str