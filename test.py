import hashlib

data = "hello world"
md5_test = hashlib.md5(data.encode()).hexdigest()
print(f"md5_test : {md5_test}")