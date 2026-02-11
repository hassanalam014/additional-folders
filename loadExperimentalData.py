import os,sys,math,csv,numpy as npy
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

#======================================================
#Critical Point and Molecular Weight
#======================================================

Pc0 = 0.001
Tc0 = 265.0
Rc0 = 0.0001

Data1=True
Data2=False
Data3=False
Data4=False

#======================================================
#Loading Isotherm Data 1
#======================================================

if Data1==True:
	with open('Data/434K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_434K = range(0,numpts)
				T0_434K = range(0,numpts)
				R0_434K = range(0,numpts)
				M0_434K = range(0,numpts)
				I0_434K = range(0,numpts)
			if index1 >= 6:
				P0_434K[index2] = float(row[0])
				T0_434K[index2] = float(row[1])
				R0_434K[index2] = float(row[2])
				M0_434K[index2] = float(row[3])
				I0_434K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_434K
	T0 = T0_434K
	R0 = R0_434K
	M0 = M0_434K
	I0 = I0_434K

	with open('Data/449K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_449K = range(0,numpts)
				T0_449K = range(0,numpts)
				R0_449K = range(0,numpts)
				M0_449K = range(0,numpts)
				I0_449K = range(0,numpts)
			if index1 >= 6:
				P0_449K[index2] = float(row[0])
				T0_449K[index2] = float(row[1])
				R0_449K[index2] = float(row[2])
				M0_449K[index2] = float(row[3])
				I0_449K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_449K),axis=0)
	T0 = npy.concatenate((T0,T0_449K),axis=0)
	R0 = npy.concatenate((R0,R0_449K),axis=0)
	M0 = npy.concatenate((M0,M0_449K),axis=0)
	I0 = npy.concatenate((I0,I0_449K),axis=0)

	with open('Data/465K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_465K = range(0,numpts)
				T0_465K = range(0,numpts)
				R0_465K = range(0,numpts)
				M0_465K = range(0,numpts)
				I0_465K = range(0,numpts)
			if index1 >= 6:
				P0_465K[index2] = float(row[0])
				T0_465K[index2] = float(row[1])
				R0_465K[index2] = float(row[2])
				M0_465K[index2] = float(row[3])
				I0_465K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_465K),axis=0)
	T0 = npy.concatenate((T0,T0_465K),axis=0)
	R0 = npy.concatenate((R0,R0_465K),axis=0)
	M0 = npy.concatenate((M0,M0_465K),axis=0)
	I0 = npy.concatenate((I0,I0_465K),axis=0)

	with open('Data/480K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_480K = range(0,numpts)
				T0_480K = range(0,numpts)
				R0_480K = range(0,numpts)
				M0_480K = range(0,numpts)
				I0_480K = range(0,numpts)
			if index1 >= 6:
				P0_480K[index2] = float(row[0])
				T0_480K[index2] = float(row[1])
				R0_480K[index2] = float(row[2])
				M0_480K[index2] = float(row[3])
				I0_480K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_480K),axis=0)
	T0 = npy.concatenate((T0,T0_480K),axis=0)
	R0 = npy.concatenate((R0,R0_480K),axis=0)
	M0 = npy.concatenate((M0,M0_480K),axis=0)
	I0 = npy.concatenate((I0,I0_480K),axis=0)

	with open('Data/495K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_495K = range(0,numpts)
				T0_495K = range(0,numpts)
				R0_495K = range(0,numpts)
				M0_495K = range(0,numpts)
				I0_495K = range(0,numpts)
			if index1 >= 6:
				P0_495K[index2] = float(row[0])
				T0_495K[index2] = float(row[1])
				R0_495K[index2] = float(row[2])
				M0_495K[index2] = float(row[3])
				I0_495K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_495K),axis=0)
	T0 = npy.concatenate((T0,T0_495K),axis=0)
	R0 = npy.concatenate((R0,R0_495K),axis=0)
	M0 = npy.concatenate((M0,M0_495K),axis=0)
	I0 = npy.concatenate((I0,I0_495K),axis=0)

	with open('Data/511K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_511K = range(0,numpts)
				T0_511K = range(0,numpts)
				R0_511K = range(0,numpts)
				M0_511K = range(0,numpts)
				I0_511K = range(0,numpts)
			if index1 >= 6:
				P0_511K[index2] = float(row[0])
				T0_511K[index2] = float(row[1])
				R0_511K[index2] = float(row[2])
				M0_511K[index2] = float(row[3])
				I0_511K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_511K),axis=0)
	T0 = npy.concatenate((T0,T0_511K),axis=0)
	R0 = npy.concatenate((R0,R0_511K),axis=0)
	M0 = npy.concatenate((M0,M0_511K),axis=0)
	I0 = npy.concatenate((I0,I0_511K),axis=0)

	with open('Data/526K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_526K = range(0,numpts)
				T0_526K = range(0,numpts)
				R0_526K = range(0,numpts)
				M0_526K = range(0,numpts)
				I0_526K = range(0,numpts)
			if index1 >= 6:
				P0_526K[index2] = float(row[0])
				T0_526K[index2] = float(row[1])
				R0_526K[index2] = float(row[2])
				M0_526K[index2] = float(row[3])
				I0_526K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_526K),axis=0)
	T0 = npy.concatenate((T0,T0_526K),axis=0)
	R0 = npy.concatenate((R0,R0_526K),axis=0)
	M0 = npy.concatenate((M0,M0_526K),axis=0)
	I0 = npy.concatenate((I0,I0_526K),axis=0)

	with open('Data/541K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_541K = range(0,numpts)
				T0_541K = range(0,numpts)
				R0_541K = range(0,numpts)
				M0_541K = range(0,numpts)
				I0_541K = range(0,numpts)
			if index1 >= 6:
				P0_541K[index2] = float(row[0])
				T0_541K[index2] = float(row[1])
				R0_541K[index2] = float(row[2])
				M0_541K[index2] = float(row[3])
				I0_541K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_541K),axis=0)
	T0 = npy.concatenate((T0,T0_541K),axis=0)
	R0 = npy.concatenate((R0,R0_541K),axis=0)
	M0 = npy.concatenate((M0,M0_541K),axis=0)
	I0 = npy.concatenate((I0,I0_541K),axis=0)

	with open('Data/557K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_557K = range(0,numpts)
				T0_557K = range(0,numpts)
				R0_557K = range(0,numpts)
				M0_557K = range(0,numpts)
				I0_557K = range(0,numpts)
			if index1 >= 6:
				P0_557K[index2] = float(row[0])
				T0_557K[index2] = float(row[1])
				R0_557K[index2] = float(row[2])
				M0_557K[index2] = float(row[3])
				I0_557K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_557K),axis=0)
	T0 = npy.concatenate((T0,T0_557K),axis=0)
	R0 = npy.concatenate((R0,R0_557K),axis=0)
	M0 = npy.concatenate((M0,M0_557K),axis=0)
	I0 = npy.concatenate((I0,I0_557K),axis=0)

	with open('Data/572K_PC_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_572K = range(0,numpts)
				T0_572K = range(0,numpts)
				R0_572K = range(0,numpts)
				M0_572K = range(0,numpts)
				I0_572K = range(0,numpts)
			if index1 >= 6:
				P0_572K[index2] = float(row[0])
				T0_572K[index2] = float(row[1])
				R0_572K[index2] = float(row[2])
				M0_572K[index2] = float(row[3])
				I0_572K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_572K),axis=0)
	T0 = npy.concatenate((T0,T0_572K),axis=0)
	R0 = npy.concatenate((R0,R0_572K),axis=0)
	M0 = npy.concatenate((M0,M0_572K),axis=0)
	I0 = npy.concatenate((I0,I0_572K),axis=0)

