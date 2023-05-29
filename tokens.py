class Token:
	def __init__(self, lexeme: str):
		self.lexeme = lexeme

	def __eq__(self, other):
		return self.lexeme == other.lexeme
