# 문자 (single quotation / double quotation 의 차이 없음)

# single * 1
a = 'Hello, Python!'
print(a)

# single * 3
b = '''python's
Hello, World!        !!!!
    Hello, Python'''
print(b)

a = 'python\'s\nHello, World!'
print(a)

# \ : escape character

# double * 1
c = "python's\nHello, World!"
print(c)

c = "python's\nHello, \"World!\""
print(c)

# double * 3
d = """python's
"Hello, World!" """
print(d)

e = "c:\test"
print(e)

f = r"c:\test"
print(f)

# r = raw string : \를 문자로 인식

str01 = "Hello, "
str02 = "World!"
print(str01 + str02)
print(str01 * 3 + str02)

