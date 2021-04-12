from math import *
from numpy import *
Lxx=1.8
Lyy=1.8
Lzz=3.0
Lxyz=[Lxx,Lyy,Lzz]
m=18
j=0.0016
j0=0.04
Kf=0.5
Kf0=0.03
Km=0.00001
Km0=0
Ks=0.1
t=0
# ????????
p0=[0,0,0]
p1=[0.5,0,-0.5]
p2=[0.5,0,0.5]
p3=[-0.5,0,0.5]
p4=[-0.5,0,-0.5]
p5=[-1.5,0,0]
# ?????????
e1=[1,0,0]
e2=[0,1,0]
e3=[0,0,1]

# Управление
# k1=0
# k2=0
# k3=0
# k4=0
# k5=0
# k6=0


Gx=0
Gy=-9.81
Gz=0
GV=[Gx,Gy,Gz]
dt=0.001
tMax=11
n=18
eps0=0
eps1=0
eps2=0
eps3=0
eps4=0
eps5=0
# Вектор упраления
epsV=[eps0,eps1,eps2,eps3,eps4,eps5]
per=5*2*pi
array=[0,0,0,0,0,0,0,0,0,0,0,0,2*per,per,per,per,per,0]
for i in range(n):
    print(array[i],",",end=" ")
print()



# Функция для сумирования двух векторов размерности 3
def VtoV(a,b,n):
    tmp=[0,0,0]
    for i in range(n):
        tmp[i]=a[i]+b[i]
    return tmp
# Функция для суммирования пяти векторов размерности 3
def VtoVFive(a,b,c,d,e,k):
    tmp=[0,0,0]
    for i in range(3):
        tmp[i]=a[i]+b[i]+c[i]+d[i]+e[i]+k[i]
    return tmp

# Функция кватернионного уравнения для двух кватровекторов
def KvatrVect(a,b):
    temp=[0,0,0,0]
    temp[0]=a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
    temp[1]=a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2]
    temp[2]=a[0]*b[2]+a[2]*b[0]+a[3]*b[1]-a[1]*b[3]
    temp[3]=a[0]*b[3]+a[3]*b[0]+a[1]*b[2]-a[2]*b[1]
    return temp
# Функция умножения элементов двух векторов
def VnaV(a,b):
    temp=[0,0,0]
    for i in range(3):
        temp[i]=a[i]*b[i]

    return temp

# Шаг для метода Рунге-Куты
def rungeKutStep(cur_x,mas):
    temp =0.0
    temp=cur_x+dt/6*(mas[0]+2*mas[1]+2*mas[2]+mas[3])
    return temp
# Нахождение коэфициентов для каждой правой части
def rungeKut1(Fe,Gx,Fs):
    mas=[0.0,0.0,0.0,0.0]
    h=dt
    mas[0]=rightPart2(Fe,Gx,Fs)
    mas[1]=rightPart2(Fe+0.5*h*mas[0],Gx+0.5*h*mas[0],Fs+0.5*h*mas[0])
    mas[2]=rightPart2(Fe+0.5*h*mas[1],Gx+0.5*h*mas[1],Fs+0.5*h*mas[1])
    mas[3]=rightPart2(Fe+h*mas[2],Gx+h*mas[2],Fs+h*mas[2])
    return mas
def rungeKut2(Mg,dH,Mf,Ma,l):
    mas=[0.0,0.0,0.0,0.0]
    h=dt
    mas[0]=rightPart3(Mg,dH,Mf,Ma,l)
    mas[1]=rightPart3(Mg+0.5*h*mas[0],dH+0.5*h*mas[0],Mf+0.5*h*mas[0],Ma+0.5*h*mas[0],l+0.5*h*mas[0])
    mas[2]=rightPart3(Mg+0.5*h*mas[1],dH+0.5*h*mas[1],Mf+0.5*h*mas[1],Ma+0.5*h*mas[1],l+0.5*h*mas[1])
    mas[3]=rightPart3(Mg+h*mas[2],dH+h*mas[2],Mf+h*mas[2],Ma+h*mas[2],l+h*mas[2])
    return mas
