from matplotlib import pyplot as plt
import numpy as np
import xlrd
import xlwt
import ast
import sys
import os
import time
import getopt
import matplotlib

matplotlib.rcParams['text.usetex'] = True


def arrowed_spines(ax=None, arrow_length=20, labels=('', ''), arrowprops=None):
    xlabel, ylabel = labels
    if ax is None:
        ax = plt.gca()
    if arrowprops is None:
        arrowprops = dict(arrowstyle='<|-', facecolor='black')

    for i, spine in enumerate(['left', 'bottom']):
        # Set up the annotation parameters
        t = ax.spines[spine].get_transform()
        xy, xycoords = [1, 0], ('axes fraction', t)
        xytext, textcoords = [arrow_length, 0], ('offset points', t)
        ha, va = 'left', 'bottom'

        # If axis is reversed, draw the arrow the other way
        top, bottom = ax.spines[spine].axis.get_view_interval()
        if top < bottom:
            xy[0] = 0
            xytext[0] *= -1
            ha, va = 'right', 'top'

        if spine is 'bottom':
            xarrow = ax.annotate(xlabel, xy, xycoords=xycoords, xytext=xytext,
                                 textcoords=textcoords, ha=ha, va='center',
                                 arrowprops=arrowprops)
        else:
            yarrow = ax.annotate(ylabel, xy[::-1], xycoords=xycoords[::-1],
                                 xytext=xytext[::-1], textcoords=textcoords[::-1],
                                 ha='center', va=va, arrowprops=arrowprops)
    return xarrow, yarrow


def add_arrow(line, position=None, direction='right', size=5, color=None):
    """
    add an arrow to a line.

    line:       Line2D object
    position:   x-position of the arrow. If None, mean of xdata is taken
    direction:  'left' or 'right'
    size:       size of the arrow in fontsize points
    color:      if None, line color is taken.
    """
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if position is None:
        position = xdata.max()
    # find closest index
    start_ind = 0
    end_ind = 1
    hw = 0.5
    hl = 0.9
    lw = 0.5  # axis line width
    ohg = 0.3  # arrow overhang
    # ax.arrow(0, -0.03, 68, -0.03, fc='k', ec='k', lw=lw,
    #          head_width=hw, head_length=hl, overhang=ohg,
    #          length_includes_head=True, clip_on=False)arrowprops=dict(arrowstyle='simple',fc="0.5",color=color),
    line.axes.annotate('',
                       xytext=(xdata[start_ind], ydata[start_ind]),
                       xy=(xdata[end_ind], ydata[end_ind]),
                       arrowprops=dict(headwidth=4, headlength=5, width=0.8, fc="0.5", color=color),
                       size=size
                       )


mean_error_l = [2025112.1182000001, 234074.52411000003, 58280.480090000005, 135074.27234000002, 6.13516, \
                4.252680000000001, 1.0, 1.0, 12.22451, 1.90654, 1.5652000000000001, \
                1.5652800000000002, 1.83165, 10664.568519999999, 2.2533299999999996, 1.0, \
                2.02422, 1.0, 11.60261, 37.64867999999999]
sngfl_fname = [u'airy_Ai', u'airy_Bi', u'airy_Ai_deriv', u'airy_Bi_deriv', u'bessel_J0', u'bessel_J1', u'bessel_Y0',
               u'bessel_Y1', u'clausen', u'expint_Ei', u'legendre_P2', u'legendre_P3', u'legendre_Q1', u'psi', u'Chi',
               u'Ci', u'lnsinh', u'zeta', u'eta']

ngfl_fname = [u'gsl_sf_airy_Ai', u'gsl_sf_airy_Bi', u'gsl_sf_airy_Ai_deriv', u'gsl_sf_airy_Bi_deriv',
              u'gsl_sf_bessel_J0', u'gsl_sf_bessel_J1', u'gsl_sf_bessel_Y0', u'gsl_sf_bessel_Y1', u'gsl_sf_clausen',
              u'gsl_sf_expint_Ei', u'gsl_sf_legendre_P2', u'gsl_sf_legendre_P3', u'gsl_sf_legendre_Q1', u'gsl_sf_psi',
              u'gsl_sf_psi_1', u'gsl_sf_Chi', u'gsl_sf_Ci', u'gsl_sf_lnsinh', u'gsl_sf_zeta', u'gsl_sf_eta']

