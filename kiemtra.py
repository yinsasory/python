class StudentDataStore:
    def __init__(self):
        self.data = {}
    
    def add_or_update_student(self, student_id, student_name, student_info):
        self.data[student_id] = {"name": student_name, **student_info}
        print(f"Thông tin sinh viên với mã {student_id} và tên {student_name} đã được lưu.") 
    
    def get_student_by_id(self, student_id):
        return self.data.get(student_id, "Không tìm thấy sinh viên với mã này!")
    
    def update_student(self, old_student_id, new_student_id, new_student_name, updated_info):
        if old_student_id in self.data:
            if old_student_id != new_student_id:
                self.data[new_student_id] = self.data.pop(old_student_id)
            self.data[new_student_id].update({"name": new_student_name, **updated_info})
            print(f"Thông tin sinh viên với mã {new_student_id} đã được cập nhật.")
        else:
            print("Không tìm thấy sinh viên với mã này để sửa!")
    
    def delete_student(self, student_id):
        if student_id in self.data:
            del self.data[student_id]
            print(f"Đã xóa sinh viên với mã {student_id}.")
        else:
            print("Không tìm thấy sinh viên với mã này để xóa!")
    
    def show_all_students(self):
        if self.data:
            for student_id, student_info in self.data.items():
                print(f"Mã sinh viên: {student_id}, Thông tin: {student_info}")
        else:
            print("Không có dữ liệu sinh viên nào.")


def input_student_info():
    student_id = input("Nhập mã sinh viên: ")
    student_name = input("Nhập tên sinh viên: ")
    
    while True:
        try:
            age = int(input("Nhập tuổi sinh viên: "))
            break
        except ValueError:
            print("Tuổi phải là một số. Vui lòng nhập lại.")
    
    major = input("Nhập ngành học của sinh viên: ")
    
    return student_id, student_name, {"age": age, "major": major}


def main():
    student_store = StudentDataStore()
    
    while True:
        print("\nChọn thao tác:")
        print("1. Thêm sinh viên")
        print("2. Sửa thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm sinh viên theo mã")
        print("5. Hiển thị toàn bộ sinh viên")
        print("6. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == "1":
            student_id, student_name, student_info = input_student_info()
            student_store.add_or_update_student(student_id, student_name, student_info)
        
        elif choice == "2":
            old_student_id = input("Nhập mã sinh viên hiện tại để sửa: ")

            if student_store.get_student_by_id(old_student_id) == "Không tìm thấy sinh viên với mã này!":
                print("Sinh viên không tồn tại.")
            else:
                new_student_id, new_student_name, updated_info = input_student_info()
                student_store.update_student(old_student_id, new_student_id, new_student_name, updated_info)
        
        elif choice == "3":
            student_id = input("Nhập mã sinh viên để xóa: ")
            student_store.delete_student(student_id)
        
        elif choice == "4":
            student_id = input("Nhập mã sinh viên để tìm: ")
            print(student_store.get_student_by_id(student_id))
        
        elif choice == "5":
            student_store.show_all_students()
        
        elif choice == "6":
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


main()