def rungeKut3(s3,s2,teta,gama):
    mas=[0.0,0.0,0.0,0.0]
    h=dt
    mas[0]=rightPart7(s3,s2,teta,gama)
    mas[1]=rightPart7(s3+0.5*h*mas[0],s2+0.5*h*mas[0],teta+0.5*h*mas[0],gama+0.5*h*mas[0])
    mas[2]=rightPart7(s3+0.5*h*mas[1],s2+0.5*h*mas[1],teta+0.5*h*mas[1],gama+0.5*h*mas[1])
    mas[3]=rightPart7(s3+h*mas[2],s2+h*mas[2],teta+h*mas[2],gama+h*mas[2])
    return mas
def rungeKut4(s3,s2,gama):
    mas=[0.0,0.0,0.0,0.0]
    h=dt
    mas[0]=rightPart8(s3,s2,gama)
    mas[1]=rightPart8(s3+0.5*h*mas[0],s2+0.5*h*mas[0],gama+0.5*h*mas[0])
    mas[2]=rightPart8(s3+0.5*h*mas[1],s2+0.5*h*mas[1],gama+0.5*h*mas[1])
    mas[3]=rightPart8(s3+h*mas[2],s2+h*mas[2],gama+h*mas[2])
    return mas
def rungeKut5(s1,teta,s3,s2,gama):
    mas=[0.0,0.0,0.0,0.0]
    h=dt
    mas[0]=rightPart9(s1,teta,s3,s2,gama)
    mas[1]=rightPart9(s1+0.5*h*mas[0],teta+0.5*h*mas[0],s3+0.5*h*mas[0],s2+0.5*h*mas[0],gama+0.5*h*mas[0])
    mas[2]=rightPart9(s1+0.5*h*mas[1],teta+0.5*h*mas[1],s3+0.5*h*mas[1],s2+0.5*h*mas[1],gama+0.5*h*mas[1])
    mas[3]=rightPart9(s1+h*mas[2],teta+h*mas[2],s3+h*mas[2],s2+h*mas[2],gama+h*mas[2])
    return mas
def rungeKut6(eps):
    mas = [0.0, 0.0, 0.0, 0.0]
    h = dt
    mas[0] = rightPart10(eps)
    mas[1] = rightPart10(eps + 0.5 * h * mas[0])
    mas[2] = rightPart10(eps + 0.5 * h * mas[1])
    mas[3] = rightPart10(eps + h * mas[2])
    return mas
def rungeKut7(v):
    mas = [0.0, 0.0, 0.0, 0.0]
    h = dt
    mas[0] = rightPart10(v)
    mas[1] = rightPart10(v+ 0.5 * h * mas[0])
    mas[2] = rightPart10(v + 0.5 * h * mas[1])
    mas[3] = rightPart10(v + h * mas[2])
    return mas




# Правые части
def rightPart1(Vector):
    return Vector

def rightPart2(Fe,Gx,Fs):
    temp=Fe/m+Gx+Fs/m
    return temp

def rightPart3(Mg,dH,Mf,Ma,l):
    temp=(-Mg-dH+Mf+Ma)/l
    return temp
def rightPart7(sigma3,sigma2,teta,gama):
    temp=(sigma3*sin(gama)-sigma2*cos(gama))/cos(teta)
    return temp
def rightPart8(sigma3,sigma2,gama):
    temp=sigma3*sin(gama)+sigma2*cos(gama)
    return temp
def rightPart9(sigma1,teta,sigma3,sigma2,gama):
    temp=sigma1+tan(teta)*(sigma3*sin(gama)-sigma2*cos(gama))
    return temp
def rightPart10(eps):

    return eps

# Ввод времени:

# Проверка введенного времени
per=0
time=100

new=input("Вводить управление вручную?(1-Да, 0-Нет)")

file=open('sistem.txt','w',encoding='utf-8')

data=''
times=''

try:
    new=int(new)
except:
    print("Error value")
if new!=1:
    time = input("Enter time:")
    try:
        time = double(time)
        t=0
    except:
        print("Value error!")
        exit()
