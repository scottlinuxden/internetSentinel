import keyring
import getpass

keyring.set_password("internet_sentinel", "email_login_username", input("Enter your email login username: "))

done = False

entry = []

while not done:
    attempt = 0
    while attempt <= 2:
        try:
            if attempt == 0:
                prompt = 'Enter email login password: '
            else:
                prompt = "Re-enter email login password to confirm: "
            entry.append(getpass.getpass(prompt=prompt))
        except Exception as error:
            print('ERROR', error)
            del entry
            entry = []
            break
        else:
            attempt = attempt + 1
            if attempt == 2:
                if entry[0] == entry[1]:
                    done = True
                    break
                else:
                    del entry[1]
                    print("Passwords do not match!")
                    attempt = 1

keyring.set_password("internet_sentinel", "email_login_password", entry[0])