id_l = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17',
        'P18', 'P19']


def plot_zfig(acb, aca, sngfl_fname, file_name):
    x = range(1, 20)
    fig = plt.figure()
    fig.set_figheight(3)
    y1 = []
    y2 = []
    y3 = []
    k = 0
    for i in range(0, 20):
        if i != 14:
            y1.append(acb[i + k])
            y2.append(acb[i + k + 1])
            y3.append(acb[i + k + 2])
        k = k + 2
    z1 = []
    z2 = []
    z3 = []
    k = 0
    for i in range(0, 20):
        if i != 14:
            z1.append(aca[i + k])
            z2.append(aca[i + k + 1])
            z3.append(aca[i + k + 2])
        k = k + 2
    plt.subplot(3, 1, 1)
    plt.annotate(r'$L_\varepsilon$',
                 xy=(0.2, 0.7), xycoords='data',
                 xytext=(0, 3), textcoords='offset points', fontsize=16)
    plt.plot(x, y1, 'ro-', label='L')
    plt.plot(x, z1, 'ro-', label='L')
    for i in x:
        plt.annotate(str(y1[i - 1]),
                     xy=(i, y1[i - 1]), xycoords='data',
                     xytext=(-4, 3), textcoords='offset points', fontsize=8)
        plt.annotate(str(z1[i - 1]),
                     xy=(i, z1[i - 1]), xycoords='data',
                     xytext=(-4, 3), textcoords='offset points', fontsize=8)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        left=False,  # ticks along the top edge are off
        labelleft=False)  # labels along the bottom edge are off
    plt.subplot(3, 1, 2)
    plt.annotate(r'$M_\varepsilon$',
                 xy=(0.2, 0.7), xycoords='data',
                 xytext=(0, 3), textcoords='offset points', fontsize=16)
    plt.plot(x, y2, 'g+-', label='M')
    plt.plot(x, z2, 'g+-', label='M')
    for i in x:
        plt.annotate(str(y2[i - 1]),
                     xy=(i, y2[i - 1]), xycoords='data',
                     xytext=(-4, 3), textcoords='offset points', fontsize=8)
        plt.annotate(str(z2[i - 1]),
                     xy=(i, z2[i - 1]), xycoords='data',
                     xytext=(-4, 3), textcoords='offset points', fontsize=8)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        left=False,  # ticks along the top edge are off
        labelleft=False)  # labels along the bottom edge are off
    plt.subplot(3, 1, 3)
    plt.annotate(r'$H_\varepsilon$',
                 xy=(0.2, 0.7), xycoords='data',
                 xytext=(0, 3), textcoords='offset points', fontsize=16)
    plt.plot(x, y3, 'b^-', label='H')
    plt.plot(x, z3, 'b^-', label='H')
    for i in x:
        plt.annotate(str(y3[i - 1]),
                     xy=(i, y3[i - 1]), xycoords='data',
                     xytext=(-4, 3), textcoords='offset points', fontsize=8)
        plt.annotate(str(z3[i - 1]),
                     xy=(i, z3[i - 1]), xycoords='data',
                     xytext=(-4, 3), textcoords='offset points', fontsize=8)
    # Set common labels
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        left=False,  # ticks along the top edge are off
        labelleft=False)  # labels along the bottom edge are off
    fig.text(0.5, 0.01, 'Program ID', ha='center', va='center')
    fig.text(0.01, 0.5, 'Accuracy rate', ha='center', va='center', rotation='vertical')
    plt.xticks(x, x)
    fig.tight_layout()
    plt.savefig("accuracyRepair.eps", format="eps")
    plt.show()


