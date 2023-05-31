class Token:
	def __init__(self, token_type: 'TokenType', lexeme: str):
		self.token_type = token_type
		self.lexeme = lexeme

	def __eq__(self, other) -> bool:
		return self.token_type == other.token_type and self.lexeme == other.lexeme


class TokenType:
	class Symbol(enumerate):
		VAR = 'Symbol.Var'

	class Relation:
		EQUAL = 'Relation.Equal'
		BANG_EQUAL = 'Relation.BangEqual'
		LESS = 'Relation.Less'
		LESS_EQUAL = 'Relation.LessEqual'
		GREATER = 'Relation.Greater'
		GREATER_EQUAL = 'Relation.GreaterEqual'

	class Number(enumerate):
		INT = 'Number.Int'

	class Operator(enumerate):
		PLUS = 'Operator.Plus'
		MINUS = 'Operator.Minus'
		STAR = 'Operator.Star'
		BAR = 'Operator.Bar'
