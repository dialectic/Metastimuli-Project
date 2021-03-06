import pickle
import numpy as np



class Shuffler:

    def __init__(self, x, y, dims, trsplit=0.8, tesplit=0.2):
        self.x = x
        self.y = y
        self.dims = dims

        self.trsplit = trsplit
        self.tesplit = tesplit


    def data_to_numpy(self, lst):
        # make encoded data into numpy arrays
        holder = []
        for ele in lst:
            # converts list of lists into a numpy array
            if ele == []:
                # check if empty list, not sure why empty lists are in the data.
                ele = list(np.zeros((self.dims, 1)))
                # ele = [0., 0.]
            temp = np.array(ele)
            temp = temp.reshape((temp.shape[0], 1))
            holder.append(temp)

        arr = np.concatenate(holder, axis=1)

        return arr


    def split(self, xx, yy):
        assert self.trsplit + self.tesplit == 1.0
        test = []
        train = []
        test_labels = []
        train_labels = []
        for ii in range (len(xx)):
            ran = np.random.random()
            if ran < self.tesplit:
                test.append(xx[ii, :])
                test_labels.append(yy[ii, :])
            else:
                train.append(xx[ii, :])
                train_labels.append(yy[ii, :])

        train = np.asarray(train)
        train_labels = np.asarray(train_labels)
        test = np.asarray(test)
        test_labels = np.asarray(test_labels)


        return train, train_labels, test, test_labels

    def norm_all(self, train=None, test=None, null=None):
        from sklearn import preprocessing

        train_shape = np.shape(train)
        test_shape = np.shape(test)
        null_shape = np.shape(null)

        if train_shape != ():
            con = np.concatenate((train, test), axis=0)
            y = preprocessing.normalize(con)
            # y = preprocessing.MinMaxScaler(con)
            trnorm = y[:train_shape[0], :]
            tenorm = y[train_shape[0]:, :]


            return trnorm, tenorm
        else:
            reshape_null = np.reshape(null, (null.shape[0]*null.shape[2], null.shape[1]))

            y = preprocessing.normalize(reshape_null)
            # y = preprocessing.MinMaxScaler(con)
            nunorm = np.reshape(y, null.shape)
            return nunorm

    def rando(self, x, y):
        xx = np.ones(x.shape)
        yy = np.ones(y.shape)

        oldx = np.copy(x)
        oldy = np.copy(y)

        for ii in range(np.random.randint(3, 13)):
            for row in range(len(x)):
                r = np.random.randint(0, len(x))
                xx[row, :] = oldx[r, :]
                xx[r, :] = oldx[row, :]

                yy[r, :] = oldy[row, :]
                yy[row, :] = oldy[r, :]
            oldx = np.copy(xx)
            oldy = np.copy(yy)

        return xx, yy


    def train_test_split(self):
        xx = self.data_to_numpy(self.x)
        if list(self.y):
            yy = np.asarray(self.y)
        else:
            yy = self.y

        xx = xx.T

        train, train_labels, test, test_labels = self.split(xx, yy)

        return train, train_labels, test, test_labels

    def shuff_train_test_split(self):
        xx = self.data_to_numpy(self.x)
        if list(self.y):
            yy = np.asarray(self.y)
        else:
            yy = self.y

        xx = xx.T

        xxx, yyy = self.rando(xx, yy)
        train, train_labels, test, test_labels = self.split(xxx, yyy)

        return train, train_labels, test, test_labels


# if __name__ == '__main__':
#     # x1 = r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\ndelta_rico\W_1_20_output_3Dims\train.pkl'
#     # y1 = r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\ndelta_rico\W_1_20_output_3Dims\train_labels.pkl'
#     # x2 = r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\ndelta_rico\W_1_20_output_3Dims\test.pkl'
#     # y2 = r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\ndelta_rico\W_1_20_output_3Dims\test_labels.pkl'
#     # x3 = x2
#     # y3 = r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\ndelta_rico\W_1_20_output_3Dims\nulltest_3dims.pkl'
#
#     x1 = r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Ordered_Data\Rico-Corpus\model_10000ep_30dims\BOWsum\w100\all_atoms_weighted_100alpha.pkl'
#     y1 = r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Ordered_Data\Full_Ordered_Labels_3Dims.pkl'
#     #
#     #
#     with open(x1, 'rb') as f1:
#         xtr = pickle.load(f1)
#
#     with open(y1, 'rb') as f2:
#         ytr = pickle.load(f2)
#
#
#     SH = Shuffler(x1, y1, 30)
#
#     # with open(x2, 'rb') as f3:
#     #     xte = pickle.load(f3)
#     #
#     # with open(y2, 'rb') as f4:
#     #     yte = pickle.load(f4)
#     #
#     # with open(x3, 'rb') as f5:
#     #     xnu = pickle.load(f5)
#     #
#     # with open(y3, 'rb') as f6:
#     #     ynu = pickle.load(f6)
#
#
#
#
#     xtr = data_to_numpy(xtr, 10)
#     # xte = data_to_numpy(xte)
#     ytr = np.asarray(ytr)
#     # yte = np.asarray(yte)
#
#     # transpose?
#     xtr = xtr.T
#     # xte = xte.T
#
#
#     print(len(xtr))
#     print(len(ytr))
#     # print(len(xte))
#     # print(len(yte))
#
#     x = xtr
#     y = ytr
#
#     # x = np.concatenate((xtr, xte))
#     # y = np.concatenate((ytr, yte))
#
#
#     # with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Misc_Data\full_set.pkl', 'wb') as f:
#     #     pickle.dump(x, f)
#
#     # with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\BOWavg_sciart\fulltest_atoms.pkl', 'wb') as f01:
#     #     pickle.dump(x, f01)
#     # with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\BOWavg_sciart\fulltest_labels.pkl', 'wb') as f02:
#     #     pickle.dump(y, f02)
#
#
#     # xx, yy = rando(x, y)
#
#
#     # if you want the ordered dataset split, uncomment below and comment out rando()
#     xx = x
#     yy = y
#
#     train, train_labels, test, test_labels = split(xx, yy, 0.8, 0.2)
#
#
#     # train, test = norm_all(train=xtr, test=xte)
#     # train_labels, test_labels= norm_all(train=ytr, test=yte)
#     # null_labels = norm_all(null=ynu)
#
#
#
#
#     with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Ordered_Data\Rico-Corpus\model_10000ep_30dims\BOWsum\w100\train.pkl', 'wb') as f5:
#         pickle.dump(train, f5)
#     with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Ordered_Data\Rico-Corpus\model_10000ep_30dims\BOWsum\w100\train_labels.pkl', 'wb') as f6:
#         pickle.dump(train_labels, f6)
#
#     with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Ordered_Data\Rico-Corpus\model_10000ep_30dims\BOWsum\w100\test.pkl', 'wb') as f7:
#         pickle.dump(test, f7)
#     with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Ordered_Data\Rico-Corpus\model_10000ep_30dims\BOWsum\w100\test_labels.pkl', 'wb') as f8:
#         pickle.dump(test_labels, f8)
#
#
#     # with open(r'C:\Users\liqui\PycharmProjects\Generation_of_Novel_Metastimulus\Lib\Shuffled_Data_1\Rico-Corpus\model_10000ep_10dims\ndelta_rico\W_1_20_output_3Dims\null_labels_norm.pkl', 'wb') as f10:
#     #     pickle.dump(null_labels, f10)