def draw_arrow_error(be, ae, thl, name, name2):
    f = plt.figure(frameon=False, figsize=(5, 3))
    ax = plt.subplot(111)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    hw = 0.5
    hl = 0.9
    lw = 0.5  # axis line width
    ohg = 0.3  # arrow overhang
    ax.arrow(0, -0.03, 68, -0.03, fc='k', ec='k', lw=lw,
             head_width=hw, head_length=hl, overhang=ohg,
             length_includes_head=True, clip_on=False)
    for i in range(0, len(be)):
        if i < 14:
            s_y = 19 - i
            plt.plot([0, 64 - be[i]], [s_y, s_y], c='black', linewidth=1, alpha=0.6)
            line2 = plt.plot([64 - be[i], 64 - ae[i]], [s_y, s_y], c='black', linewidth=1, alpha=0)[0]
            add_arrow(line2)
            plt.scatter(64 - thl[i], s_y, c='r', s=25, marker='<')
            plt.scatter(64 - np.log2(mean_error_l[i]), s_y, c='r', marker=(5, 1))
            plt.plot([64 - be[i], 64 - be[i]], [s_y - 0.2, s_y + 0.2], c='black', linewidth=2)
        if i > 14:
            s_y = 20 - i
            plt.plot([0, 64 - be[i]], [s_y, s_y], c='black', linewidth=1, alpha=0.6)
            line2 = plt.plot([64 - be[i], 64 - ae[i]], [s_y, s_y], c='black', linewidth=1, alpha=0)[0]
            add_arrow(line2)
            plt.scatter(64 - thl[i], s_y, c='r', s=25, marker='<')
            plt.scatter(64 - np.log2(mean_error_l[i]), s_y, c='r', marker=(5, 1))
            plt.plot([64 - be[i], 64 - be[i]], [s_y - 0.2, s_y + 0.2], c='black', linewidth=2)

    plt.tick_params(
        axis='y',  # changes apply to the y-axis
        which='both',  # both major and minor ticks are affected
        left=False,  # ticks along the top edge are off
        labelleft=False,
    )  # labels along the bottom edge are off
    # plt.annotate("Bits Correct for Maximum Error",
    #              xy=(12, 20), xycoords='data',
    #              xytext=(0, 3), textcoords='offset points', fontsize=12)
    plt.annotate('Accuracy improving for ' + name2,
                 xy=(12, 20), xycoords='data',
                 xytext=(0, 3), textcoords='offset points', fontsize=12)
    x_l = []
    temp_y = range(1, 20)
    temp_y.reverse()
    sngfl_fname.reverse()
    for j in range(0, 19):
        plt.annotate("P" + str(temp_y[j]),
                     xy=(-3, j + 0.8), xycoords='data',
                     xytext=(-0.5, 0), textcoords='offset points', fontsize=6)
    for i in range(0, 65, 8):
        x_l.append(i)
    ax.set_xticks(x_l)
    plt.ylabel("Program ID")
    plt.tight_layout()
    plt.savefig(name + ".pdf", format="pdf")
    plt.close()
    # plt.show()


def get_repair_accuracy(exname):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    accuracy_before_l = []
    accuracy_after_l = []
    print table.nrows
    for i in range(0, table.nrows - 1):
        accuracy_before_l.append(float("%.2f" % float(table.row_values(i + 1)[35])))
        accuracy_after_l.append(float("%.2f" % float(table.row_values(i + 1)[45])))
    plot_zfig(accuracy_before_l, accuracy_after_l, sngfl_fname, '')


def hbg_extract_results():
    # temp_str = "/home/yixin/experiment/tempgh/af1"
    temp_str = "/home/yixin/experiment/tempgh/be1"
    source_list = os.listdir(temp_str)
    source_list = sorted(source_list)
    max_l = []
    avg_l = []
    n_l = []
    for j in source_list:
        file_name = temp_str + "/" + j
        f = open(file_name, 'r+')
        all_lines = f.readlines()
        aa = all_lines[1].strip(" bits average error\n")
        aa = float(aa)
        am = all_lines[2].strip(" bits max error\n")
        am = float(am)
        jn = j.strip(".out.gh")
        jn = jn.strip("est_")
        max_l.append(am)
        avg_l.append(aa)
        n_l.append(jn)
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    sheet.write(0, 0, "Program name")
    sheet.write(0, 1, "max_err")
    sheet.write(0, 2, "averge_err")
    for i in range(0, 20):
        sheet.write(i + 1, 0, n_l[i])
        sheet.write(i + 1, 1, max_l[i])
        sheet.write(i + 1, 2, avg_l[i])
    # book.save("autoRNP2.xls")
    book.save("hbg712.xls")


