# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:33:28 2020

@author: Janhavi
"""
import ephem

def RA_DEC(ob,latt,long,ele):
    obs=ephem.Observer()
    obs.lat=latt
    obs.lon=long
    obs.elevation=float(ele)
    obj=ephem.star(ob)
    obj.compute(obs)
    print(ob,':\nRA:',obj.ra.real,' DEC:', obj.dec.real)
    
RA_DEC(input('Enter name of star: '),input('Enter latitude: '),input('Enter longitude: '), input('Enter elevation: '))

