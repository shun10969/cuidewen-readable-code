from slack_sdk import WebClient

client = WebClient(token='xoxb-247578397445-2237502186229-eld4CjB9UBfKCM0t2c5LHNOY')
#client.chat_postMessage(channel="myserver",text="djkhfjka")
r=client.files_upload(channel="myserver",file="./t.py")
print(r)