# hbg_extract_results()

def out_programIDName(exname):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    max_err = []
    print table.nrows
    for i in range(0, 20):
        max_err.append(float("%.2f" % np.log2(float(table.row_values(i * 3 + 1)[31]))))
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    sheet.write(0, 0, "Program ID")
    sheet.write(0, 1, "Benchmark")
    sheet.write(0, 2, "Program ID")
    sheet.write(0, 3, "Benchmark")
    for i in range(0, 20):
        if i < 14:
            sheet.write(i + 1, 0, "P" + str(i + 1))
            sheet.write(i + 1, 1, ngfl_fname[i])
            sheet.write(i + 1, 2, max_err[i])
        if i > 14:
            sheet.write(i, 0, "P" + str(i))
            sheet.write(i, 1, ngfl_fname[i])
            sheet.write(i, 2, max_err[i])
        if i == 14:
            sheet.write(20, 0, "P" + str(20))
            sheet.write(20, 1, ngfl_fname[i])
            sheet.write(20, 2, max_err[i])
    book.save("benchmarks.xls")


def out_benchAndresults(exname):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    accuracy_before_l = []
    accuracy_after_l = []
    print table.nrows
    for i in range(0, table.nrows - 1):
        accuracy_before_l.append(float("%.2f" % float(table.row_values(i + 1)[35])))
        accuracy_after_l.append(float("%.2f" % float(table.row_values(i + 1)[45])))
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    # merge_format = book.add_format({
    #     'bold': 1,
    #     'border': 1,
    #     'align': 'center',
    #     'valign': 'vcenter',})
    sheet.write_merge(0, 2, 0, 0, "ID")
    # sheet.write(0, 1, "Time(s)")
    sheet.write_merge(0, 0, 1, 3, "Repair Time(s)")
    sheet.write_merge(1, 2, 1, 1, "L")
    sheet.write_merge(1, 2, 2, 2, "M")
    sheet.write_merge(1, 2, 3, 3, "H")
    sheet.write_merge(0, 0, 4, 9, "Accuracy of Repair")
    sheet.write_merge(1, 1, 4, 5, "L")
    sheet.write(2, 4, "Before")
    sheet.write(2, 5, "After")
    sheet.write_merge(1, 1, 6, 7, "M")
    sheet.write(2, 6, "Before")
    sheet.write(2, 7, "After")
    sheet.write_merge(1, 1, 8, 9, "H")
    sheet.write(2, 8, "Before")
    sheet.write(2, 9, "After")
    for i in range(0, 20):
        if i < 14:
            k1 = i + 3
            sheet.write(k1, 0, "P" + str(i + 1))
            t1 = "%.2f" % float(table.row_values(i * 3 + 1)[8])
            sheet.write(k1, 1, t1)
            t1 = "%.2f" % float(table.row_values(i * 3 + 2)[8])
            sheet.write(k1, 2, t1)
            t1 = "%.2f" % float(table.row_values(i * 3 + 3)[8])
            sheet.write(k1, 3, t1)
            b1 = "%.2f%%" % (float(table.row_values(i * 3 + 1)[35]) * 100)
            sheet.write(k1, 4, b1)
            a1 = "%.2f%%" % (float(table.row_values(i * 3 + 1)[45]) * 100)
            sheet.write(k1, 5, a1)
            b1 = "%.2f%%" % (float(table.row_values(i * 3 + 2)[35]) * 100)
            sheet.write(k1, 6, b1)
            a1 = "%.2f%%" % (float(table.row_values(i * 3 + 2)[45]) * 100)
            sheet.write(k1, 7, a1)
            b1 = "%.2f%%" % (float(table.row_values(i * 3 + 3)[35]) * 100)
            sheet.write(k1, 8, b1)
            a1 = "%.2f%%" % (float(table.row_values(i * 3 + 3)[45]) * 100)
            sheet.write(k1, 9, a1)
        if i > 14:
            k2 = i + 2
            sheet.write(k2, 0, "P" + str(i))
            t1 = "%.2f" % float(table.row_values(i * 3 + 1)[8])
            sheet.write(k2, 1, t1)
            t1 = "%.2f" % float(table.row_values(i * 3 + 2)[8])
            sheet.write(k2, 2, t1)
            t1 = "%.2f" % float(table.row_values(i * 3 + 3)[8])
            sheet.write(k2, 3, t1)
            b1 = "%.2f%%" % (float(table.row_values(i * 3 + 1)[35]) * 100)
            sheet.write(k2, 4, b1)
            a1 = "%.2f%%" % (float(table.row_values(i * 3 + 1)[45]) * 100)
            sheet.write(k2, 5, a1)
            b1 = "%.2f%%" % (float(table.row_values(i * 3 + 2)[35]) * 100)
            sheet.write(k2, 6, b1)
            a1 = "%.2f%%" % (float(table.row_values(i * 3 + 2)[45]) * 100)
            sheet.write(k2, 7, a1)
            b1 = "%.2f%%" % (float(table.row_values(i * 3 + 3)[35]) * 100)
            sheet.write(k2, 8, b1)
            a1 = "%.2f%%" % (float(table.row_values(i * 3 + 3)[45]) * 100)
            sheet.write(k2, 9, a1)
        if i == 14:
            k3 = 20 + 2
            sheet.write(k3, 0, "P" + str(20))
            sheet.write(k3, 1, "T/O")
            sheet.write(k3, 2, "T/O")
            sheet.write(k3, 3, "T/O")
            b1 = "%.f%%" % (float(table.row_values(42 + 1)[35]) * 100)
            sheet.write(k3, 4, b1)
            a1 = "%.2f%%" % (float(table.row_values(42 + 1)[45]) * 100)
            sheet.write(k3, 5, a1)
            b1 = "%.2f%%" % (float(table.row_values(42 + 2)[35]) * 100)
            sheet.write(k3, 6, b1)
            a1 = "%.2f%%" % (float(table.row_values(42 + 2)[45]) * 100)
            sheet.write(k3, 7, a1)
            b1 = "%.2f%%" % (float(table.row_values(42 + 3)[35]) * 100)
            sheet.write(k3, 8, b1)
            a1 = "%.2f%%" % (float(table.row_values(42 + 3)[45]) * 100)
            sheet.write(k3, 9, a1)

    book.save("benchAndResults.xls")


