class Token:
	def __init__(self, token_type: 'TokenType', lexeme: str):
		self.token_type = token_type
		self.lexeme = lexeme

	def __eq__(self, other) -> bool:
		return self.token_type == other.token_type and self.lexeme == other.lexeme

	def __repr__(self) -> str:
		return f"<{self.token_type}:'{self.lexeme}'>"


class TokenType:
	class Relation:
		EQUAL = 'Relation.Equal'

	class Number(enumerate):
		INT = 'Number.Int'

	class Operator(enumerate):
		PLUS = 'Operator.Plus'
		MINUS = 'Operator.Minus'
		STAR = 'Operator.Star'
		BAR = 'Operator.Bar'
