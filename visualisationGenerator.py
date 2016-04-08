import tkinter

def generate(maze):
	root = tkinter.Tk()
	canvas = tkinter.Canvas(width=800, height=800)
	canvas.pack()
	canvas.configure(scrollregion=(0, 0, 1000, 1000))

	paths = maze.paths
	dimensions = [maze.height, maze.width]
	start = maze.start
	finish = maze.finish

	size = 50
	offset = 50

	def draw_border_lines():
		canvas.create_line(offset, offset, 
				dimensions[0]*size + offset, offset)
		canvas.create_line(offset, dimensions[1]*size + offset, 
			dimensions[0]*size + offset, dimensions[1]*size + offset)
		canvas.create_line(offset, offset, 
				offset, dimensions[1]*size + offset)
		canvas.create_line(dimensions[0]*size + offset, offset, 
			dimensions[1]*size + offset, dimensions[0]*size + offset)


	def draw_walls():
		for i in range(dimensions[0]):
			for j in range(dimensions[1]-1):
				if ((i, j), (i, j+1)) not in paths and ((i, j+1), (i, j)) not in paths:
					print("(" + str(i) + "," + str(j) + "),(" + str(i) + "," + str(j+1) + ")")
					canvas.create_line((j+1)*size+offset, i*size+offset, 
						(j+1)*size+offset, (i+1)*size + offset)

		for i in range(dimensions[0]-1):
			for j in range(dimensions[1]):
				if ((i, j), (i+1, j)) not in paths and ((i+1, j), (i, j)) not in paths:
					print("(" + str(i) + "," + str(j) + "),(" + str(i) + "," + str(j+1) + ")")
					canvas.create_line(j*size+offset, (i+1)*size+offset, 
						(j+1)*size+offset, (i+1)*size + offset)


	def draw_ends():
		canvas.create_oval(start[0]*size + 0.25*size + offset, start[1]*size + 0.25*size + offset, 
			start[0]*size + 0.75*size + offset, start[1]*size + 0.75*size + offset, fill="green")
		canvas.create_oval(finish[0]*size + 0.25*size + offset, finish[1]*size + 0.25*size + offset, 
			finish[0]*size + 0.75*size + offset, finish[1]*size + 0.75*size + offset, fill="red")

	draw_border_lines()
	draw_walls()
	draw_ends()
	root.mainloop()
