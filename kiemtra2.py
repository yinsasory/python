class personDataStore:
    def __init__(self):

        self.data = {}
    
    def add_or_update_person(self, person_id, person_name, person_info):
        self.data[person_id] = {"name": person_name, **person_info}
        print(f"Thông tin Kỹ sư với mã {person_id} và tên {person_name} đã được lưu.")

    def get_person_by_id(self, person_id):
        return self.data.get(person_id, "Không tìm thấy Kỹ sư với mã này!")
    
    
    def show_person_sorted_by_YearofGraduation_desc(self):
        if self.data:
            sorted_person = sorted(self.data.items(), key=lambda item: item[1]['YearofGraduation'], reverse=True)
            for person_id, person_info in sorted_person:
                print(f"Mã kỹ sư: {person_id}, Tên: {person_info['name']}, Tuổi: {person_info['YearofGraduation']}, Ngành học: {person_info['major']}")
        else:
            print("Không có dữ liệu sinh viên nào.")    
    def show_all_persons(self):
        if self.data:
            for person_id, person_info in self.data.items():
                print(f"Mã Kỹ sư: {person_id}, Thông tin: {person_info}")
        else:
            print("Không có dữ liệu Kỹ sư nào.")
class KySu(personDataStore):
    def __init__(self):
        super().__init__
        self.YearofGraduation=''
        self.major=''
    def inputEngineer(self):
        super().add_or_update_person 
        self.YearofGraduation
        self.major

def input_person_info():
    person_id = input("Nhập mã Kỹ sư: ")
    person_name = input("Nhập tên Kỹ sư: ")
    YearofGraduation = int(input("Nhập năm tốt nghiệp của Kỹ sư: "))
    major = input("Nhập ngành học của Kỹ sư: ")
    return person_id, person_name, {"YearofGraduation": YearofGraduation, "major": major}

def main():
    person_store = personDataStore()
    
    while True:
        print("\n-----Menu-----")
        print("1. Thêm Kỹ sư.")
        print("2. Tìm Kỹ sư theo mã.")
        print("3. Hiển thị toàn bộ Kỹ sư.")
        print("4. Hiển thị theo năm tốt nghiệp.")
        print("5. Thoát.")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == "1":
            person_id, person_name, person_info = input_person_info()
            person_store.add_or_update_person(person_id, person_name, person_info)
        
        elif choice == "2":
            person_id = input("Nhập mã Kỹ sư để tìm: ")
            print(person_store.get_person_by_id(person_id))
        
        elif choice == "3":
            person_store.show_all_persons()
            
        elif choice == "4":
            person_store.show_person_sorted_by_YearofGraduation_desc()
        
        elif choice == "5":
            print("Thoát chương trình.")
        
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


main()