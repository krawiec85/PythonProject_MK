import chardet

with open('test.log', 'r', encoding='utf-8') as f:
    raw_data = f.read()

print(raw_data)

with open('test.log', 'rb') as f:
    raw_data = f.read()

print(raw_data)

result = chardet.detect(raw_data)
print(result)