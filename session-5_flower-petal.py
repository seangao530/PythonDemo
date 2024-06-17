import turtle as t

t.speed(0)				# 加快画笔的速度
	
for i in range(12):  	# 循环 12 次
	t.seth(i * 30)		# 设置画笔的方向
	t.circle(180, 100)	# 画一个半径180，弧度80的圆弧
	t.lt(80)			# 画笔左转 100 度
	t.circle(180, 100)	# 画一个半径180，弧度80的圆弧

t.done()