if time<tMax or new==1:
    while t<time:
        if new==1:
            print("Введите stop, чтоб завершить!")
            for i in range(6):
                print("ε",i+1," = ",end="")
                eps=input()
                print()
                try:
                    eps=double(eps)
                    epsV[i]=eps
                except:
                    if eps=='stop':
                        exit()
                    eps=0

        # Присвоение знаений
        Vx=array[3]
        Vy = array[4]
        Vz = array[5]
        psi = array[6]
        teta = array[7]
        gama = array[8]
        sigma1 = array[9]
        sigma2 = array[10]
        sigma3 = array[11]
        w0 = array[12]
        w1 = array[13]
        w2 = array[14]
        w3 = array[15]
        w4 = array[16]
        w5 = array[17]

        # Нахождение вектора равнодействующей силы тяги
        # dot - функция numpy для скалярного произведения
        F0=dot(Kf*w0**2,e2)
        F1 = dot(Kf * w1 ** 2, e2)
        F2 = dot(Kf * w2 ** 2, e2)
        F3 = dot(Kf * w3 ** 2, e2)
        F4 = dot(Kf * w4 ** 2, e2)
        F5 = dot(Kf * w5 ** 2, e3)
        # print(F1)
        # Вектор равнодействующей силы тяги
        Fcck=VtoVFive(F0,F1,F2,F3,F4,F5)

        # print("Fcck = ",Fcck)

        Lpsi=[cos(psi/2),0,sin(psi/2),0]
        Lteta=[cos(teta/2),0,0,sin(teta/2)]
        Lgama=[cos(gama/2),sin(gama/2),0,0]

        # кватернионное утножение векторов поочередно?
        L=KvatrVect(Lpsi,Lteta)
        L=KvatrVect(L,Lgama) # вычисляемый кватернион ориентации  ССК  относительно ИСК
        Pcck=[0,Fcck[0],Fcck[1],Fcck[2]] # Кватернион с нулевой скалярной частью
        # print("L = ",L)
        LOb=[L[0],-L[1],-L[2],-L[3]]

        Fs=KvatrVect(L,Pcck)
        Fs=KvatrVect(Fs,LOb)
        # print("Fs =",Fs)



        # Проекция силы сопротивления воздуха
        Fsx=-Ks*Vx**3
        Fsy = -Ks * Vy ** 3
        Fsz = -Ks * Vz ** 3
        FSV=[Fsx,Fsy,Fsz]

        # print("FSV =",FSV)

        H1=Lxx*sigma1
        H2=Lyy*sigma2+j*(w1-w2+w3-w4)+j0*w0
        H3=Lzz*sigma3+j*w5
        HV=[H1,H2,H3]# Вектор кинетического момента
        SV=[sigma1,sigma2,sigma3]# Вектор угловой скорости
        Mg=VtoV(HV,SV,3) #Вычесляемый вектор гироскопического момента
        # print("MG =",Mg)





        dH1=0
        dH2=j*(eps1-eps2+eps3-eps4)+j0*eps0
        dH3=j*eps5
        dHV=[dH1,dH2,dH3]# Вектор производной кинетического момента

        # Вычесление сумарного аэродинамического момента

        MA0 = dot(Km0 * w0 ** 2, e2)
        MA1 = dot(Km * w1 ** 2, e2)
        MA2 = dot(Km * w2 ** 2, e2)
        MA3 = dot(Km * w3 ** 2, e2)
        MA4 = dot(Km * w4 ** 2, e2)
        MA5 = dot(Km * w5 ** 2, e2)
        MAs=VtoVFive(MA0,MA1,MA2,MA3,MA4,MA4)# Сложение покомпонентно векторов, вектор аэродинамического момента
        # print("MAs =",MAs)

        # Вычесление сумарного момента силы тяги двигателей

        Fp0 = VnaV(p0,F0)
        Fp1 = VnaV(p1, F1)
        Fp2 = VnaV(p2, F2)
        Fp3 = VnaV(p3, F3)
        Fp4 = VnaV(p4, F4)
        Fp5 = VnaV(p5, F5)
        MFV=VtoVFive(Fp0,Fp1,Fp2,Fp3,Fp4,Fp5)# Сложение покомпонентно векторов, вектор силы тяги двигателей
        # print("MFV =",MFV)


        ind=0
        ind1=0
        for i in range(n):
            # Условия заколнения вектора состояния
            if i<3:
                array[i]=rungeKutStep(array[i],rungeKut7(array[i+3]))
            if i>2 and i<6:
                array[i]=rungeKutStep(array[i],rungeKut1(Fs[ind+1],GV[ind],FSV[ind]))
                ind+=1
            if i == 6:
                array[i]=rungeKutStep(array[i],rungeKut3(sigma3,sigma2,teta,gama))
            if i == 7:
                array[i]=rungeKutStep(array[i],rungeKut4(sigma3,sigma2,gama))
            if i == 8:
                array[i]=rungeKutStep(array[i],rungeKut5(sigma1,teta,sigma3,sigma2,gama))
            if i>8 and i<12:
                array[i]=rungeKutStep(array[i],rungeKut2(Mg[ind1],HV[ind1],MFV[ind1],MAs[ind1],Lxyz[ind1]))
                ind1+=1
            if i>11:
                array[i]=rungeKutStep(array[i],rungeKut6(epsV[i-12]))
        # Вывод каждые 1 секунды

        if per%1000==0 or new==1:
            file.write('time:'+str(round(t,2))+'\n')
            file.write('X* = '+str(round(array[0],2))+'\n')
            file.write('Y* = '+str(round(array[1],2))+'\n')
            file.write('Z* = '+str(round(array[2],2))+'\n')
            file.write('Vx = '+str(round(array[3],2))+'\n')
            file.write('Vy = '+str(round(array[4],2))+'\n')
            file.write('Vz= '+str(round(array[5],2))+'\n')
            file.write('ѱ = '+str(round(array[6],2))+'\n')
            file.write('Ө = '+str(round(array[7],2))+'\n')
            file.write('γ = '+str(round(array[8],2))+'\n')
            file.write('Ω1 = '+str(round(array[9],2))+'\n')
            file.write('Ω2 = '+str(round(array[10],2))+'\n')
            file.write('Ω3 = '+str(round(array[11],2))+'\n')
            file.write('ώ0 = '+str(round(array[12],2))+'\n')
            file.write('ώ1 = '+str(round(array[13],2))+'\n')
            file.write('ώ2 = '+str(round(array[14],2))+'\n')
            file.write('ώ3 = '+str(round(array[15],2))+'\n')
            file.write('ώ4 = '+str(round(array[16],2))+'\n')
            file.write('ώ5 = '+str(round(array[17],2))+'\n\n\n')
            # print(times)
            # print("===================")
            # print("t = ", round(t,2), "с")
            # print()
            # print("Vx =", array[3])
            # print("Vy =", array[4])
            # print("Vz =", array[5])
            # print("ѱ =", array[6])
            # print("Ө =", array[7])
            # print("γ =", array[8])
            # print("Ω1 =", array[9])
            # print("Ω2 =", array[10])
            # print("Ω3 =", array[11])
            # print("ώ0 =", array[12])
            # print("ώ1 =", array[13])
            # print("ώ2 =", array[14])
            # print("ώ3 =", array[15])
            # print("ώ4 =", array[16])
            # print("ώ5 =", array[17])

        t+=dt
        per+=1

else:
    print("Error")
    exit()
print("The End===================")
print("Time =",time)
print("Vx =",array[3])
print("Vy =",array[4])
print("Vz =",array[5])
print("ѱ =",array[6])
print("Ө =",array[7])
print("γ =",array[8])
print("Ω1 =",array[9])
print("Ω2 =",array[10])
print("Ω3 =",array[11])
print("ώ0 =",array[12])
print("ώ1 =",array[13])
print("ώ2 =",array[14])
print("ώ3 =",array[15])
print("ώ4 =",array[16])
print("ώ5 =",array[17])
