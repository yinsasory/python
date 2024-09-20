import math
"""
#bai 1:
ID= input("nhap ma sinh vien: ")
Name = input("Nhap ten sinh vien: ")
Date= input("Ngay thang  nam sinh: ")
Sex = input("Gioi tinh: ")
classs= input("Lop: ")
majors= input("Nganh hoc: ")
print(ID,Name, Date,Sex,classs ,majors)




#bai 2
g=input()
x=input()
y=input()
z=input()

g_float = float(g)
x_float = float(x)
y_float = float(y)
z_float = float(z)

run = x_float + y_float + g_float + z_float

print(run,run%10,run//10)



#bai 3
num = input("Nhập một số có 4 chữ số: ")

if len(num) == 4 and num.isdigit():
    total = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
    print(f"Tổng các chữ số của {num} là: {total}")
else:
    print("Vui lòng nhập đúng một số có 4 chữ số.")
num_fl=float(num)
print(num_fl%10,num_fl//1000)


a= input("Nhap a: ")
b= input("Nhap b: ")
a_fl=float(a)
b_fl=float(b)
tong=a_fl+b_fl
hieu=a_fl-b_fl
tich=a_fl*b_fl
thuong=a_fl/b_fl
print (tong,hieu,tich,thuong,a_fl%b_fl,a_fl//b_fl)
"""

