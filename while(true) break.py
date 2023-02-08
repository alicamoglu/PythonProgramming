#kullanıcı adı parola
defusername = "ali"
defparola = "12"
while (True):
    username = input("username: ")
    parola = input("parolanız: ")
    if ((defusername == username) and (defparola == parola)):
        print("wellcome", username)
        break
    elif ((defusername != username) and (defparola == parola)):
        print("username is not accurate")
        break
    elif ((defusername == username) and (defparola != parola)):
        print("forgot parola?")
        print("parola renew? ( yes or no)")
        answer = input("please answer with yes or no to question if you the parola renew want:")
        if (answer == "yes"):
            new_parola = input("new parola")
            print("wait please")
            defparola = new_parola
            print("parola renew is successful")
        else:
            break # bu break olmasa kod tekrar başa dönmek suretiyle username soruyor yada ilk if scope'u da öyle
    else:
        print("tekrar deneyin")