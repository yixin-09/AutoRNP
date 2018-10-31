import basic_function as bf
import numpy as np

# step back to refine the "badland"
def step_back(th,temp_b1,step,rf,pf,sign,ulp_p):
    print "step back point"
    ori_value = temp_b1 + ulp_p*step*sign
    print ori_value
    print temp_b1
    step = step/2.0
    while(sign*temp_b1<sign*ori_value):
        temp_b1 = temp_b1 + ulp_p*step*sign
        # max_err_mid = estimate_error(point,p0_err,rf,pf,temp_b1)
        max_err_mid,temp_b1 = bf.max_errorOnPoint(rf,pf,temp_b1,step)
        # if (max_err_mid-th <=5.0):
        #     return temp_b1
        if (max_err_mid > th):
            if step < 100.0:
                return temp_b1
            else:
                temp_b1 = temp_b1 - ulp_p*step*sign
                step = step / 2.0
    return ori_value

# exec the pointToBound algorithm
def pointToBound(th,rf,pf,point):
    print "Begin Find the bound around the inputs and under the threshold"
    # right ward iteration
    step = 4e2
    print "Right forward to find the up bound"
    ulp_p = bf.getulp(point)
    p0_err = bf.getUlpError(rf(point), pf(point))
    temp_b1 = point
    for i in range(0,int(4e2)):
        temp_b1 = temp_b1 + ulp_p*step
        max_err_mid, temp_b1 = bf.max_errorOnPoint(rf, pf, temp_b1, step)
        try:
            times = np.max([np.log10(max_err_mid / th), 2.0])
        except AttributeError:
            times = 1.0
        if (max_err_mid < th):
            temp_b1 = step_back(th,temp_b1,step,rf,pf,-1,ulp_p)
            bound_up = temp_b1
            break
        step = int(step * times)
    print "Left forward to find the down bound"
    step = 4e2
    temp_b1 = point
    for i in range(0, int(4e2)):
        temp_b1 = temp_b1 - ulp_p * step
        max_err_mid, temp_b1 = bf.max_errorOnPoint(rf, pf, temp_b1, step)
        try:
            times = np.max([np.log10(max_err_mid / th), 2.0])
        except AttributeError:
            times = 1.0
        # print step
        # times = np.max([np.log2(max_err_mid / th), 2.0])
        if (max_err_mid < th):
            # print step / times
            temp_b1 = step_back(th, temp_b1, step, rf, pf,1,ulp_p)
            bound_down = temp_b1
            break
        step = int(step * times)
    return [bound_down,bound_up]
