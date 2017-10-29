
# coding: utf-8

# In[1]:


import numpy as np

r=0.05
S0=100
K=110
sigma=0.01
T=1

np.random.randn()

EPOCH=10000
N=10

C=0
P=0
for i in range(EPOCH):
    S_bar=0
    S=S0
    for j in range(N):
        WT=np.random.randn()*np.sqrt(T/N)
        S=S*np.exp((r-0.5*sigma**2)*(T/N) + sigma*WT)
        S_bar += S
    S_bar /= N    
    C += max(0,S_bar-K)
    P += max(0,K-S_bar)
    
call_price = (C/EPOCH)*np.exp(-r*T)
put_price = (P/EPOCH)*np.exp(-r*T)

print('Floating Lookback Option:')
print('Call price = ', call_price)
print('Put price = ', put_price)