def get_error(exname, k):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    ret_l = []
    temp_k = k
    bmax_err_list = []
    bavg_err_list = []
    amax_err_list = []
    aavg_err_list = []
    th_list = []
    for i in range(0, 20):
        bmax_err_list.append(np.log2(float(str(table.row_values(i + k)[31]).strip("[]"))))
        bavg_err_list.append(np.log2(float(table.row_values(i + k)[33])))
        amax_err_list.append(np.log2(float(str(table.row_values(i + k)[41]).strip("[]"))))
        aavg_err_list.append(np.log2(float(table.row_values(i + k)[43])))
        th_list.append(np.log2(float(table.row_values(i + k)[1])))
        k = k + 2
    if temp_k == 1:
        draw_arrow_error(bmax_err_list, amax_err_list, th_list, "low_max", r'$L_\varepsilon$')
        draw_arrow_error(bavg_err_list, aavg_err_list, th_list, "low_avg", r'$L_\varepsilon$')
    if temp_k == 2:
        draw_arrow_error(bmax_err_list, amax_err_list, th_list, "Mid_max", r'$M_\varepsilon$')
        draw_arrow_error(bavg_err_list, aavg_err_list, th_list, "Mid_avg", r'$M_\varepsilon$')
    if temp_k == 3:
        draw_arrow_error(bmax_err_list, amax_err_list, th_list, "Hig_max", r'$H_\varepsilon$')
        draw_arrow_error(bavg_err_list, aavg_err_list, th_list, "Hig_avg", r'$H_\varepsilon$')


