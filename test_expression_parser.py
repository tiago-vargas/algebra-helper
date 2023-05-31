from expression_parser import Parser
from tokens import Token
from tokens import TokenType as Type


class TestExpressions:
	def test_parsing_number(self):
		tokens = Parser.parse('5')

		assert tokens == [Token(Type.Number.INT, lexeme='5')]

	def test_parsing_addition(self):
		tokens = Parser.parse('100 + 2')

		assert tokens == [Token(Type.Number.INT, lexeme='100'), Token(Type.Operator.PLUS, lexeme='+'), Token(Type.Number.INT, lexeme='2')]
