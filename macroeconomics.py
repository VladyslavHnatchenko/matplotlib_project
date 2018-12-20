import matplotlib.pyplot as plt


fig1, ax1 = plt.subplots()

print(id(fig1))
print(id(plt.gcf()))

fig2, ax2 = plt.subplots()
print(id(fig2) == id(plt.gcf()))

# from io import BytesIO
# import tarfile
# import numpy as np
# from urllib.request import urlopen
#
#
# url = "http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz"
# b = BytesIO(urlopen(url).read())
# fpath = "CaliforniaHousing/cal_housing.data"
#
# with tarfile.open(mode='r', fileobj=b) as archive:
#     housing = np.loadtxt(archive.extractfile(fpath), delimiter=',')
#
# y = housing[:, -1]
# pop, age = housing[:, [4, 7]].T
#
#
# def add_titlebox(ax, text):
#     ax.text(
#         .55, .8, text,
#         horizontalalalignment='center',
#         transform=ax.transAxes,
#         bbox=dict(facecolor='white', alpha=0.6),
#         fontsize=12.5
#     )
#     return ax
