import turtle as t

t.speed(0)

t.pu()					# 抬起画笔
t.goto(150, 0)			# 移动画笔到（150，0）位置
t.pd()					# 放下画笔

t.color("deepskyblue")	# 设置画笔颜色为 deepskyblue
t.seth(135)				# 设置画笔方向为 135 度
t.begin_fill()			# 开始填色
for i in range(4):		# 循环四次
	t.fd(300)			# 画笔向前 300 像素
	t.lt(90)			# 画笔左转 90 度
t.end_fill()			# 结束填色

t.pu()					# 抬起画笔
t.goto(300, 0)			# 移动画笔到（300，0）位置
t.pd()					# 放下画笔

t.color("limegreen")	# 设置画笔颜色为 limegreen
t.seth(135)				# 设置画笔方向为 135 度
t.begin_fill()			# 开始填色
for i in range(4):		# 循环四次
	t.fd(300)			# 画笔向前 300 像素
	t.lt(90)			# 画笔左转 90 度
t.end_fill()			# 结束填色

t.pu()					# 抬起画笔
t.goto(150, 0)			# 移动画笔到（150，0）位置
t.pd()					# 放下画笔


t.color("slateblue")	# 设置画笔颜色为 slateblue
t.seth(135)				# 设置画笔方向为 135 度
t.begin_fill()			# 开始填色
for i in range(4):		# 循环四次
	t.fd(195)			# 画笔向前 300 像素
	t.lt(90)			# 画笔左转 90 度
t.end_fill()			# 结束填色


t.done()