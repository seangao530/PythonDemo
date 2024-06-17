import turtle as t
import random					# 加载随机模块

t.color('black', 'blue')		# 

t.pencolor('black')
t.fillcolor('cyan')
t.speed(0)
t.tracer(0)						# 关闭屏幕刷新
t.ht()      

a = 280

for i in range(2800):
	color = (random.uniform(0, 1),
             random.uniform(0, 1),
             random.uniform(0, 1))    # 设置随机颜色
	t.fillcolor(color)
	t.begin_fill()
	for j in range(4):
		t.fd(a)
		t.lt(90)s
	a = a - 0.1
	t.lt(3)
	t.end_fill()

t.update()						# 强制屏幕刷新
t.done()


