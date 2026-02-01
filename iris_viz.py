import seaborn as sns
import matplotlib.pyplot as plt

# 1. アヤメのデータを読み込む
iris = sns.load_dataset('iris')

# 2. データの最初の5行を表示して中身を確認
print("--- データの最初を確認 ---")
print(iris.head())

# 3. 散布図行列（Pair Plot）を作成
# 種類(species)ごとに色を分けて、すべての項目の組み合わせをグラフにします
sns.pairplot(iris, hue='species')

# 4. グラフを表示する
plt.show()