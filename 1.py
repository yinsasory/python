array = []

n = int(input("Nhập số lượng phần tử muốn thêm vào mảng: "))

for i in range(n):
    element = input(f"Nhập phần tử thứ {i+1}: ")
    array.append(element)

print("Mảng sau khi đã thêm các phần tử:", array)
