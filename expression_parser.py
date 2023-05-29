from tokens import Token


class Parser:
	@classmethod
	def parse(cls, expression: str) -> list[Token]:
		return [Token(lexeme=expression)]
