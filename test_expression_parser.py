from expression_parser import Parser
from tokens import Token
from tokens import TokenType as Type


class TestExpressions:
	def test_parsing_number(self):
		tokens = Parser.parse('5')

		assert tokens == [Token(Type.Number.INT, lexeme='5')]

	def test_parsing_addition(self):
		tokens = Parser.parse('100 + 2')

		assert tokens == [Token(Type.Number.INT, lexeme='100'), Token(Type.Operator.PLUS, lexeme='+'),
		                  Token(Type.Number.INT, lexeme='2')]

	def test_parsing_many_operations(self):
		tokens = Parser.parse('10 + 2 - 1 * 0 / 0')

		assert tokens == [Token(Type.Number.INT, lexeme='10'), Token(Type.Operator.PLUS, lexeme='+'),
		                  Token(Type.Number.INT, lexeme='2'), Token(Type.Operator.MINUS, lexeme='-'),
		                  Token(Type.Number.INT, lexeme='1'), Token(Type.Operator.STAR, lexeme='*'),
		                  Token(Type.Number.INT, lexeme='0'), Token(Type.Operator.BAR, lexeme='/'),
		                  Token(Type.Number.INT, lexeme='0')]


class TestRelations:
	def test_parsing_equation(self):
		tokens = Parser.parse('1 + 1 = 2')

		assert tokens == [Token(Type.Number.INT, lexeme='1'), Token(Type.Operator.PLUS, lexeme='+'),
		                  Token(Type.Number.INT, lexeme='1'), Token(Type.Relation.EQUAL, lexeme='='),
		                  Token(Type.Number.INT, lexeme='2')]

	def test_parsing_other_relations(self):
		tokens = Parser.parse('= != < <= > >=')

		assert tokens == [Token(Type.Relation.EQUAL, lexeme='='),  Token(Type.Relation.BANG_EQUAL, lexeme='!='),
		                  Token(Type.Relation.LESS, lexeme='<'), Token(Type.Relation.LESS_EQUAL, lexeme='<='),
		                  Token(Type.Relation.GREATER, lexeme='>'), Token(Type.Relation.GREATER_EQUAL, lexeme='>=')]


class TestVariables:
	def test_parsing_many_single_letter_variables(self):
		tokens = Parser.parse('y = m * x + n')

		assert tokens == [Token(Type.Symbol.VAR, lexeme='y'), Token(Type.Relation.EQUAL, lexeme='='),
		                  Token(Type.Symbol.VAR, lexeme='m'), Token(Type.Operator.STAR, lexeme='*'),
		                  Token(Type.Symbol.VAR, lexeme='x'), Token(Type.Operator.PLUS, lexeme='+'),
		                  Token(Type.Symbol.VAR, lexeme='n')]
