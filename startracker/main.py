
import ephem
import speech_recognition as sr
import math

#To get the altitude and azimuth when provided with the star latitude, longitude and elevation
# uses ephem 
def ALT_AZ(ob,latt,long,ele): 
    obs=ephem.Observer()
    obs.lat=latt
    obs.lon=long
    obs.elevation=float(ele)
    obj=ephem.star(ob)
    obj.compute(obs)
    
    alt=obj.alt.real
    az=obj.az.real
    altdeg=alt*180/math.pi
    azdeg=az*180/math.pi
    print('\n',ob)
    print('ALT:',altdeg,' AZ:', azdeg)
    return altdeg, azdeg

#To take speech as input
# uses seech_recognition library
def recognizing(r):
    with sr.Microphone() as source:
        audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
            return text
                    
        except:
            return 'Unable to recognise voice'

#To confirm what we said
def confirmation(a):
    c=0
    while c==0:
        print(a)
        r=sr.Recognizer()
        o=recognizing(r)
        if o=='Unable to recognise voice':
            print(o,' Kindly repeat')
        else:   
            print('Did you say ', o)
            conf=sr.Recognizer()
            co=recognizing(r)
            if co =='yes':
                c=1
            else:
                print('Kindly repeat')
    return o    
       
# To process the speech input and convert it to the desired form     
# used in case of latitude and longitude             
def processing(text):
        star=list(map(str,text.split()))
        st={'degrees':0,'minutes':0,'seconds':0}
        
        i = 0
        while i < len(star):
            j=star[i]
            k=star[i+1]
            st[k] = j
            i+=2
            
        st_values=list(st.values())
        latt='{}:{}:{}'.format(st_values[0] ,st_values[1] ,st_values[2])
        return latt

    
a='Name of star : '
Name=confirmation(a)
Name_of_star=Name.capitalize()


a='Latitude : '
lati=confirmation(a)
Latitude = processing(lati)

a='Longitude : '
longt=confirmation(a)
Longitude = processing(longt)

a='Elevation : '
Elevation = confirmation(a)

ALT_AZ(Name_of_star, Latitude, Longitude, Elevation)