def average_error_out(exname, k):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    ret_l = []
    temp_k = k
    bmax_err_list = []
    bavg_err_list = []
    amax_err_list = []
    aavg_err_list = []
    th_list = []
    for i in range(0, 20):
        bmax_err_list.append(np.log2(float(table.row_values(i + k)[31])))
        bavg_err_list.append(np.log2(float(table.row_values(i + k)[33])))
        amax_err_list.append(np.log2(float(str(table.row_values(i + k)[41]).strip("[]"))))
        aavg_err_list.append(np.log2(float(table.row_values(i + k)[43])))
        th_list.append(np.log2(float(table.row_values(i + k)[1])))
        k = k + 2
    print bavg_err_list
    print aavg_err_list
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    for i in range(0, 20):
        sheet.write(i, 0, bavg_err_list[i])
        sheet.write(i, 1, aavg_err_list[i])
        sheet.write(i, 2, bavg_err_list[i] - aavg_err_list[i])
    book.save("average_autoRNPm.xls")


def normallist(l):
    l = np.asarray(l)
    return (l - l.min()) / (l.max() - l.min())


def plot_th2Time2Boudn(bl, tl, ll):
    # fig = plt.figure()
    # fig.set_figheight(4)
    # fig.set_figwidth(10)
    f2, ax = plt.subplots()
    f2.set_figheight(3.6)
    f2.set_figwidth(12)
    # ax.spines['right'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    x = range(1, 20)
    y1 = []
    y2 = []
    y3 = []
    k = 0
    for i in range(0, 20):
        if i != 14:
            y1.append(bl[i + k])
            y2.append(bl[i + k + 1])
            y3.append(bl[i + k + 2])
        k = k + 2
    z1 = []
    z2 = []
    z3 = []
    k = 0
    for i in range(0, 20):
        if i != 14:
            z1.append(tl[i + k])
            z2.append(tl[i + k + 1])
            z3.append(tl[i + k + 2])
        k = k + 2
    # l1 = []
    # l2 = []
    # l3 = []
    # k = 0
    # for i in range(0, 20):
    #     if i != 14:
    #         l1.append(ll[i + k])
    #         l2.append(ll[i + k + 1])
    #         l3.append(ll[i + k + 2])
    #     k = k + 2
    # ax = plt.subplot(1, 2, 1)
    # ax.grid(True)
    l1, = plt.plot(x, y1, 'bo--', label=r'$I_{err}$' + ' size with ' + r'$L_\varepsilon$')
    l2, = plt.plot(x, y2, 'b+--', label=r'$I_{err}$' + ' size with ' + r'$M_\varepsilon$')
    l3, = plt.plot(x, y3, 'b^--', label=r'$I_{err}$' + ' size with ' + r'$H_\varepsilon$')
    # l1, = plt.plot(x, y1, 'bo--', label="a")
    # l2, = plt.plot(x, y2, 'b+--', label="b")
    # l3, = plt.plot(x, y3, 'b^--', label="c")
    plt.xticks(x, x)
    # ax2 = plt.subplot(1, 2, 2)
    # ax2.grid(True)
    l4, = plt.plot(x, z1, 'ko-', label="repair time with " + r'$L_\varepsilon$')
    l5, = plt.plot(x, z2, 'k+-', label="repair time with " + r'$M_\varepsilon$')
    l6, = plt.plot(x, z3, 'k^-', label="repair time with " + r'$H_\varepsilon$')
    plt.xticks(x, id_l)
    plt.ylabel("log2 value of Time(s) and Size of " + r'$I_{err}$', size=12)
    plt.xlabel("Program ID", size=12)
    i = 3
    for j, k in zip(bl, range(0, 60)):
        if k not in [42, 43, 44]:
            if k in [39, 40, 41]:
                ofst = 15
            else:
                ofst = 2
            plt.annotate(str(int(ll[k])),
                         xy=(i / 3, bl[k]), xycoords='data',
                         xytext=(ofst - 5, 4), textcoords='offset points', fontsize=10)
            i = i + 1
    # plt.legend(handles=[l1,l2,l3,l4,l5,l6], bbox_to_anchor=(0., 1.01, 0.7, .701), ncol=4, loc=3,
    #            mode="expand", borderaxespad=0.)
    # for i in range(1,20):
    #     plt.plot([i,i],[np.min(z1)-0.1,np.max(y3)+0.5])
    # plt.yticks(np.arange(np.min(tl), np.max(bl), 4))
    # plt.grid(True)
    plt.ylim([-4, 50.2])
    plt.tick_params(
        axis='y',  # changes apply to the y-axis
        which='both',  # both major and minor ticks are affected
        right=False,  # ticks along the top edge are off
        labelright=False,
    )  # labels along the bottom edge are off
    # plt.legend(prop={'size': 6},handlelength= 7)
    # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")handles=[l1,l2,l3],
    l1 = plt.legend(handles=[l1, l2, l3], loc="upper left", prop={'size': 10})
    l2 = plt.legend(handles=[l4, l5, l6], bbox_to_anchor=(1.0, 0.4), loc="center right", prop={'size': 10})
    plt.gca().add_artist(l1)
    # plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
    #            mode="expand", borderaxespad=0, ncol=1)
    plt.tight_layout()
    plt.savefig("th2time2bound.pdf", bbox_inches = 'tight',pad_inches = 0,format="pdf")
    plt.close()


