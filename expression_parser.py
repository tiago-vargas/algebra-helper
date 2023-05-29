from tokens import Token


class Parser:
	@classmethod
	def parse(cls, expression: str) -> list[Token]:
		tokens = []

		lexemes = expression.split(sep=' ')
		for lexeme in lexemes:
			token_type = _get_token_type(lexeme)
			tokens.append(Token(token_type, lexeme))

		return tokens


def _get_token_type(lexeme: str) -> Token.Type:
	if lexeme == '+':
		return Token.Type.OPERATOR
	else:
		return Token.Type.NUMBER