#======================================================
#Loading Isotherm Data 2
#======================================================

if Data2==True:
	with open('Data/424K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_424K = range(0,numpts)
				T0_424K = range(0,numpts)
				R0_424K = range(0,numpts)
				M0_424K = range(0,numpts)
				I0_424K = range(0,numpts)
			if index1 >= 6:
				P0_424K[index2] = float(row[0])
				T0_424K[index2] = float(row[1])
				R0_424K[index2] = float(row[2])
				M0_424K[index2] = float(row[3])
				I0_424K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_424K
	T0 = T0_424K
	R0 = R0_424K
	M0 = M0_424K
	I0 = I0_424K

	with open('Data/444K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_444K = range(0,numpts)
				T0_444K = range(0,numpts)
				R0_444K = range(0,numpts)
				M0_444K = range(0,numpts)
				I0_444K = range(0,numpts)
			if index1 >= 6:
				P0_444K[index2] = float(row[0])
				T0_444K[index2] = float(row[1])
				R0_444K[index2] = float(row[2])
				M0_444K[index2] = float(row[3])
				I0_444K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_444K),axis=0)
	T0 = npy.concatenate((T0,T0_444K),axis=0)
	R0 = npy.concatenate((R0,R0_444K),axis=0)
	M0 = npy.concatenate((M0,M0_444K),axis=0)
	I0 = npy.concatenate((I0,I0_444K),axis=0)

	with open('Data/464K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_464K = range(0,numpts)
				T0_464K = range(0,numpts)
				R0_464K = range(0,numpts)
				M0_464K = range(0,numpts)
				I0_464K = range(0,numpts)
			if index1 >= 6:
				P0_464K[index2] = float(row[0])
				T0_464K[index2] = float(row[1])
				R0_464K[index2] = float(row[2])
				M0_464K[index2] = float(row[3])
				I0_464K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_464K),axis=0)
	T0 = npy.concatenate((T0,T0_464K),axis=0)
	R0 = npy.concatenate((R0,R0_464K),axis=0)
	M0 = npy.concatenate((M0,M0_464K),axis=0)
	I0 = npy.concatenate((I0,I0_464K),axis=0)

	with open('Data/484K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_484K = range(0,numpts)
				T0_484K = range(0,numpts)
				R0_484K = range(0,numpts)
				M0_484K = range(0,numpts)
				I0_484K = range(0,numpts)
			if index1 >= 6:
				P0_484K[index2] = float(row[0])
				T0_484K[index2] = float(row[1])
				R0_484K[index2] = float(row[2])
				M0_484K[index2] = float(row[3])
				I0_484K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_484K),axis=0)
	T0 = npy.concatenate((T0,T0_484K),axis=0)
	R0 = npy.concatenate((R0,R0_484K),axis=0)
	M0 = npy.concatenate((M0,M0_484K),axis=0)
	I0 = npy.concatenate((I0,I0_484K),axis=0)

	with open('Data/503K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_503K = range(0,numpts)
				T0_503K = range(0,numpts)
				R0_503K = range(0,numpts)
				M0_503K = range(0,numpts)
				I0_503K = range(0,numpts)
			if index1 >= 6:
				P0_503K[index2] = float(row[0])
				T0_503K[index2] = float(row[1])
				R0_503K[index2] = float(row[2])
				M0_503K[index2] = float(row[3])
				I0_503K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_503K),axis=0)
	T0 = npy.concatenate((T0,T0_503K),axis=0)
	R0 = npy.concatenate((R0,R0_503K),axis=0)
	M0 = npy.concatenate((M0,M0_503K),axis=0)
	I0 = npy.concatenate((I0,I0_503K),axis=0)

	with open('Data/524K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_524K = range(0,numpts)
				T0_524K = range(0,numpts)
				R0_524K = range(0,numpts)
				M0_524K = range(0,numpts)
				I0_524K = range(0,numpts)
			if index1 >= 6:
				P0_524K[index2] = float(row[0])
				T0_524K[index2] = float(row[1])
				R0_524K[index2] = float(row[2])
				M0_524K[index2] = float(row[3])
				I0_524K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_524K),axis=0)
	T0 = npy.concatenate((T0,T0_524K),axis=0)
	R0 = npy.concatenate((R0,R0_524K),axis=0)
	M0 = npy.concatenate((M0,M0_524K),axis=0)
	I0 = npy.concatenate((I0,I0_524K),axis=0)

	with open('Data/544K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_544K = range(0,numpts)
				T0_544K = range(0,numpts)
				R0_544K = range(0,numpts)
				M0_544K = range(0,numpts)
				I0_544K = range(0,numpts)
			if index1 >= 6:
				P0_544K[index2] = float(row[0])
				T0_544K[index2] = float(row[1])
				R0_544K[index2] = float(row[2])
				M0_544K[index2] = float(row[3])
				I0_544K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_544K),axis=0)
	T0 = npy.concatenate((T0,T0_544K),axis=0)
	R0 = npy.concatenate((R0,R0_544K),axis=0)
	M0 = npy.concatenate((M0,M0_544K),axis=0)
	I0 = npy.concatenate((I0,I0_544K),axis=0)

	with open('Data/564K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_564K = range(0,numpts)
				T0_564K = range(0,numpts)
				R0_564K = range(0,numpts)
				M0_564K = range(0,numpts)
				I0_564K = range(0,numpts)
			if index1 >= 6:
				P0_564K[index2] = float(row[0])
				T0_564K[index2] = float(row[1])
				R0_564K[index2] = float(row[2])
				M0_564K[index2] = float(row[3])
				I0_564K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_564K),axis=0)
	T0 = npy.concatenate((T0,T0_564K),axis=0)
	R0 = npy.concatenate((R0,R0_564K),axis=0)
	M0 = npy.concatenate((M0,M0_564K),axis=0)
	I0 = npy.concatenate((I0,I0_564K),axis=0)

	with open('Data/584K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_584K = range(0,numpts)
				T0_584K = range(0,numpts)
				R0_584K = range(0,numpts)
				M0_584K = range(0,numpts)
				I0_584K = range(0,numpts)
			if index1 >= 6:
				P0_584K[index2] = float(row[0])
				T0_584K[index2] = float(row[1])
				R0_584K[index2] = float(row[2])
				M0_584K[index2] = float(row[3])
				I0_584K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_584K),axis=0)
	T0 = npy.concatenate((T0,T0_584K),axis=0)
	R0 = npy.concatenate((R0,R0_584K),axis=0)
	M0 = npy.concatenate((M0,M0_584K),axis=0)
	I0 = npy.concatenate((I0,I0_584K),axis=0)

	with open('Data/603K_PC_6E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_603K = range(0,numpts)
				T0_603K = range(0,numpts)
				R0_603K = range(0,numpts)
				M0_603K = range(0,numpts)
				I0_603K = range(0,numpts)
			if index1 >= 6:
				P0_603K[index2] = float(row[0])
				T0_603K[index2] = float(row[1])
				R0_603K[index2] = float(row[2])
				M0_603K[index2] = float(row[3])
				I0_603K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_603K),axis=0)
	T0 = npy.concatenate((T0,T0_603K),axis=0)
	R0 = npy.concatenate((R0,R0_603K),axis=0)
	M0 = npy.concatenate((M0,M0_603K),axis=0)
	I0 = npy.concatenate((I0,I0_603K),axis=0)

