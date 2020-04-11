from sys import argv
from PIL import Image

def breadthFirstSearch(maze):
	start = findStart(maze)
	size = maze.size
	

#finds the start of the maze and returns the index
def findStart(maze):
	return start


def main():
	#inputing the maze into an Image object
	filename = argv[1]
	mazeImage = Image.open(filename, 'r')

	#creates a list of the Image RGBA values
	mazePixels = mazeImage.load()
	print mazePixels[0,0] #TODO, remove this as debug
	#decide which ways to solve the maze and output


if __name__ == '__main__':
	main()