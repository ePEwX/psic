n=["m","n"]
c=["ẗ","c","z̈","d̈"]
ua=['p','t','k']
sa=['b','d','g',]
ub=['l','f','x','w','j','s','s̈']
sb=['l','v','w','j','z']
v=["i","ÿ","ä","a","o","u","y"]
ci1=""
ci2=""
vo=""
cf1=""
cf2=""
ici1=0
ici2=0
iv=0
icf1=0
icf2=0
us1=5
us2=5
def fci1():
	for ici1 in range(0,6):
		if ici1 <= 2:
			ci1=ub[ici1]
			us1=0
			fci2()
			return 0
		elif ici1 <= 5:
			ci1=sb[ici1-3]
			us1=1
			fci2()
			return 0
		else:
			ci1=""
			fci2()
			return 0
def fci2():
	if us1==0:
		for ici2 in range(0,7):
			if ici2 != 7:
				ci2=ub[ici2]
				fvo()
				return 0
			else:
				ci2=""
				fvo()
				return 0
	elif us1==1:
		for ici2 in range(0,5):
			if ici2 != 5:
				ci2=sb[ici2]
				fvo()
				return 0
			else:
				ci2=""
				fvo()
				return 0
	else:
		for ici2 in range(0,12):
			if ici2 <= 6:
				ci2=ub[ici2]
				fvo()
				return 0
			elif ici2 <= 11:
				ci2=sb[ici2-7]
				fvo()
				return 0
			else:
				ci2=""
				fvo()
				return 0
def fvo():
	for iv in range(0,6):
		vo=v[iv]
		fcf1()
		return 0
def fcf1():
	for icf1 in range(0,6):
		if icf1 <= 2:
			cf1=ub[icf1]
			us2=0
			fcf2()
			return 0
		elif icf1 <= 5:
			cf1=sb[icf1-3]
			us2=1
			fcf2()
			return 0
		else:
			cf1=""
			fcf2()
			return 0
def fcf2():
	if us2==0:
		for icf2 in range(0,7):
			if icf2 != 7:
				cf2=ub[icf2]
				print(ci1+ci2+vo+cf1+cf2)
			else:
				cf2=""
				print(ci1+ci2+vo+cf1+cf2)
	elif us2==1:
		for icf2 in range(0,5):
			if icf2 != 5:
				cf2=sb[icf2]
				print(ci1+ci2+vo+cf1+cf2)
			else:
				cf2=""
				print(ci1+ci2+vo+cf1+cf2)
	else:
		for icf2 in range(0,12):
			if icf2 <= 6:
				cf2=ub[icf2]
				print(ci1+ci2+vo+cf1+cf2)
			elif icf2 <= 11:
				cf2=sb[icf2-7]
				print(ci1+ci2+vo+cf1+cf2)
			else:
				cf2=""
				print(ci1+ci2+vo+cf1+cf2)
fci1()
