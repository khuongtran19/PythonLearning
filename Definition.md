Numbers: Store numerical information and come in two form:
- Integers - Whole Numbers
- Floating Point - Numbers with a decimal

String: Ordered sequence of characters

Lists: Ordered sequence of objects (mutable)

Tuples: Ordered sequence of objects (immutable)

Dictionary: Key-Value pairing that is unordered

*args and **kwargs
*args stand for arguments
**kwargs stand for key word arguments

LEGB Rule:
- L: Local - name assigned in any way within a function (def or lambda), and not declared global in the function.
- E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
- G: Global (module) - Names assigned at the top-level of a module file, or declared global in a def within the file.
- B: Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError,...

Error:
- try: This is the block of code to be attemped (may lead to error)
- except: Block of code will execute in case there is an error in try block
- finally: A final block of code to be executed, regardless of an error
