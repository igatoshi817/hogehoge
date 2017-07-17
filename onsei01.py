import numpy as np
import glob
#template_data,test_data
temp_folder = 'city_mcepdata/city012/*'
test_folder = 'city_mcepdata/city022/*'
def main():
    #data_load
    fl_temp = glob.glob(temp_folder)
    fl_test = glob.glob(test_folder)
    dat_temp = [[[0]*15]*15]*len(fl_temp)
    dat_test = [[[0]*15]*15]*len(fl_test)
    for num in range((len(fl_temp))):
        dat_temp[num]=np.loadtxt(fl_temp[num],dtype='float',skiprows=3)
    for num in range((len(fl_test))):
        dat_test[num]=np.loadtxt(fl_test[num],dtype='float',skiprows=3)
    #g_data_intiation
    tf_g = np.zeros(len(fl_temp))
    g = np.zeros(len(fl_temp))

    #main
    dist_dat = np.zeros((15, 15))
    for test_num in range(len(fl_test)):
        for temp_num in range(len(fl_temp)):
            for i in range(15):
                for j in range(15):
                    dist_dat[i][j] = np.sqrt(np.sum((dat_temp[temp_num][i,]-dat_test[test_num][j,])**2))
            g[temp_num] = dp(dist_dat)
        if np.argmin(g) == test_num:
            tf_g[test_num] = 1
        #print('test_number : %d, true:%d'.format(test_num, tf_g[test_num]))
    print('\ttemplate: %s \n\ttest :%s \n\t%d percent' % (temp_folder,test_folder,np.sum(tf_g)))

#dp_matching
def dp(data):
    dist_data = data
    rows, cols = data.shape
    for i in range(rows-1):
        dist_data[i+1][0] = dist_data[i][0]+data[i+1][0]
    for j in range(cols-1):
        dist_data[0][j+1] = dist_data[0][j]+data[0][j+1]
    for i in range(rows-1):
        for j in range(cols-1):
            way =np.zeros(3)
            way[0] = dist_data[i+1][j] + data[i+1][j+1]
            way[1] = dist_data[i][j] + 2*data[i+1][j+1]
            way[2] = dist_data[i][j+1] + data[i+1][j+1]
            dist_data[i+1][j+1] = np.min(way)
    return dist_data[rows-1][cols-1]

main()
