import numpy as np

#1次元配列の生成
arr = np.asarray([1,2,3])
print('①', arr)

#2次元配列の生成
arr = np.asarray([[1, 2, 3],[4, 5, 6]])
print('②', arr)

#平均の取得
print('③', np.mean(arr))

# #最大値、最小値の取得
print('④', np.max(arr))
print('⑤', np.min(arr))

#和の取得
print('⑥', np.sum(arr))

#標準偏差の取得
print('⑦', np.std(arr))
