from expression_parser import Parser
from tokens import Token


class TestExpressions:
	def test_parsing_number(self):
		tokens = Parser.parse('5')

		assert tokens == [Token(lexeme='5')]