#======================================================
#Loading Isotherm Data 3
#======================================================

if Data3==True:
	with open('Data/433K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_433K = range(0,numpts)
				T0_433K = range(0,numpts)
				R0_433K = range(0,numpts)
				M0_433K = range(0,numpts)
				I0_433K = range(0,numpts)
			if index1 >= 6:
				P0_433K[index2] = float(row[0])
				T0_433K[index2] = float(row[1])
				R0_433K[index2] = float(row[2])
				M0_433K[index2] = float(row[3])
				I0_433K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_433K
	T0 = T0_433K
	R0 = R0_433K
	M0 = M0_433K
	I0 = I0_433K

	with open('Data/443K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_443K = range(0,numpts)
				T0_443K = range(0,numpts)
				R0_443K = range(0,numpts)
				M0_443K = range(0,numpts)
				I0_443K = range(0,numpts)
			if index1 >= 6:
				P0_443K[index2] = float(row[0])
				T0_443K[index2] = float(row[1])
				R0_443K[index2] = float(row[2])
				M0_443K[index2] = float(row[3])
				I0_443K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_443K),axis=0)
	T0 = npy.concatenate((T0,T0_443K),axis=0)
	R0 = npy.concatenate((R0,R0_443K),axis=0)
	M0 = npy.concatenate((M0,M0_443K),axis=0)
	I0 = npy.concatenate((I0,I0_443K),axis=0)

	with open('Data/453K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_453K = range(0,numpts)
				T0_453K = range(0,numpts)
				R0_453K = range(0,numpts)
				M0_453K = range(0,numpts)
				I0_453K = range(0,numpts)
			if index1 >= 6:
				P0_453K[index2] = float(row[0])
				T0_453K[index2] = float(row[1])
				R0_453K[index2] = float(row[2])
				M0_453K[index2] = float(row[3])
				I0_453K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_453K),axis=0)
	T0 = npy.concatenate((T0,T0_453K),axis=0)
	R0 = npy.concatenate((R0,R0_453K),axis=0)
	M0 = npy.concatenate((M0,M0_453K),axis=0)
	I0 = npy.concatenate((I0,I0_453K),axis=0)

	with open('Data/463K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_463K = range(0,numpts)
				T0_463K = range(0,numpts)
				R0_463K = range(0,numpts)
				M0_463K = range(0,numpts)
				I0_463K = range(0,numpts)
			if index1 >= 6:
				P0_463K[index2] = float(row[0])
				T0_463K[index2] = float(row[1])
				R0_463K[index2] = float(row[2])
				M0_463K[index2] = float(row[3])
				I0_463K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_463K),axis=0)
	T0 = npy.concatenate((T0,T0_463K),axis=0)
	R0 = npy.concatenate((R0,R0_463K),axis=0)
	M0 = npy.concatenate((M0,M0_463K),axis=0)
	I0 = npy.concatenate((I0,I0_463K),axis=0)

	with open('Data/473K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_473K = range(0,numpts)
				T0_473K = range(0,numpts)
				R0_473K = range(0,numpts)
				M0_473K = range(0,numpts)
				I0_473K = range(0,numpts)
			if index1 >= 6:
				P0_473K[index2] = float(row[0])
				T0_473K[index2] = float(row[1])
				R0_473K[index2] = float(row[2])
				M0_473K[index2] = float(row[3])
				I0_473K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_473K),axis=0)
	T0 = npy.concatenate((T0,T0_473K),axis=0)
	R0 = npy.concatenate((R0,R0_473K),axis=0)
	M0 = npy.concatenate((M0,M0_473K),axis=0)
	I0 = npy.concatenate((I0,I0_473K),axis=0)

	with open('Data/483K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_483K = range(0,numpts)
				T0_483K = range(0,numpts)
				R0_483K = range(0,numpts)
				M0_483K = range(0,numpts)
				I0_483K = range(0,numpts)
			if index1 >= 6:
				P0_483K[index2] = float(row[0])
				T0_483K[index2] = float(row[1])
				R0_483K[index2] = float(row[2])
				M0_483K[index2] = float(row[3])
				I0_483K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_483K),axis=0)
	T0 = npy.concatenate((T0,T0_483K),axis=0)
	R0 = npy.concatenate((R0,R0_483K),axis=0)
	M0 = npy.concatenate((M0,M0_483K),axis=0)
	I0 = npy.concatenate((I0,I0_483K),axis=0)

	with open('Data/493K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_493K = range(0,numpts)
				T0_493K = range(0,numpts)
				R0_493K = range(0,numpts)
				M0_493K = range(0,numpts)
				I0_493K = range(0,numpts)
			if index1 >= 6:
				P0_493K[index2] = float(row[0])
				T0_493K[index2] = float(row[1])
				R0_493K[index2] = float(row[2])
				M0_493K[index2] = float(row[3])
				I0_493K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_493K),axis=0)
	T0 = npy.concatenate((T0,T0_493K),axis=0)
	R0 = npy.concatenate((R0,R0_493K),axis=0)
	M0 = npy.concatenate((M0,M0_493K),axis=0)
	I0 = npy.concatenate((I0,I0_493K),axis=0)

	with open('Data/503K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_503K = range(0,numpts)
				T0_503K = range(0,numpts)
				R0_503K = range(0,numpts)
				M0_503K = range(0,numpts)
				I0_503K = range(0,numpts)
			if index1 >= 6:
				P0_503K[index2] = float(row[0])
				T0_503K[index2] = float(row[1])
				R0_503K[index2] = float(row[2])
				M0_503K[index2] = float(row[3])
				I0_503K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_503K),axis=0)
	T0 = npy.concatenate((T0,T0_503K),axis=0)
	R0 = npy.concatenate((R0,R0_503K),axis=0)
	M0 = npy.concatenate((M0,M0_503K),axis=0)
	I0 = npy.concatenate((I0,I0_503K),axis=0)

	with open('Data/513K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_513K = range(0,numpts)
				T0_513K = range(0,numpts)
				R0_513K = range(0,numpts)
				M0_513K = range(0,numpts)
				I0_513K = range(0,numpts)
			if index1 >= 6:
				P0_513K[index2] = float(row[0])
				T0_513K[index2] = float(row[1])
				R0_513K[index2] = float(row[2])
				M0_513K[index2] = float(row[3])
				I0_513K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_513K),axis=0)
	T0 = npy.concatenate((T0,T0_513K),axis=0)
	R0 = npy.concatenate((R0,R0_513K),axis=0)
	M0 = npy.concatenate((M0,M0_513K),axis=0)
	I0 = npy.concatenate((I0,I0_513K),axis=0)

	with open('Data/523K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_523K = range(0,numpts)
				T0_523K = range(0,numpts)
				R0_523K = range(0,numpts)
				M0_523K = range(0,numpts)
				I0_523K = range(0,numpts)
			if index1 >= 6:
				P0_523K[index2] = float(row[0])
				T0_523K[index2] = float(row[1])
				R0_523K[index2] = float(row[2])
				M0_523K[index2] = float(row[3])
				I0_523K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_523K),axis=0)
	T0 = npy.concatenate((T0,T0_523K),axis=0)
	R0 = npy.concatenate((R0,R0_523K),axis=0)
	M0 = npy.concatenate((M0,M0_523K),axis=0)
	I0 = npy.concatenate((I0,I0_523K),axis=0)


	with open('Data/533K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_533K = range(0,numpts)
				T0_533K = range(0,numpts)
				R0_533K = range(0,numpts)
				M0_533K = range(0,numpts)
				I0_533K = range(0,numpts)
			if index1 >= 6:
				P0_533K[index2] = float(row[0])
				T0_533K[index2] = float(row[1])
				R0_533K[index2] = float(row[2])
				M0_533K[index2] = float(row[3])
				I0_533K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_533K),axis=0)
	T0 = npy.concatenate((T0,T0_533K),axis=0)
	R0 = npy.concatenate((R0,R0_533K),axis=0)
	M0 = npy.concatenate((M0,M0_533K),axis=0)
	I0 = npy.concatenate((I0,I0_533K),axis=0)

	with open('Data/543K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_543K = range(0,numpts)
				T0_543K = range(0,numpts)
				R0_543K = range(0,numpts)
				M0_543K = range(0,numpts)
				I0_543K = range(0,numpts)
			if index1 >= 6:
				P0_543K[index2] = float(row[0])
				T0_543K[index2] = float(row[1])
				R0_543K[index2] = float(row[2])
				M0_543K[index2] = float(row[3])
				I0_543K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_543K),axis=0)
	T0 = npy.concatenate((T0,T0_543K),axis=0)
	R0 = npy.concatenate((R0,R0_543K),axis=0)
	M0 = npy.concatenate((M0,M0_543K),axis=0)
	I0 = npy.concatenate((I0,I0_543K),axis=0)

	with open('Data/553K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_553K = range(0,numpts)
				T0_553K = range(0,numpts)
				R0_553K = range(0,numpts)
				M0_553K = range(0,numpts)
				I0_553K = range(0,numpts)
			if index1 >= 6:
				P0_553K[index2] = float(row[0])
				T0_553K[index2] = float(row[1])
				R0_553K[index2] = float(row[2])
				M0_553K[index2] = float(row[3])
				I0_553K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_553K),axis=0)
	T0 = npy.concatenate((T0,T0_553K),axis=0)
	R0 = npy.concatenate((R0,R0_553K),axis=0)
	M0 = npy.concatenate((M0,M0_553K),axis=0)
	I0 = npy.concatenate((I0,I0_553K),axis=0)

	with open('Data/563K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_563K = range(0,numpts)
				T0_563K = range(0,numpts)
				R0_563K = range(0,numpts)
				M0_563K = range(0,numpts)
				I0_563K = range(0,numpts)
			if index1 >= 6:
				P0_563K[index2] = float(row[0])
				T0_563K[index2] = float(row[1])
				R0_563K[index2] = float(row[2])
				M0_563K[index2] = float(row[3])
				I0_563K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_563K),axis=0)
	T0 = npy.concatenate((T0,T0_563K),axis=0)
	R0 = npy.concatenate((R0,R0_563K),axis=0)
	M0 = npy.concatenate((M0,M0_563K),axis=0)
	I0 = npy.concatenate((I0,I0_563K),axis=0)

	with open('Data/573K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_573K = range(0,numpts)
				T0_573K = range(0,numpts)
				R0_573K = range(0,numpts)
				M0_573K = range(0,numpts)
				I0_573K = range(0,numpts)
			if index1 >= 6:
				P0_573K[index2] = float(row[0])
				T0_573K[index2] = float(row[1])
				R0_573K[index2] = float(row[2])
				M0_573K[index2] = float(row[3])
				I0_573K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_573K),axis=0)
	T0 = npy.concatenate((T0,T0_573K),axis=0)
	R0 = npy.concatenate((R0,R0_573K),axis=0)
	M0 = npy.concatenate((M0,M0_573K),axis=0)
	I0 = npy.concatenate((I0,I0_573K),axis=0)

	with open('Data/583K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_583K = range(0,numpts)
				T0_583K = range(0,numpts)
				R0_583K = range(0,numpts)
				M0_583K = range(0,numpts)
				I0_583K = range(0,numpts)
			if index1 >= 6:
				P0_583K[index2] = float(row[0])
				T0_583K[index2] = float(row[1])
				R0_583K[index2] = float(row[2])
				M0_583K[index2] = float(row[3])
				I0_583K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_583K),axis=0)
	T0 = npy.concatenate((T0,T0_583K),axis=0)
	R0 = npy.concatenate((R0,R0_583K),axis=0)
	M0 = npy.concatenate((M0,M0_583K),axis=0)
	I0 = npy.concatenate((I0,I0_583K),axis=0)

	with open('Data/593K_PC_305E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_593K = range(0,numpts)
				T0_593K = range(0,numpts)
				R0_593K = range(0,numpts)
				M0_593K = range(0,numpts)
				I0_593K = range(0,numpts)
			if index1 >= 6:
				P0_593K[index2] = float(row[0])
				T0_593K[index2] = float(row[1])
				R0_593K[index2] = float(row[2])
				M0_593K[index2] = float(row[3])
				I0_593K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_593K),axis=0)
	T0 = npy.concatenate((T0,T0_593K),axis=0)
	R0 = npy.concatenate((R0,R0_593K),axis=0)
	M0 = npy.concatenate((M0,M0_593K),axis=0)
	I0 = npy.concatenate((I0,I0_593K),axis=0)

