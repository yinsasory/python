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