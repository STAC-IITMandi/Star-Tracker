
import ephem
import speech_recognition as sr

#To get the RA and DEC when provided with the star latitude, longitude and elevation
# uses ephem 
def RA_DEC(ob,latt,long,ele): 
    obs=ephem.Observer()
    obs.lat=latt
    obs.lon=long
    obs.elevation=float(ele)
    obj=ephem.star(ob)
    obj.compute(obs)
    print('\n',ob)
    print('RA:',obj.ra.real,' DEC:', obj.dec.real)

#To take speech as input
# uses seech_recognition library
def recognizing(r):
    with sr.Microphone() as source:
        audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
            print(text)
            return text
                    
        except:
            return 'Unable to recognise voice'
        
# To process the speech input and convert it to the desired form     
# used in case of latitude and longitude             
def processing(text):
        star=list(map(str,text.split()))
        st=['0','0','0']
        for i in range(len(star)):                
            if i%2==0:
                st[int(i/2)]=star[i]
    
        latt='{}:{}:{}'.format(st[0] ,st[1] ,st[2])
        return latt

    
print('Name of star : ',end=' ')
NoS = sr.Recognizer()
Name_of_star=recognizing(NoS)

print('Latitude : ',end=' ')
lati=sr.Recognizer()
latii = recognizing(lati)
Latitude = processing(latii)

print('Longitude : ',end=' ')
logt = sr.Recognizer()
longt=recognizing(logt)
Longitude = processing(longt)

print('Elevation : ',end=' ')
elv = sr.Recognizer()
Elevation = recognizing(elv)

RA_DEC(Name_of_star, Latitude, Longitude, Elevation)