import turtle as t

t.color('blue')					# 设置画笔的颜色为蓝色
t.speed(0)

for y in range(-500, 500, 40):  # 循环从-300 到 350之前，每次递增40
	t.pu()						# 抬起画笔
	t.goto(-120, 0)				# 画笔移动到位置(-100，0)
	t.pd()						# 放下画笔

	t.goto(0, y)				# 画笔前进到位置 (0, y)
	t.goto(120, 0)				# 画笔前进到位置 (100, 0)

t.color('red')
t.pensize(5)
t.pu()
t.goto(-50, 350)
t.pd()
t.goto(-50, -350)

t.pu()
t.goto(50, 350)
t.pd()
t.goto(50, -350)

t.done()