import os
import datetime

def check(oper, op1,op2):
    if oper=='+' or oper=='add:':
        return op1+op2
    if oper=='-' or oper=='sub:':
        return op1-op2
    if oper=='*' or oper=='mul:':
        return op1*op2
    if (oper=='/' or oper=='div:') and op2!=0:
        return op1/op2

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

abs_path=os.getcwd()
count_info=count_error=0
opertion_list=["+","-","*","/","add:","sub:","mul:","div:"]
txt="{}::{}::{}::{}\n"
with open(os.path.join(abs_path,'log.txt'),'w') as f:
    while True:
        str = input("Exprestion:")
        x = str.split()
        if x[0] in opertion_list:
            if is_number(x[1]) and is_number(x[2]):
                res=check(x[0],float(x[1]),float(x[2]))
                if res!=None:
                    count_info=count_info+1
                    f.write(txt.format(datetime.datetime.now(),'INFO',str,res))
                    print("Result:",'{:.3f}'.format(res))
                else:
                    count_error = count_error + 1
                    t = "Can't divide by 0"
                    print(t)
                    f.write(txt.format(datetime.datetime.now(), 'ERROR', t, str))
            else:
                count_error = count_error + 1
                t='Wrong operands'
                print(t)
                f.write(txt.format(datetime.datetime.now(), 'ERROR', t, str))
        else:
            count_error = count_error + 1
            t='This is not a basic mathematical operation'
            print(t)
            f.write(txt.format(datetime.datetime.now(), 'ERROR', t, str))
        print("Report: INFO-{}, ERROR-{}".format(count_info, count_error))

