email =input("Enter your email: ")#minimum letters in eamil= g@h.in '6 letters'
if len(email) >= 6:
    if email[0].isalpha():
        pass
    else:
        print("sorry, 1st letter of email takes alphabet only.")
  
else:
    print("wrong email!")
