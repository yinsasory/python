import json
from tabulate import tabulate

class EmployeeDataStore:
    def __init__(self, file_name):
        self.data = {}
        self.file_name = file_name
        self.load_data_from_file()

    def load_data_from_file(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                self.data = json.load(file)
            print(f"Dữ liệu đã được nạp từ file {self.file_name}.")
        except FileNotFoundError:
            print(f"File {self.file_name} không tồn tại. Bắt đầu với dữ liệu rỗng.")
        except json.JSONDecodeError:
            print("File bị hỏng hoặc không đúng định dạng. Không thể nạp dữ liệu.")

    def save_data_to_file(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
        print(f"Dữ liệu đã được lưu vào file {self.file_name}.")

    def add_or_update_Employee(self, Employee_id, Employee_name, Employee_info):
        self.data[Employee_id] = {"name": Employee_name, **Employee_info}
        print(f"Thông tin Nhân viên với mã {Employee_id} và tên {Employee_name} đã được lưu.")
        self.save_data_to_file()

    def get_Employee_by_id(self, Employee_id):
        return self.data.get(Employee_id, "Không tìm thấy Nhân viên với mã này!")

    def update_Employee(self, Employee_id, new_Employee_name, updated_info):
        if Employee_id in self.data:
            self.data[Employee_id].update({"name": new_Employee_name, **updated_info})
            print(f"Thông tin Nhân viên với mã {Employee_id} đã được cập nhật.")
            self.save_data_to_file()
        else:
            print("Không tìm thấy Nhân viên với mã này để sửa!")

    def delete_Employee(self, Employee_id):
        if Employee_id in self.data:
            del self.data[Employee_id]
            print(f"Đã xóa Nhân viên với mã {Employee_id}.")
            self.save_data_to_file()
        else:
            print("Không tìm thấy Nhân viên với mã này để xóa!")

    def show_all_Employees(self):
        if self.data:
            table_data = []
            for Employee_id, info in self.data.items():
                basic_salary = info['basic_salary']
                work_days = info['work_days']
                allowance = info['allowance']
                health_insurance = info['health_insurance']
                tax = info['tax']

                salary = (basic_salary * work_days / 30) + allowance - health_insurance - tax

                table_data.append([
                    Employee_id, info['name'], info['position'], 
                    basic_salary, work_days, health_insurance, salary
                ])
            
            headers = ["Employee_ID", "Employee_name", "Chức vụ", "Lương cơ bản", "Ngày công", "BHYT", "Thực lĩnh"]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("Không có dữ liệu Nhân viên nào.")

def input_Employee_info():
    Employee_name = input("Nhập tên Nhân viên: ")
    
    while True:
        try:
            age = int(input("Nhập tuổi Nhân viên: "))
            break
        except ValueError:
            print("Tuổi phải là một số. Vui lòng nhập lại.")
    
    position = input("Nhập chức vụ của Nhân viên: ")
    
    while True:
        try:
            basic_salary = float(input("Nhập lương cơ bản: "))
            work_days = int(input("Nhập số ngày công: "))
            allowance = float(input("Nhập phụ cấp chức vụ: "))
            health_insurance = float(input("Nhập BHYT: "))
            tax = float(input("Nhập thuế thu nhập: "))
            break
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
    
    return Employee_name, {
        "age": age, 
        "position": position, 
        "basic_salary": basic_salary, 
        "work_days": work_days, 
        "allowance": allowance, 
        "health_insurance": health_insurance, 
        "tax": tax
    }

def main():
    Employee_store = EmployeeDataStore("employee_data.txt")
    
    while True:
        print("\nChọn thao tác:")
        print("1. Thêm Nhân viên")
        print("2. Sửa thông tin Nhân viên")
        print("3. Xóa Nhân viên")
        print("4. Tìm Nhân viên theo mã")
        print("5. Hiển thị toàn bộ Nhân viên")
        print("6. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == "1":
            Employee_id = input("Nhập mã Nhân viên: ")
            Employee_name, Employee_info = input_Employee_info()
            Employee_store.add_or_update_Employee(Employee_id, Employee_name, Employee_info)
        
        elif choice == "2":
            old_Employee_id = input("Nhập mã Nhân viên hiện tại để sửa: ")

            if Employee_store.get_Employee_by_id(old_Employee_id) == "Không tìm thấy Nhân viên với mã này!":
                print("Nhân viên không tồn tại.")
            else:
                new_Employee_name, updated_info = input_Employee_info()
                Employee_store.update_Employee(old_Employee_id, new_Employee_name, updated_info)
        
        elif choice == "3":
            Employee_id = input("Nhập mã Nhân viên để xóa: ")
            Employee_store.delete_Employee(Employee_id)
        
        elif choice == "4":
            Employee_id = input("Nhập mã Nhân viên để tìm: ")
            print(Employee_store.get_Employee_by_id(Employee_id))
        
        elif choice == "5":
            Employee_store.show_all_Employees()
        
        elif choice == "6":
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

main()