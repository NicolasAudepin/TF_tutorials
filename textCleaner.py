import json

newFileName = 'Bendo.txt'

filelist = ['C:\\Users\\AUDEPIN\\Documents\\DataSet\\messages\\inbox\\levraibendo_dqhadtqkvg\\message_1.json',
        'C:\\Users\\AUDEPIN\\Documents\\DataSet\\messages\\inbox\\lesbailsextremes_6tuxzmegua\\message_1.json',
        'C:\\Users\\AUDEPIN\\Documents\\DataSet\\messages\\inbox\\theoldbendo_zit2qvup2a\\message_1.json']

messages=[]
n=0
for path_to_file in filelist:
    with open(path_to_file) as json_data:
        data = json.load(json_data)

    participants = []

    for part in data["participants"]:
        participants.append(part['name'])
    print(participants)


    
    for mess in data["messages"]:
        n+=1
        
        if('content' in mess):
            messages.append([mess['timestamp_ms'],
                        mess['sender_name'],
                        mess['content']
                    ])
        else:
            messages.append([mess['timestamp_ms'],
                        mess['sender_name'],
                        'PICTURE'])

    print (n)


def timestamp(mess):
    return(mess[0])
messages = sorted(messages,key=timestamp)
print(messages[0])



def MessageListToText(messagelist):
    txt = ""
    for message in messagelist:
        txt=txt+ "["+message[1]+"] "+message[2]+"\n"
    
    return txt

text = MessageListToText(messages)

newFile = open(newFileName,"w")

for letter in text:
    try:
        newFile.write(letter)
    except:
        n=0
        #print(letter)

newFile.close()