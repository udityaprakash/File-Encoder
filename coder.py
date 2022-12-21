import time
list1=[]
p=[]
print(".....................Welcome To Uditya's Coder.......................")
print('\n\n')
jklp=input('Enter the name of file(.txt):  ')
lmk=open(jklp+".txt","r")
kl=lmk.readlines()
qwe=input('Enter the name of file to save the generated code: ')
filem=open(qwe+".txt","a") 
for l in kl:
 z=len(l)
 for i in range(0,z):  
   p=l[i]
   if p=='a': 
       z='11'
       list1.append(z)
   elif p=='b':
        
       z='1a'
       list1.append(z)
         
   elif p=='c':
       
       z='13'
       list1.append(z)
      
   elif p=='d':
       
       z='14'
       list1.append(z)
       
   elif p=='e':
        
       z='1d'
       list1.append(z)
       
   elif p=='f':
       
       z='16'
       list1.append(z)
       
   elif p=='g':
       
       z='17'
       list1.append(z) 
       
   elif p=='h':
        
       z='1g'
       list1.append(z)
       
   elif p=='i':
        
       z='19'
       list1.append(z)
       
   elif p=='j':
        
       z='20'
       list1.append(z)
              
   elif p=='k':
        
       z='2j'
       list1.append(z)   
   elif p=='l':
       
       z='22'
       list1.append(z)
   elif p=='m':
       
       z='23'
       list1.append(z)
   elif p=='n':
        
       z='2m'
       list1.append(z) 
   elif p=='o':
       
       z='25'
       list1.append(z)
   elif p=='p':
       
       z='26'
       list1.append(z)
   elif p=='q':
        
       z='2p'
       list1.append(z)
   elif p=='r':
       
       z='28'
       list1.append(z)
   elif p=='s':
       
       z='29'
       list1.append(z) 
   elif p=='t':
        
       z='3s'
       list1.append(z) 
   elif p=='u':
       
       z='31'
       list1.append(z)
   elif p=='v':
       
       z='32'
       list1.append(z)  
   elif p=='w':
       
       z='3v'
       list1.append(z) 
   elif p=='x':
       
       z='34'
       list1.append(z)
   elif p=='y':
       
       z='35'
       list1.append(z)
   elif p=='z':
       z='3y'
       list1.append(z)
   elif p=='A':
       z='65'
       list1.append(z)
   elif p=='B':
       z='6A'
       list1.append(z)
   elif p=='C':
       z='67'
       list1.append(z)
   elif p=='D':
       z='68'
       list1.append(z)
   elif p=='E':
       z='6D'
       list1.append(z)
   elif p=='F':
       z='70'
       list1.append(z)
   elif p=='G':
       z='71'
       list1.append(z)
   elif p=='H':
       z='7G'
       list1.append(z)
   elif p=='I':
       z='73'
       list1.append(z)
   elif p=='J':
       z='74'
       list1.append(z)
   elif p=='K':
       z='7J'
       list1.append(z)
   elif p=='L':
       z='76'
       list1.append(z)
   elif p=='M':
       z='77'
       list1.append(z)
   elif p=='N':
       z='7M'
       list1.append(z)
   elif p=='O':
       z='79'
       list1.append(z)
   elif p=='P':
       z='80'
       list1.append(z)
   elif p=='Q':
       z='8P'
       list1.append(z)
   elif p=='R':
       z='82'
       list1.append(z)
   elif p=='S':
       z='83'
       list1.append(z)
   elif p=='T':
       z='8S'
       list1.append(z)
   elif p=='U':
       z='85'
       list1.append(z)
   elif p=='V':
       z='86'
       list1.append(z)
   elif p=='W':
       z='8V'
       list1.append(z)
   elif p=='X':
       z='88'
       list1.append(z)
   elif p=='Y':
       z='89'
       list1.append(z)
   elif p=='Z':
       z='9Y'
       list1.append(z)
   elif p=='.':
       z='36'
       list1.append(z)
   elif p==',':
       z='37'
       list1.append(z)
   elif p=='0':
       z='51'
       list1.append(z)
   elif p=='1':
       z='52'
       list1.append(z)
   elif p=='2':    
       z='5c'
       list1.append(z)
   elif p=='3':
       z='53'
       list1.append(z)
   elif p=='4':
       z='54'
       list1.append(z)
   elif p=='5':
       z='5d'
       list1.append(z)
   elif p=='6':
       z='56'
       list1.append(z)
   elif p=='7':
       z='57'
       list1.append(z)
   elif p=='8':
       z='5e'
       list1.append(z)
   elif p=='9':
       z='59'
       list1.append(z)    
   else :
       list1.append(p)
filem.writelines(list1)
filem.close()    
lmk.close()
print('kindly go to desktop file name "'+qwe+'"')
print('')       
time.sleep(10)       
       
       
  
