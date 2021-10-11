import csv,re,os
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator

def data_x_y(data_local):
    compile_result_list = []
    average_list_x = []
    average_list_y = []
    #將.csv數據寫入list data中
    with open(data_local, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    #刪除前四項數據
    for i in range(4):
        del(data[0])

    #正則表達式處理數據剃除分號並分組
    for i in range(len(data)):
        #重新放入 compile_result_list中
        compile_result_list.append(re.findall(r"\d+\.+\d+", data[i][0], re.I))

    #數據由字串轉為浮點數
    for i in range(len(compile_result_list)):
        for j in range(len(compile_result_list[i])):
            compile_result_list[i][j] = float(compile_result_list[i][j])

    #compile_result_list[182][18]
    #計算並排列數據
    for i in range(len(compile_result_list)):
        sum_A = 0
        sum_B = 0
        #總和計算
        for j in range(int(len(compile_result_list[0])/2)):
            sum_A +=compile_result_list[i][2*j]
            sum_B +=compile_result_list[i][2*j+1]
        #平均計算
        average_list_x.append(sum_A / (len(compile_result_list[i])/2))
        average_list_y.append(sum_B / (len(compile_result_list[i])/2))
    #print(average_list_y)
    #print(average_list_x)
    return(average_list_x,average_list_y)

if __name__ == '__main__':
    #顏色順序(需>=數據量)
    color_and_type = ['blue','green','red','cyan','black','greenyellow','purple']
    legend_result = []
    legend_result_list = []
    #數據位置
    data_path = '.\\data'
    allFileList = os.listdir(data_path)
    fig,axes=plt.subplots(1,1)
    #讀取資料
    j = 0
    for i in allFileList:
        j += 1
        #機算點資料
        data_file = '.\\data\\'+i
        x, y = data_x_y(data_file)
        #圖形繪製
        plt.plot(x, y,color=color_and_type[j-1])
    #讀取檔案名稱
    for i in range(len(allFileList)):
        legend_result.append(re.findall(r"\w+[^.csv]", allFileList[i], re.I)[0])
    #寫入檔案名稱至圖例
    plt.legend(legend_result)
    #格線
    plt.grid(True)
    #x座標名
    plt.xlabel('Time(s)')
    #y座標名
    plt.ylabel('Temperature[℃]')
    #刻度等分數
    axes.xaxis.set_minor_locator(AutoMinorLocator(5))
    axes.yaxis.set_minor_locator(AutoMinorLocator(5))
    #標題
    plt.title('Laser speed 1500mm/s')
    #存檔位置
    plt.savefig('.\\figure\\fig.png')
    #跳出圖型視窗
    plt.show()
