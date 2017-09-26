import numpy as np
#평균제곱오차
t= [0,0,1,0,0,0,0,0,0,0]
# 예1 : '2'일 확률이 가장 높다고 추정
y = [0.1,0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]


def mean_squared_error(y,t) : 
	return 0.5 * np.sum((y-t)**2)

mean_squared_error(np.array(y), np.array(t))

# 예1-1 : '2'일 확률이 가장 높다고 추정된 결과, 예2보다 값이 낮게 나온다. 
y = [0.1,0.05,0.7,0.0,0.05,0.05,0.0,0.05,0.0,0.0]
mean_squared_error(np.array(y), np.array(t))

# 예1-2 : '7'일 확률이 가장 높다고 추정된 결과
y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
mean_squared_error(np.array(y), np.array(t))


#교차 엔트로피 오차
def cross_entroypy_error(y,t):
	delta = 1e-7
	return -np.sum(t * np.log(y+delta))

t= [0,0,1,0,0,0,0,0,0,0]
# 예2-1 : '2'일 확률이 가장 높다고 추정된 결과, 예2보다 값이 낮게 나온다. 
y = [0.1,0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
cross_entroypy_error(np.array(y), np.array(t))

# 예2-2 : '2'일 확률이 가장 높다고 추정된 결과
y = [0.1,0.05,0.7,0.0,0.05,0.1,0.0,0.0,0.0,0.0]
cross_entroypy_error(np.array(y), np.array(t))



# 예1-2 : '7'일 확률이 가장 높다고 추정된 결과
y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
cross_entroypy_error(np.array(y), np.array(t))



# (배치용) 교차 엔트로피 오차
#정답 레이블이 원-핫 인코딩인 경우

def cross_entroy_error(y,t) :
	if y.ndim ==1:
		t=t.reshape(1,t.size)
		y=y.reshape(1,y.size)
	
	batch_size=y.shape[0]
	return -np.sum(t*np.log(y)) / batch_size