def get_th_bound_time(exname):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    bound_l = []
    time_l = []
    lines_l = []
    for i in range(0, table.nrows - 1):
        bound_l.append(np.log2(float(table.row_values(i + 1)[3])) - 1.2)
        time_l.append(np.log2(np.max([float(table.row_values(i + 1)[8]) - float(table.row_values(i + 1)[6]), 0.1])))
        lines_l.append(float(table.row_values(i + 1)[10]))
    # normalized
    # bound_l = normallist(bound_l)
    # time_l = normallist(time_l)
    # th_list = normallist(th_list)
    plot_th2Time2Boudn(bound_l, time_l, lines_l)


# plot the cumulative distribution of time overhead

def plot_time_overhead1(z1):
    z1 = np.array(z1)
    values, base = np.histogram(z1, bins=len(z1))
    print z1
    # evaluate the cumulative
    cumulative = np.cumsum(values)
    # plot the cumulative function
    prec_cum = []
    for i in cumulative:
        prec_cum.append(i * 100 / len(z1))
    print cumulative
    print len(z1)
    print len(cumulative)
    print prec_cum
    print base
    return base, prec_cum
    plt.plot(base[:-1], prec_cum, c='blue')
    plt.show()


def plot_time_overhead(z1):
    z1 = np.array(z1)
    z1 = np.sort(z1)
    y = np.arange(1, len(z1) + 1) / float(len(z1))
    return z1, y


def plot_cumulative_dis_time(b, a, name):
    ratio_b = []
    for i, j in zip(b, a):
        ratio_b.append(j / i)
    z1 = []
    z2 = []
    z3 = []
    k = 0
    for i in range(0, 20):
        if i != 14:
            z1.append(ratio_b[i + k])
            z2.append(ratio_b[i + k + 1])
            z3.append(ratio_b[i + k + 2])
        k = k + 2
    # print z2
    z1, y1 = plot_time_overhead(z1)
    z2, y2 = plot_time_overhead(z2)
    z3, y3 = plot_time_overhead(z3)
    plt.plot(z1, y1, 'b:', label=r'$L_\varepsilon$')
    # print np.interp(1.0, z1, y1)
    # print np.interp(1.0, z2, y2)
    # print np.interp(1.0, z3, y3)
    plt.plot(z2, y2, 'g--', label=r'$M_\varepsilon$')
    plt.plot(z3, y3, 'k-', label=r'$H_\varepsilon$')
    ylabel = []
    for i in np.arange(0, 105, 20):
        ylabel.append(str(i) + "%")
    plt.yticks(np.arange(0, 1.1, 0.2), ylabel)
    plt.legend(loc=4)
    plt.grid(True)
    # plt.ylim([0,1.1])
    plt.savefig(name + ".pdf", format="pdf")
    plt.close()
    # plt.show()
    # # plot the survival function
    # plt.plot(base[:-1], len(z1) - cumulative, c='green')


