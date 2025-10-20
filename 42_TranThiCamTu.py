# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    student = {"name": name, "year_of_birth": year_of_birth, "address": address}
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for s in student_list:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")

def search_student(search_name):
    print("--- KET QUA TIM KIEM ---")
    found_students = [s for s in student_list if search_name.lower() in s["name"].lower()]
    if not found_students:
        print("Khong tim thay sinh vien nao.")
    else:
        for s in found_students:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
            
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    
    # Yêu cầu 1: Thêm sinh viên
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    # Yêu cầu 2: In danh sách
    print("\n2. In danh sach sinh vien:")
    print_student_list()

    # Yêu cầu 3: Tìm kiếm
    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")
    
    print("\nTim kiem sinh vien theo ten 'Dung':")
    search_student("Dung")