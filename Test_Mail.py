def mail_test(mail): 
    if mail.endswith("@gmail.com") or mail.endswith("@zohomail.in"):
        if mail[0].isalpha():
            return True
        else:
            return False
        return True

    else:
        return False
    
while True:
    mail = input("Enter your Mal: ")
    if mail_test(mail):
        print("valid mail")
    elif mail == "exit":
        print("Existing the Test Program")
        break
    else:
        print("invalid mail")
