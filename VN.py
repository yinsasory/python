import turtle

# Thiết lập cửa sổ vẽ
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("red")  # Phông nền màu đỏ
screen.title("Tung Lam (CLHShin)")

# Thiết lập người vẽ
pen = turtle.Turtle()
pen.speed(0.5)  # Tốc độ nhanh nhất
pen.color("yellow")  # Màu vàng cho ngôi sao
pen.fillcolor("yellow")  # Fill color cho ngôi sao

# Vẽ ngôi sao
pen.penup()
pen.goto(-50, 50)
pen.begin_fill()  # Bắt đầu fill màu

for _ in range(5):
    for _ in range(2):
        pen.forward(100)
        pen.right(144)
    pen.right(144)

pen.end_fill()  # Kết thúc fill màu

# Ẩn người vẽ và hiển thị kết quả
pen.hideturtle()
screen.mainloop()