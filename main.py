import csv
import re
from matplotlib import pyplot as plt
compile_result_list = []
average_list_x = []
average_list_y = []

#將.csv數據寫入list data中
with open('.\\data\\P2T.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#刪除前四項數據
for i in range(4):
    del(data[0])

#正則表達式處理數據剃除分號並分組
for i in range(len(data)):
    compile_result = re.findall(r"\d+\.+\d+", data[i][0], re.I)
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
print(average_list_y)
print(average_list_x)

plt.xlabel('Time(s)')
plt.ylabel('Temperature[℃]')
plt.title('Laser speed 1500mm/s')
plt.plot(average_list_x, average_list_y)
plt.savefig('.\\figure\\fig.png')
plt.show()
