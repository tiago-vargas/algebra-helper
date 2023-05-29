from tokens import Token


class Parser:
	@classmethod
	def parse(cls, expression: str) -> list[Token]:
		components = expression.split(sep=' ')
		tokens = []
		for string in components:
			tokens.append(Token(lexeme=string))
		return tokens
