from balance_parens import balance_parens

# Add more test cases!...
print(balance_parens("abc(d)e(fgh))(i)j)k") == "abc(d)e(fgh)(i)jk")
print(balance_parens("abc((d)e(fgh)(i)j(k") == "abc(d)e(fgh)(i)jk")
print(balance_parens(("()")) == "()")
print(balance_parens(("a(b)c)")) == "a(b)c")
print(balance_parens(("(a)(bdd)c)")) == "(a)(bdd)c")
print(balance_parens(("a(dbvb)c)")) == "a(dbvb)c")
print(balance_parens(("a(b)(c)())")) == "a(b)(c)()")
print(balance_parens((")(")) == "")
print(balance_parens(("(((((")) == "")
print(balance_parens((")(())(")) == "(())")
print(balance_parens(("(()()(")) == "()()")
print(balance_parens((")())(()()(")) == "()()()")

# Challenge: nested parentheses...
print(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p") == "abc(d)(ef(g(h))ij)klm()op")
print(balance_parens(")(())(") == "(())")