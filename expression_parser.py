from tokens import Token, TokenType


class Parser:
	@classmethod
	def parse(cls, expression: str) -> list[Token]:
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
	else:
		return TokenType.Number.INT
