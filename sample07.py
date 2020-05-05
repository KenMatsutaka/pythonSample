# copy : sharrow copy と deep copyを扱う為のライブラリ
import copy

#浅いコピー
x = [[1, 2, 3], 4, 5]
y = copy.copy(x)
y[0][0] = 100
y[1] = 400
print("浅いコピー",x , y)

#深いコピー
xx = [[1, 2, 3], 4, 5]
yy = copy.deepcopy(xx)
yy[1] = 400

print("深いコピー",xx , yy)
