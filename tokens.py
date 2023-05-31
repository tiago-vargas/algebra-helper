class Token:
	def __init__(self, token_type: 'Type', lexeme: str):
		self.token_type = token_type
		self.lexeme = lexeme

	def __eq__(self, other) -> bool:
		return self.token_type == other.token_type and self.lexeme == other.lexeme

	class Type:
		class Number(enumerate):
			INT = 'Number.Int'

		class Operator(enumerate):
			PLUS = 'Operator.Plus'
