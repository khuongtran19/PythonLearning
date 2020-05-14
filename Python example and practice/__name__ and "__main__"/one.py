# one.py

def func():
    print('FUNC() in ONE.PY')

print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('ONE.py has been imported!')

#python one.py
#TOP LEVEL IN ONE.PY
#ONE.PY is being run directly!