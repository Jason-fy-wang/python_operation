
code = """
def coder():
    print("This is a code generator function.")
    return "code"
"""
## exec can dynamic define code 
exec(code, globals())

result = coder()
print(f"result from generate code: {result}")

code = "lambda: 1 + 2"

## eval use to evaluate sing expression
result = eval(code)()
print(f"result from generate code: {result}")

result = eval("1 + 4")
print(f"result from generate code: {result}")