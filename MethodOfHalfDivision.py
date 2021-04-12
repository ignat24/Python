from math import *
from tkinter import *


def grafic():
    def stop():
        lst = root.grid_slaves()
        for l in lst:
            l.destroy()
    
    def Function(x):
        # return 2*x**2-4*x+16/x
        return (4 * x + 0.5 * x ** 2) * log(x) - 0.25 * x ** 2 - 8 * x
        # return (1 / 3) * x ** 3 + (3 / 2) * x ** 2 - 4 * x + 3
        # return (4*x-0.25)*atan(x)-x**3/12-0.75
        # return -0.75*x*(x-1.5)*(x-2.7)*(x-3)+1;

    def MethodOfHalfDivision(a, b,delta):
        stop()
        k = 0
        x = 0

        print("k", "| ", "x1", "  | ","xm"," |  ", "x2", "  | ", "f(x1)"," |  f(xm)  |"," f(x2)  ", "|     ", "[a,b]", "       |  ",
              "Lk")
        while (b - a) >= delta:
            if k>100: break
            k += 1
            Lk=b-a
            xm=(a+b)/2
            x1=a+Lk/4
            x2=b-Lk/4
            Fm=Function(xm)
            F1=Function(x1)
            F2=Function(x2)
            if F1<Fm:
                b=xm
                xm=x1
            if F1>Fm and F2<Fm:
                a=xm
                xm=x2
            if F1>Fm and F2>Fm:
                a=x1
                b=x2
            L=b-a
            
            print(k, "|", round(x1, 3),"|", round(xm, 3), "| ", round(x2, 3), " |", round(Function(x1), 3), "|", round(Fm, 3),"|",
                  round(Function(x2), 3), "|", "[", round(a, 3), ",", round(b, 3), "]", "|", round(L, 3))
           
            x = (round(x1,3) + round(x2,3)) / 2


        f = Frame(root, bg="#FFEFD5", relief="groove")  # GROOVE)
        label1 = Label(f, bg=color5, text="X = "+str(round(x, 4)), font='Times 20')
        label2 = Label(f, bg=color5, text="F(x) ="+str(round(Function(x), 4)), font='Times 20')
        label1.grid(row=1,column=1,pady=20,padx=50)
        label2.grid(row=2,column=1,pady=20,padx=50)
        f.grid()
        print("X* =", round(x, 4))
        print("F(X*) =", round(Function(x), 4))
            
            
    color5 = "#FFEFD5"
    root = Tk()
    root["bg"] = "#FFEFD5"
    root.title("Polovinne Dilenny")
    root.geometry("400x400")
    f = Frame(root, bg="#FFEFD5", relief="groove")  # GROOVE)
    label0 = Label(f, bg=color5, text="Polovinne Dilenny ", font='Times 30 bold')
    label1 = Label(f, bg=color5, text="a:", font='Times 20')
    entry1 = Entry(f, font='Times 20', bg=color5)
    label2 = Label(f, bg=color5, text="b:", font='Times 20')
    entry2 = Entry(f, font='Times 20', bg=color5)
    label4 = Label(f, bg=color5, text="delta:", font='Times 20')
    entry4 = Entry(f, font='Times 20', bg=color5)
    btnEnter = Button(f, text="Next", font='Times 20 bold',command = lambda:MethodOfHalfDivision(float(entry1.get()),float(entry2.get()),float(entry4.get())))
    label0.grid(row=0,column=1,padx=20,pady=20)
    label1.grid(row=1,column=0)
    entry1.grid(row=1,column=1)
    label2.grid(row=2,column=0)
    entry2.grid(row=2,column=1)
    # label3.grid(row=3, column=0)
    # entry3.grid(row=3, column=1)
    label4.grid(row=4, column=0)
    entry4.grid(row=4, column=1)
    btnEnter.grid(row=5,column=1)
    f.grid()
    root.mainloop()


grafic()
