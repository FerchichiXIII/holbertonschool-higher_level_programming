#!/usr/bin/python3
"""python-inheritance"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
	"""class square"""

	def __init__(self, size):
		"""init"""
		super().__init__(size, size)
		self.__size = size
