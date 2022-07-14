import base64

#I want that 500 THB voucher
secret = "aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K"
whatIsIt = base64.b64decode(secret)[::-1].decode("utf-8")
print(whatIsIt)