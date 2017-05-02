#1. Clump Thickness: 1 - 10
#2. Uniformity of Cell Size: 1 - 10
#3. Uniformity of Cell Shape: 1 - 10
#4. Marginal Adhesion: 1 - 10
#5. Single Epithelial Cell Size: 1 - 10
#6. Bare Nuclei: 1 - 10
#7. Bland Chromatin: 1 - 10
#8. Normal Nucleoli: 1 - 10
#9. Mitoses: 1 - 10

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

def pred(dict):
	ds = pd.read_csv("cancer_predictor/breast_cancer.csv")
	data = ds.values[:,:]
	split = int(0.80*data.shape[0])
	X_train = data[:split, 1:10]
	X_test = data[split:, 1:]
	y_train = data[:split, 10]
	y_test = data[split:, 10]
	rf = RandomForestClassifier(n_estimators=100)
	rf.fit(X_train, y_train)
	list = dict.values()
	nlist = []
	for ix in list[:9]:
		if int(ix) < 11:
			nlist.append(int(ix))
	X = np.array(nlist)
	test = X.reshape(1,-1)
	res = rf.predict(test)
	if(res == 2):
		print "Benign"
	else:
		print "Malignant"
	return int(res)
