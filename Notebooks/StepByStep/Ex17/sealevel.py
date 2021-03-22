import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_and_plot_data(filename,figsize=(12,6)):
    data = pd.read_excel(filename)
    plt.figure(figsize=figsize)
    plt.plot(data['Age_kaBP'],data['RSL_m'],color='firebrick')
    plt.xlabel("Age (kaBP)")
    plt.ylabel("RSL (m)")
    plt.gca().invert_xaxis()
    plt.show()
    return data
def interpolate_data(data,ninterp=4096):
    ndata = data.Age_kaBP.size
    interp_times = np.linspace(0,data.Age_kaBP[ndata-1],ninterp)
    interp_data = np.interp(interp_times,data.Age_kaBP,data.RSL_m)
    return interp_times,interp_data
def de_mean(u):
    return u-u.mean()

def plot_Milankovitch(filename,nfft=40960,figsize=(10,8)):
    data = pd.read_excel(filename)
    interpTimes, interpData = interpolate_data(data)

    spec = np.fft.rfft(de_mean(interpData),nfft,norm='ortho')
    fs = np.fft.rfftfreq(nfft,interpTimes[1])

    plt.figure(figsize=figsize)
    plt.plot(fs,np.real(spec.conj()*spec),'firebrick')
    plt.xlim(0,0.1)
    ymin,ymax = plt.ylim()
    xshift = 0.0025
    plt.plot([1/41,1/41],[0,ymax],'k--')
    plt.text(1/41-xshift,0.9*ymax,'Axial tilt',rotation=90,fontsize=10,va='top')

    plt.plot([1/23,1/23],[0,ymax],'k--')
    plt.text(1/23 - xshift, 0.9*ymax,'Axial precession',rotation=90,fontsize=10,va='top')

    plt.plot([1/100,1/100],[0,ymax],'k--')
    plt.text(1/100 - xshift, 0.9*ymax,'Orbital ellipticity',rotation=90,fontsize=10,va='top')
    plt.xticks([1/x for x in [10,20,30,40,50,100]],[10,20,30,40,50,100])
    plt.xlabel("Period/kyr")
    plt.ylabel("Power")
    plt.ylim(0,ymax)
    plt.show()

def cosineLowPass(f,flo,fhi):
    return np.where(f<flo,1,np.where(f>fhi,0,0.5*(1+np.cos(np.pi*((f-flo)/(fhi-flo))))))

def cosineHighPass(f,flo,fhi):
    return np.where(f>fhi,1,np.where(f<flo,0,0.5*(1-np.cos(np.pi*((f-flo)/(fhi-flo))))))

def cosineBandPass(f,f1,f2,f3,f4):
    return cosineHighPass(f,f1,f2)*cosineLowPass(f,f3,f4)

def gaussianBandPass(f,fcen,w):
    return np.exp(-(f-fcen)**2 / (2*w**2))


def plot_filtered(filename,filt,nfft=40960,figsize=(10,8)):
    data = pd.read_excel(filename)
    interpTimes, interpData = interpolate_data(data)

    spec = np.fft.rfft(de_mean(interpData),nfft,norm='ortho')
    fs = np.fft.rfftfreq(nfft,interpTimes[1])

    fspec = filt(fs)*spec
    plt.figure(figsize=figsize)
    plt.subplot(211)
    plt.plot(fs,np.real(np.conj(fspec)*fspec))
    plt.xlim(0,0.1)
    plt.xticks([1/x for x in [10,20,30,40,50,100]],[10,20,30,40,50,100])
    plt.xlabel("Period/kyr")
    plt.ylabel("Power")
    plt.subplot(212)
    plt.plot(interpTimes,np.fft.irfft(fspec,nfft, norm='ortho')[0:interpData.shape[0]])
    plt.xlabel("Age (kaBP)")
    plt.ylabel("RSL (m); filtered")
    plt.gca().invert_xaxis()
    plt.show()