def get_cumulative_dis_time(exname):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    bbpf_time_l = []
    bwpf_time_l = []
    abpf_time_l = []
    awpf_time_l = []
    for i in range(0, table.nrows - 1):
        bbpf_time_l.append(float(table.row_values(i + 1)[36]))
        bwpf_time_l.append(float(table.row_values(i + 1)[37]))
        abpf_time_l.append(float(table.row_values(i + 1)[46]))
        awpf_time_l.append(float(table.row_values(i + 1)[47]))
    plot_cumulative_dis_time(bbpf_time_l, abpf_time_l, "timeOverheadb")
    # print np.sum(bbpf_time_l)
    # print np.sum(bwpf_time_l)
    # print np.sum(abpf_time_l)
    # print np.sum(awpf_time_l)
    plot_cumulative_dis_time(bwpf_time_l, awpf_time_l, "timeOverheadW")


def plot_st_overhead(p, b, name):
    ratio_b = []
    for i, j in zip(p, b):
        if i != 0:
            ratio_b.append(i / 1024)
        else:
            ratio_b.append(0.0)
    z1 = []
    z2 = []
    z3 = []
    # ratio_b = normallist(ratio_b)
    k = 0
    for i in range(0, 20):
        if i != 14:
            z1.append(ratio_b[i + k])
            z2.append(ratio_b[i + k + 1])
            z3.append(ratio_b[i + k + 2])
        k = k + 2
    x = range(1, 20)
    # plt.plot(x,z1, 'b:', label=r'$L_\varepsilon$')
    # plt.plot(x,z2, 'g--', label=r'$M_\varepsilon$')
    # plt.plot(x,z3, 'k-', label=r'$H_\varepsilon$')
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    for i in range(0, 19):
        sheet.write(0, i + 1, "P" + str(i + 1))
    for i in range(0, 19):
        sheet.write(1, i + 1, "%.2f" % z1[i])
        sheet.write(2, i + 1, "%.2f" % z2[i])
        sheet.write(3, i + 1, "%.2f" % z3[i])
    book.save("storage.xls")

    # plt.xticks(x,id_l)
    # plt.grid(True)
    # plt.legend()
    # plt.tight_layout()
    # plt.savefig(name+".eps",format="eps")
    # plt.show()


def storage_overhead(exname):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    patch_size_l = []
    bad_size_l = []
    for i in range(0, table.nrows - 1):
        patch_size_l.append(float(table.row_values(i + 1)[9]))
        bad_size_l.append(float(table.row_values(i + 1)[3]))
    plot_st_overhead(patch_size_l, bad_size_l, "storage_overhead")


def improving_calculate(exname):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    imp_acc = []
    for i in range(3, 23):
        beacc = float(table.row_values(i)[2])
        afacc = float(table.row_values(i)[5])
        imp_acc.append(beacc - afacc)
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    for i in range(0, len(imp_acc)):
        sheet.write(i, 0, imp_acc[i])
    book.save("imp.xls")


def main():
    opts, args = getopt.getopt(sys.argv[1:], "f:", ["file_name="])
    file_name = " "
    for o, a in opts:
        if o in ('-f'):
            file_name = str(a)
        else:
            print 'unhandled option'
            sys.exit(3)

    # produce the final table
    out_benchAndresults(file_name)

    # produce the arrow figure
    get_error(file_name, 1)
    get_error(file_name, 2)
    get_error(file_name, 3)

    # produce the figure to show bound and time
    get_th_bound_time(file_name)

    # Output the figure of time overhead
    get_cumulative_dis_time(file_name)

    # Output the table of storage overhead
    storage_overhead(file_name)
    out_programIDName(file_name)


if __name__ == "__main__":
    main()

# improving_calculate("autoRNP2.xls")