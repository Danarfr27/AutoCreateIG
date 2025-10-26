from Temporary.Data.data import *

class GeneratorEmail:
    def __init__(self):
        self.r = requests.Session()           
        
    def Timer(self, seconds):
        while seconds:
            mins, secs = divmod(seconds, 60)
            timeformat = '* Message Delay: {:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            seconds -= 1
            
    def MengambilEmail(self):
        try:
            doma = ["bltiwd.com","qzueos.com","vwhins.com","jxpomup.com","ibolinva.com",'wyoxafp.com',"osxofulk.com","jkotypc.com","cmhvzylmfc.com","zudpck.com","daouse.com","illubd.com","mkzaso.com","mrotzis.com","xkxkud.com","wnbaldwy.com"]
            body = {
                "name": ''.join((random.choice(string.ascii_lowercase + string.digits) for x in range(random.randint(4,10)))),
                "domain": random.choice(doma),
            }
            head = {
                "authority": "api.internal.temp-mail.io",
                "content-length": "488",
                "sec-ch-ua-platform": "\"Android\"",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
                "accept": "*/*",
                "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
                "application-version": "4.0.0",
                "x-cors-header": "iaWg3pchvFx48fY",
                "content-type": "application/json",
                "sec-ch-ua-mobile": "?1",
                "origin": "https://temp-mail.io",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://temp-mail.io/",
                "accept-encoding": "gzip, deflate",
                "accept-language": "id-ID,id;q=0.9",
                "cookie": "_ga_3DVKZSPS3D=GS2.1.s1755791620$o1$g1$t1755791689$j53$l0$h0",
                "priority": "u=1, i"
            }
            response = self.r.post('https://api.internal.temp-mail.io/api/v3/email/new', json=body, headers=head)
            self.email = response.json()['email']
            return(self.email, f'https://temp-mail.io/email/{self.email}')
        except (Exception) as e: return(None)
            
    def MengambilKode(self, email):
        try:
            head = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
                "accept": "*/*",
                "application-version": "4.0.0",
                "x-cors-header": "iaWg3pchvFx48fY",
                "content-type": "application/json",
                "sec-ch-ua-mobile": "?1",
                "priority": "u=1, i"
            }
            while True:
                response = self.r.get('https://api.internal.temp-mail.io/api/v3/email/{}/messages'.format(email),headers=head)
                if "Instagram" in response.text:
                    for resp in response.json():
                        self.kode = resp['subject'].split(' ')[0]
                        return(self.kode)
                        break
                else: return "Kosong!"
        except (Exception) as e:
            print(e)     