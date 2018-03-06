import smtplib
import requests
		
def send_emails(emails,joke):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()

    sender_email="itstheclassicdad@gmail.com"
    try:
        server.login("itstheclassicdad@gmail.com", "Pha11ic@")
        print('login successful')
    except:
        print('Failed Autentication.')
        
    for name in emails:
        print('sending..')
        body = "Subject : Dad Joke of the Day\n\n"
        body += "Hi "+ emails[name] + ",\n\n"
        body += joke
        server.sendmail(sender_email,name,body)
    server.close()

def main():
	r = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})
	joke= r.json()
	jokeText = "" + joke['joke']
	
	emails={}
	emails["mcgonigb@tcd.ie"]="Bobby"
	emails["turnerro@tcd.ie"]="Ronan"
	emails["sarah.barron22@mail.dcu.ie"]="Sarah"
	emails["paward@tcd.ie"]="Patrick"
	send_emails(emails,jokeText)
main()