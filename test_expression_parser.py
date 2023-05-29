from expression_parser import Parser
from tokens import Token


class TestExpressions:
	def test_parsing_number(self):
		tokens = Parser.parse('5')

		assert tokens == [Token(lexeme='5')]

	def test_parsing_addition(self):
		tokens = Parser.parse('100 + 2')

		assert tokens == [Token(lexeme='100'), Token(lexeme='+'), Token(lexeme='2')]
