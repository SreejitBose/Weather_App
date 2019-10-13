import pprint
import get_cityid
from pyfiglet import Figlet
def main():
    print('')
    f=Figlet(font='slant')
    print(f.renderText('Weather App'))
    print('                  Powered by openweathermap.org             ')

    c=input('For login press L and for sign up press S to use the Weather App')
    if (c=='L'):
        lid=input('Please provide user id')
        lpass=input('enter password')
        fileob=open('C:\\Users\\Sreejit\\Desktop\\gitpro\\Weather_App\\user.txt','r')
        res=eval(fileob.read())
        if(res[lid]==lpass):
            get_cityid.main()
        else:
            print('incorrect username or password')    
    elif(c=='S'):
        uid=input('Please provide user id')
        passw=input('Please provide Password')
        copass=input('Confirm Password')
        if(passw==copass):
            fileob=open('C:\\Users\\Sreejit\\Desktop\\gitpro\\Weather_App\\user.txt','r')
            res=eval(fileob.read())
            fileob.close()
            if uid in res.keys():
                print('user already exists')
                exit()
            res[uid]=passw
            fileob=open('C:\\Users\\Sreejit\\Desktop\\gitpro\\Weather_App\\user.txt','w')
            fileob.write(pprint.pformat(res))
            fileob.close()
            print('Signed up sucessfully')
    else:
        print('Please select L for login or S for sign up to use the Weather App')        

if __name__ == "__main__":
    main()            