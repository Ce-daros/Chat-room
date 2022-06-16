import requests
print("Welcome to the chat room!")
usrname = input("Your username ")
while True:
    user_info = {'name': usrname, 'content': input("Say: ")}
    try:
        r = requests.post("http://127.0.0.1:5000/send", data=user_info)
    except:
        print("Failed")
    else:
        print(r.text)
    r = requests.get("http://127.0.0.1:5000/get_lastest")
    print(r.text)
    
    print(r.text[0])