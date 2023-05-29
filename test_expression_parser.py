from expression_parser import Parser
from tokens import Token


class TestExpressions:
	def test_parsing_number(self):
		tokens = Parser.parse('5')

		assert tokens == [Token(Token.Type.NUMBER, lexeme='5')]

	def test_parsing_addition(self):
		tokens = Parser.parse('100 + 2')

		assert tokens == [Token(Token.Type.NUMBER, lexeme='100'), Token(Token.Type.OPERATOR, lexeme='+'), Token(Token.Type.NUMBER, lexeme='2')]