"""
#Buoi2:
print("ax^2+bx+c=0")
a= int(input("Enter a: "))
b=int(input("Enter b: "))
c= int(input("Enter c: "))
if(a!=0):
   denta=b**2-4*a*c
    if(denta>0):
        print("Phuong trinh co 2 nghiem: ")
        x1=(-b-denta**(1/2))/2*a
        x2=(-b+denta**(1/2))/2*a
        print("x1:",x1,"\n x2:",x2)
    elif(denta==0):
        print("Phuong trinh co nghiem kep: ")
        xn=-b/2*a
    elif(denta!=0):
         print("vo nghiem")
else:
    print("Phuong trinh sai moi nhap lai!")




#Bai1:
n=int(input("Nhap so keo: "))
m=int(input("Nhap so em be: "))
if(n%m==0):
    print("yes")
else:
    print("no")
#bai2:
n=int(input("thu may: "))
monhoc=("python","c++","js")
giangvien=("co huong","thay duc","thay minh")
phonghoc=("D701","D702","D703")
if(n==2):
    print(monhoc[0],"-",phonghoc[0],"-",giangvien[0])
elif(n==3):
    print(monhoc[1],"-",phonghoc[1],"-",giangvien[1])
elif(n==4):
    print(monhoc[2],"-",phonghoc[2],"-",giangvien[2])
else:
    print("tu hoc")
#bai3
n=int(input(""))
if(n<=50):
    tongtien=n*1678
    print("thanh tien: ",tongtien)
elif(n>=51 and n<=100):
    tongtien=1678*50+(n-50)*1734
    print("thanh tien: ",tongtien)
elif(n>=101 and  n<=200):
    tongtien=1678*50+1734*50+(n-100)*2014
    print("thanh tien: ",tongtien)
elif(n>=201 and n<=300):
    tongtien= 1678*50+1734*50+2014*100+(n-200)*2536
    print("thanh tien: ",tongtien)
elif(n>=301):
    tongtien= 1678*50+1734*50+2014*100+100*2536+(n-300)*2834
    print("thanh tien: ",tongtien)
#Bai4
n=int(input("nhap n: "))
int(s1=2022)
float(s2=1/1)
for i in range (2,n,2):
    s1=s1+n
for i in range (1,n):
    s2=s2+1/i*n
print("s1",s1,"s2",s2)
#bai5
n=int(input("nhap so muon lam bang: "))
for i in range (1,11):
    print(n,"x",i,"=",n*i,"\n")
#bai6
n=int(input("so virus hien co: "))
tongvirus=1
while (tongvirus>=1000000000):
    tongvirus=tongvirus*n
print(tongvirus)
#bai7
n=int(input("Nhap so can kiem tra: "))
if (n==1 or n==2):
    print("n la so nguyen to: ")
elif(n!=0 and n>0):
    for i in range(2,n,1):
        if(n%i==0):
            print(n,"khong phai so nguyen to")
        else:
            print(n,"la so nguyen to")
else:
    print("khong xac dinh")
#bai8
n=int(input("Nhap nam:"))
if(n%4==0):
    print("nam nhuan")
else:
    print("nam khong nhuan")
#bai9

n=input("Nhap thang:")
m=int(input("Nhap nam:"))
u=("1,3,5,7,9,10,12")
if (n=u):
    print("thang co 31 ngay")
elif(n=2 and m%4==0):
    print("Thang co 29 ngay")
elif(n=2 and m%4!=0):
    print("thang co 30 ngay")
else:
    print("thang co 30 ngay")

"""
#Buoi3
"""
def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm (nghiệm phức)"

def menu():
    a = b = c = None 

    while True:
        print("\n--- Menu ---")
        print("1. Nhập 3 hệ số a, b, c")
        print("2. Xác định nghiệm")
        print("3. Thoát")

        choice = input("Lựa chọn của bạn: ")

        if choice == '1':
            try:
                a = float(input("Nhập hệ số a: "))
                b = float(input("Nhập hệ số b: "))
                c = float(input("Nhập hệ số c: "))
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
        elif choice == '2':
            if a is None or b is None or c is None:
                print("Bạn cần nhập các hệ số trước khi xác định nghiệm.")
            elif a == 0:
                print("Đây không phải là phương trình bậc 2 (a không thể bằng 0).")
            else:
                result = giai_phuong_trinh_bac_hai(a, b, c)
                print(result)
        elif choice == '3':
            print("Thoát khỏi chương trình.")
            break
        elif choice == '4':
            
            S = input("Nhập chuỗi S: ")
            D = {}

            for char in S:
                if char in D:
                    D[char] += 1  # Nếu ký tự đã có trong từ điển, tăng giá trị thêm 1
                else:
                    D[char] = 1  # Nếu ký tự chưa có trong từ điển, gán giá trị ban đầu là 1

                print(D)

        elif choice == '5':
            x=input("Hay nhap mot chuoi: ")
            checking="!!!"
            if(checking in x):
                print("Chuoi da co dau cham than")
            else:
                print(x,"!!!")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

menu()
"""
"""
#Buoi4
import math
def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm (nghiệm phức)"

def menu():
    a = b = c = None 

    while True:
        print("\n--- Menu ---")
        print("1. Nhập 3 hệ số a, b, c")
        print("2. Xác định nghiệm")
        print("3. Thoát")

        choice = input("Lựa chọn của bạn: ")

        if choice == '1':
            try:
                a = float(input("Nhập hệ số a: "))
                b = float(input("Nhập hệ số b: "))
                c = float(input("Nhập hệ số c: "))
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
        elif choice == '2':
            if a is None or b is None or c is None:
                print("Bạn cần nhập các hệ số trước khi xác định nghiệm.")
            elif a == 0:
                print("Đây không phải là phương trình bậc 2 (a không thể bằng 0).")
            else:
                result = giai_phuong_trinh_bac_hai(a, b, c)
                print(result)
        elif choice == '3':
            print("Thoát khỏi chương trình.")
            break
        elif choice == '4':
            
            S = input("Nhập chuỗi S: ")
            D = {}

            for char in S:
                if char in D:
                     D[char] += 1  # Nếu ký tự đã có trong từ điển, tăng giá trị thêm 1
                else:
                    D[char] = 1  # Nếu ký tự chưa có trong từ điển, gán giá trị ban đầu là 1

                print(D)
                
                
        elif choice == '5':
            x=input("Hay nhap mot chuoi: ")
            checking="!!!"
            if(checking in x):
                print("Chuoi da co dau cham than")
            else:
                print(x,"!!!")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

menu()
"""