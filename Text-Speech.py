import pyttsx3
import time

conv = pyttsx3.init()
v=[]
print('Welcone to a text to speech translator')
print('type "speak" to type something for the system to say')
print('type "change_voice" to change the voice')

def say(c):
    print('playing.. ')
    conv.setProperty('rate', 120)

    time.sleep(1)

    conv.say(c)
    conv.runAndWait()
    return c

def voice():
    global vce
    n=1
    voices=conv.getProperty('voices')
    for voice in voices:
        print(f'{n} %s' %voice.name)
        v.append(voice.id)
        n+=1
    c=int(input('\nWhat number: '))
    a=v[c-1]
    print(v,v[c-1],a)
    conv.setProperty('voice',a)
    conv.runAndWait()
    vce=c-1
    return 0

while True:
    ans=input(': ')
    if ans=='speak':
        c=input("What should I say? :  ")
        say(c)
        print('done')
    elif ans=='change_voice':
     print('getting things ready..')
     print('')
     time.sleep(1)
     voice()
     print('')
     print(f'voice set to {v[vce]}')
     v.clear()
    else:
        print('Not a Command!')
