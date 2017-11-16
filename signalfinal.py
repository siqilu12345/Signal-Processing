import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as signal
import obspy as ob
def plot9(b) :
    ax=list()
    plt.figure(1)
    for i in range(9) :
        ax.append(plt.subplot(3,3,i+1))
    for i in range(9) :
        plt.sca(ax[i])
        plt.plot(b[i])
    plt.show()
a=ob.read('/Users/siqilu/Desktop/D08data_ele/data/*.rms')
b=np.array(a)
#plot9(b)
def plotamp(b) :
    sp = np.fft.fft(b)
    freq = np.fft.fftfreq(np.size(b[0]), 0.005)
    ax=list()
    plt.figure(1)
    for i in range(9) :
        ax.append(plt.subplot(3,3,i+1))
    for i in range(9) :
        plt.sca(ax[i])
        plt.plot(freq,np.abs(sp[i]))
        plt.xlim(0,10)
    plt.show()
def peak(b) :
    mypeak=list()
    for i in range(9) :
        mypeak.append(signal.argrelmax(b[i],order=10000))
    return mypeak
#plotamp(b)
'''
b=signal.resample(b,8000,axis=1)
plt.plot(b[1])
'''
B,A=signal.iirdesign([0.04,0.06],[0.03,0.08],1,40)
b=signal.lfilter(B,A,b)
for i in [2,5,6,8] :
    b[i]=signal.wiener(b[i],799)
b=np.abs(signal.hilbert(b))
'''
for i in [2,5,8] :
    b[i]=signal.savgol_filter(b[i],1001,1)
'''
mypeak=peak(b)
print(np.array(mypeak))