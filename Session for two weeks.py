import aminofix
import webbrowser
email = input('Email>>>')
password = input('password>>')
client = aminofix.Client()
webbrowser.open('https://aminoapps.com/')
input("Click ")
client.login(email=email, password=password)

# الحصول على الهيدرز
headers = client.headers

# طباعة الهيدرز
print("Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")