#======================================================
#Loading Isotherm Data 4
#======================================================

if Data4==True:
	with open('Data/424K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_424K = range(0,numpts)
				T0_424K = range(0,numpts)
				R0_424K = range(0,numpts)
				M0_424K = range(0,numpts)
				I0_424K = range(0,numpts)
			if index1 >= 6:
				P0_424K[index2] = float(row[0])
				T0_424K[index2] = float(row[1])
				R0_424K[index2] = float(row[2])
				M0_424K[index2] = float(row[3])
				I0_424K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_424K
	T0 = T0_424K
	R0 = R0_424K
	M0 = M0_424K
	I0 = I0_424K

	with open('Data/434K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_434K = range(0,numpts)
				T0_434K = range(0,numpts)
				R0_434K = range(0,numpts)
				M0_434K = range(0,numpts)
				I0_434K = range(0,numpts)
			if index1 >= 6:
				P0_434K[index2] = float(row[0])
				T0_434K[index2] = float(row[1])
				R0_434K[index2] = float(row[2])
				M0_434K[index2] = float(row[3])
				I0_434K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_434K),axis=0)
	T0 = npy.concatenate((T0,T0_434K),axis=0)
	R0 = npy.concatenate((R0,R0_434K),axis=0)
	M0 = npy.concatenate((M0,M0_434K),axis=0)
	I0 = npy.concatenate((I0,I0_434K),axis=0)

	with open('Data/444K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_444K = range(0,numpts)
				T0_444K = range(0,numpts)
				R0_444K = range(0,numpts)
				M0_444K = range(0,numpts)
				I0_444K = range(0,numpts)
			if index1 >= 6:
				P0_444K[index2] = float(row[0])
				T0_444K[index2] = float(row[1])
				R0_444K[index2] = float(row[2])
				M0_444K[index2] = float(row[3])
				I0_444K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_444K),axis=0)
	T0 = npy.concatenate((T0,T0_444K),axis=0)
	R0 = npy.concatenate((R0,R0_444K),axis=0)
	M0 = npy.concatenate((M0,M0_444K),axis=0)
	I0 = npy.concatenate((I0,I0_444K),axis=0)

	with open('Data/454K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_454K = range(0,numpts)
				T0_454K = range(0,numpts)
				R0_454K = range(0,numpts)
				M0_454K = range(0,numpts)
				I0_454K = range(0,numpts)
			if index1 >= 6:
				P0_454K[index2] = float(row[0])
				T0_454K[index2] = float(row[1])
				R0_454K[index2] = float(row[2])
				M0_454K[index2] = float(row[3])
				I0_454K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_454K),axis=0)
	T0 = npy.concatenate((T0,T0_454K),axis=0)
	R0 = npy.concatenate((R0,R0_454K),axis=0)
	M0 = npy.concatenate((M0,M0_454K),axis=0)
	I0 = npy.concatenate((I0,I0_454K),axis=0)

	with open('Data/464K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_464K = range(0,numpts)
				T0_464K = range(0,numpts)
				R0_464K = range(0,numpts)
				M0_464K = range(0,numpts)
				I0_464K = range(0,numpts)
			if index1 >= 6:
				P0_464K[index2] = float(row[0])
				T0_464K[index2] = float(row[1])
				R0_464K[index2] = float(row[2])
				M0_464K[index2] = float(row[3])
				I0_464K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_464K),axis=0)
	T0 = npy.concatenate((T0,T0_464K),axis=0)
	R0 = npy.concatenate((R0,R0_464K),axis=0)
	M0 = npy.concatenate((M0,M0_464K),axis=0)
	I0 = npy.concatenate((I0,I0_464K),axis=0)

	with open('Data/474K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_474K = range(0,numpts)
				T0_474K = range(0,numpts)
				R0_474K = range(0,numpts)
				M0_474K = range(0,numpts)
				I0_474K = range(0,numpts)
			if index1 >= 6:
				P0_474K[index2] = float(row[0])
				T0_474K[index2] = float(row[1])
				R0_474K[index2] = float(row[2])
				M0_474K[index2] = float(row[3])
				I0_474K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_474K),axis=0)
	T0 = npy.concatenate((T0,T0_474K),axis=0)
	R0 = npy.concatenate((R0,R0_474K),axis=0)
	M0 = npy.concatenate((M0,M0_474K),axis=0)
	I0 = npy.concatenate((I0,I0_474K),axis=0)

	with open('Data/484K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_484K = range(0,numpts)
				T0_484K = range(0,numpts)
				R0_484K = range(0,numpts)
				M0_484K = range(0,numpts)
				I0_484K = range(0,numpts)
			if index1 >= 6:
				P0_484K[index2] = float(row[0])
				T0_484K[index2] = float(row[1])
				R0_484K[index2] = float(row[2])
				M0_484K[index2] = float(row[3])
				I0_484K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_484K),axis=0)
	T0 = npy.concatenate((T0,T0_484K),axis=0)
	R0 = npy.concatenate((R0,R0_484K),axis=0)
	M0 = npy.concatenate((M0,M0_484K),axis=0)
	I0 = npy.concatenate((I0,I0_484K),axis=0)

	with open('Data/494K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_494K = range(0,numpts)
				T0_494K = range(0,numpts)
				R0_494K = range(0,numpts)
				M0_494K = range(0,numpts)
				I0_494K = range(0,numpts)
			if index1 >= 6:
				P0_494K[index2] = float(row[0])
				T0_494K[index2] = float(row[1])
				R0_494K[index2] = float(row[2])
				M0_494K[index2] = float(row[3])
				I0_494K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_494K),axis=0)
	T0 = npy.concatenate((T0,T0_494K),axis=0)
	R0 = npy.concatenate((R0,R0_494K),axis=0)
	M0 = npy.concatenate((M0,M0_494K),axis=0)
	I0 = npy.concatenate((I0,I0_494K),axis=0)

	with open('Data/504K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_504K = range(0,numpts)
				T0_504K = range(0,numpts)
				R0_504K = range(0,numpts)
				M0_504K = range(0,numpts)
				I0_504K = range(0,numpts)
			if index1 >= 6:
				P0_504K[index2] = float(row[0])
				T0_504K[index2] = float(row[1])
				R0_504K[index2] = float(row[2])
				M0_504K[index2] = float(row[3])
				I0_504K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_504K),axis=0)
	T0 = npy.concatenate((T0,T0_504K),axis=0)
	R0 = npy.concatenate((R0,R0_504K),axis=0)
	M0 = npy.concatenate((M0,M0_504K),axis=0)
	I0 = npy.concatenate((I0,I0_504K),axis=0)

	with open('Data/514K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_514K = range(0,numpts)
				T0_514K = range(0,numpts)
				R0_514K = range(0,numpts)
				M0_514K = range(0,numpts)
				I0_514K = range(0,numpts)
			if index1 >= 6:
				P0_514K[index2] = float(row[0])
				T0_514K[index2] = float(row[1])
				R0_514K[index2] = float(row[2])
				M0_514K[index2] = float(row[3])
				I0_514K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_514K),axis=0)
	T0 = npy.concatenate((T0,T0_514K),axis=0)
	R0 = npy.concatenate((R0,R0_514K),axis=0)
	M0 = npy.concatenate((M0,M0_514K),axis=0)
	I0 = npy.concatenate((I0,I0_514K),axis=0)

	with open('Data/524K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_524K = range(0,numpts)
				T0_524K = range(0,numpts)
				R0_524K = range(0,numpts)
				M0_524K = range(0,numpts)
				I0_524K = range(0,numpts)
			if index1 >= 6:
				P0_524K[index2] = float(row[0])
				T0_524K[index2] = float(row[1])
				R0_524K[index2] = float(row[2])
				M0_524K[index2] = float(row[3])
				I0_524K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_524K),axis=0)
	T0 = npy.concatenate((T0,T0_524K),axis=0)
	R0 = npy.concatenate((R0,R0_524K),axis=0)
	M0 = npy.concatenate((M0,M0_524K),axis=0)
	I0 = npy.concatenate((I0,I0_524K),axis=0)

	with open('Data/534K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_534K = range(0,numpts)
				T0_534K = range(0,numpts)
				R0_534K = range(0,numpts)
				M0_534K = range(0,numpts)
				I0_534K = range(0,numpts)
			if index1 >= 6:
				P0_534K[index2] = float(row[0])
				T0_534K[index2] = float(row[1])
				R0_534K[index2] = float(row[2])
				M0_534K[index2] = float(row[3])
				I0_534K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_534K),axis=0)
	T0 = npy.concatenate((T0,T0_534K),axis=0)
	R0 = npy.concatenate((R0,R0_534K),axis=0)
	M0 = npy.concatenate((M0,M0_534K),axis=0)
	I0 = npy.concatenate((I0,I0_534K),axis=0)

	with open('Data/544K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_544K = range(0,numpts)
				T0_544K = range(0,numpts)
				R0_544K = range(0,numpts)
				M0_544K = range(0,numpts)
				I0_544K = range(0,numpts)
			if index1 >= 6:
				P0_544K[index2] = float(row[0])
				T0_544K[index2] = float(row[1])
				R0_544K[index2] = float(row[2])
				M0_544K[index2] = float(row[3])
				I0_544K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_544K),axis=0)
	T0 = npy.concatenate((T0,T0_544K),axis=0)
	R0 = npy.concatenate((R0,R0_544K),axis=0)
	M0 = npy.concatenate((M0,M0_544K),axis=0)
	I0 = npy.concatenate((I0,I0_544K),axis=0)

	with open('Data/554K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_554K = range(0,numpts)
				T0_554K = range(0,numpts)
				R0_554K = range(0,numpts)
				M0_554K = range(0,numpts)
				I0_554K = range(0,numpts)
			if index1 >= 6:
				P0_554K[index2] = float(row[0])
				T0_554K[index2] = float(row[1])
				R0_554K[index2] = float(row[2])
				M0_554K[index2] = float(row[3])
				I0_554K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_554K),axis=0)
	T0 = npy.concatenate((T0,T0_554K),axis=0)
	R0 = npy.concatenate((R0,R0_554K),axis=0)
	M0 = npy.concatenate((M0,M0_554K),axis=0)
	I0 = npy.concatenate((I0,I0_554K),axis=0)

	with open('Data/564K_PC_737E2_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_564K = range(0,numpts)
				T0_564K = range(0,numpts)
				R0_564K = range(0,numpts)
				M0_564K = range(0,numpts)
				I0_564K = range(0,numpts)
			if index1 >= 6:
				P0_564K[index2] = float(row[0])
				T0_564K[index2] = float(row[1])
				R0_564K[index2] = float(row[2])
				M0_564K[index2] = float(row[3])
				I0_564K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_564K),axis=0)
	T0 = npy.concatenate((T0,T0_564K),axis=0)
	R0 = npy.concatenate((R0,R0_564K),axis=0)
	M0 = npy.concatenate((M0,M0_564K),axis=0)
	I0 = npy.concatenate((I0,I0_564K),axis=0)

#======================================================
#Isotherm PVT Data
#======================================================

#Including all experimental data.
#temp = ['303K','312K','321K','332K','343K','354K','364K','373K','383K','393K','402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']
#Only data 20K above the glass transition.
#temp = ['402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']
#All data excluding all data within 20K of the glass transition.
#temp = ['303K','312K','321K','332K','343K','402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']

#for i in range(0,len(temp)):
#	exec "P0_%s,T0_%s,R0_%s,M0_%s,I0_%s = loadExperimentalData('%s_PC_11E4_PVT','isotherm',True)" % (temp[i],temp[i],temp[i],temp[i],temp[i],temp[i])