from tokens import Token, TokenType


class Scanner:
	@classmethod
	def scan(cls, expression: str) -> list[Token]:
		tokens = []

		lexemes = expression.split(sep=' ')
		for lexeme in lexemes:
			token_type = _get_token_type(lexeme)
			tokens.append(Token(token_type, lexeme))

		return tokens


def _get_token_type(lexeme: str) -> TokenType:
	if lexeme == '+':
		return TokenType.Operator.PLUS
	elif lexeme == '-':
		return TokenType.Operator.MINUS
	elif lexeme == '*':
		return TokenType.Operator.STAR
	elif lexeme == '/':
		return TokenType.Operator.BAR
	elif lexeme == '=':
		return TokenType.Relation.EQUAL
	elif lexeme == '!=':
		return TokenType.Relation.BANG_EQUAL
	elif lexeme == '<':
		return TokenType.Relation.LESS
	elif lexeme == '<=':
		return TokenType.Relation.LESS_EQUAL
	elif lexeme == '>':
		return TokenType.Relation.GREATER
	elif lexeme == '>=':
		return TokenType.Relation.GREATER_EQUAL
	elif lexeme.isnumeric():
		return TokenType.Number.INT
	elif lexeme.isalpha():
		return TokenType.Symbol.VAR
