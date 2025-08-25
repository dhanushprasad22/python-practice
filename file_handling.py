feedback= input("enter your feed back:")
with open ("feedback_log.txt","a")as log:
    log.write(feedback + "/n")
    print("thanks for feebback")