from matplotlib import pyplot as plt
import pickle
import numpy as np



def plot_loss(graph_dict, x, y, title):
    plt.xlabel = x
    plt.ylabel = y
    plt.title = title

    for key, value in graph_dict.items():
        for kkey, vvalue in value.items():
            if kkey == 'loss':
                los = vvalue
            elif kkey == 'epochs':
                ep = vvalue


        if type(ep) != list:
            ep = range(ep)
        plt.plot(ep, los, label=key)

    plt.legend()
    plt.show()






def plot_acc(graph_dict, x, y, title):
    plt.xlabel = x
    plt.ylabel = y
    plt.title = title

    for key, value in graph_dict.items():
        for kkey, vvalue in value.items():
            if kkey == 'acc':
                acc = vvalue
            elif kkey == 'epochs':
                ep = vvalue

        if len(ep) != len(acc):
            ep = range(ep)
        plt.plot(ep, acc, label=key)

    plt.legend()
    plt.show()



def plot_pred_v_actual(prediction, actual, subx, suby, title, linestyles=[], order=[]):
    x1 = []
    y1 = []
    x2 = []
    y2 =[]

    # shapes = ['.', 'o', 'v', '>', '1', '4', 's', '+', 'X', 'd']
    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'springgreen', 'tan', 'slategrey']
    colors = ['k', 'c']

    fig, ax = plt.subplots(subx, suby)
    nplots = subx*suby
    for ii in range(nplots):
        num = np.random.randint(0, len(prediction))
        x1.append(prediction[num, 1])
        y1.append(prediction[num, 2])
        x2.append(actual[num, 1])
        y2.append(actual[num, 2])


    pr = np.asarray((x1, y1))
    ac = np.asarray((x2, y2))
    tail = np.zeros((2,1))
    mm = 0
    # plt.show()

    for jj in range(subx):
        for kk in range(suby):
            ax[jj, kk].quiver((0, 0), (0, 0), ac[0, mm], ac[1, mm], scale=.05, color=colors[0])
            ax[jj, kk].quiver((0, 0), (0, 0), pr[0, mm], pr[1, mm], scale=.05, color=colors[1])
            # ax.set_xlim(-0.5, 0.5)
            # ax.set_ylim(-0.5, 0.5)

            # ax[jj, kk].quiver(*tail, (x1[mm], y1[mm]), color=colors[0], label='Prediction', linestyle=linestyles[0], zorder=order[0])
            # ax[jj, kk].quiver(*tail, (x2[mm], y2[mm]), color=colors[1], label='Actual', linestyle=linestyles[0], zorder=order[1])
            mm += 1


    # plt.legend
    fig.suptitle(title)
    plt.show()


def plot_one_loss(graph_dict, x, y, title, colors, linestyles = [], dicts_wanted=[], order=[], shift=[]):
    col_idx = 0
    plt.figure()
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.semilogy()

    for key, value in graph_dict.items():
        if key in dicts_wanted:
            d = graph_dict[key]
            loss = d['loss'].T
            eps = range(d['epochs'])
            if key in shift:
                eps = eps[1:]
                loss = loss[:-1]
            plt.plot(eps, loss, label=key, color=colors[col_idx], linestyle=linestyles[col_idx], zorder=order[col_idx])
            col_idx += 1

    plt.grid()
    plt.legend(loc='best')#, bbox_to_anchor=(0.23, 0.62, 0.5, 0.5))
    plt.show()


if __name__ == '__main__':
    x = 'Epochs'
    y = 'Loss'
    title = 'FF ndelta 10dim-rico 3dim-out relu 02'
    colors = ['r', 'g', 'b']
    linestyles = ['solid', 'dashed', 'dotted']
    layer_order = [10, 5, 0]
    # with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Metastimuli-Learn\Atom-FFNN\graphing_data.pkl', 'rb') as f1:
    #     prob_graph_dict = pickle.load(f1)
    #
    with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\results_3dims.pkl', 'rb') as f2:
        graph_dict = pickle.load(f2)

    # plot_loss(regress_graph_dict, 'Epochs', 'Loss', 'Plot1')


    dicts_wanted = [
        'ff_25ep_train_rico10dims_ndelta_w_5_500_3dim_relu_02',
        'ff_25ep_test_rico10dims_ndelta_w_5_500_3dim_relu_02',
        'ff_25ep_nullset_rico10dims_ndelta_w_5_500_3dim_relu_02'
                    ]
    shift = [
        'ff_25ep_test_rico10dims_ndelta_w_5_500_3dim_relu_02',
        'ff_25ep_nullset_rico10dims_ndelta_w_5_500_3dim_relu_02'
    ]
    plot_one_loss(graph_dict, x, y, title, colors, dicts_wanted=dicts_wanted, linestyles=linestyles, order=layer_order, shift=shift)



    # with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_2dims\BOWavg_rico\prediction.pkl', 'rb') as f3:
    #     pred = pickle.load(f3)
    #


    with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\ndelta_rico\W_1_20_output_3Dims\train_labels.pkl', 'rb') as f4:
        act = pickle.load(f4)
    #
    #


    pred00_dict = graph_dict['ff_25ep_pred_rico10dims_ndelta_w_1_20_3dim_relu_00']
    pred01_dict = graph_dict['ff_25ep_pred_rico10dims_ndelta_w_1_20_3dim_relu_01']
    pred02_dict = graph_dict['ff_25ep_pred_rico10dims_ndelta_w_1_20_3dim_relu_02']

    pred00 = pred00_dict['prediction']; pred00 = np.reshape(pred00, (pred00.shape[1], 1))
    pred01 = pred01_dict['prediction']; pred01 = np.reshape(pred01, (pred01.shape[1], 1))
    pred02 = pred02_dict['prediction']; pred02 = np.reshape(pred02, (pred02.shape[1], 1))

    pred = np.concatenate((pred00, pred01, pred02), axis=1)
    #
    title = 'Prediction vs. Actual FF ndelta 10dim-rico 3dim-out 01-02'
    subx = 3
    suby = 3
    line = ['solid', 'dashed']
    ord = [5, 0]
    plot_pred_v_actual(pred, act, subx, suby, title, linestyles=line, order=ord)
