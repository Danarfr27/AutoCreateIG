from Temporary.Data.data import *

class AccountsCenter:
    def __init__(self):
        self.r = requests.Session()
        self.info = {}
        
    def FollowMe(self, cookies):
       try:
           id_akun = '76915549395'
           self.r.headers.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                'x-csrftoken': re.search('csrftoken=(.*?);',str(cookies)).group(1),
                'cookie': cookies
            })
           resp = self.r.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format(id_akun))
           if '"challenge_required' in str(resp.text):
               return('* Gagal Follow Akun ID: {}'.format(id_akun))
           else:
               return('* Berhasil Follow Akun ID: {}'.format(id_akun))
       except (Exception) as e: return(f'*  Error Bot Auto Following: {str(e).title()}')
               
    def Open_pic(self, type_menu):
         list_path = []
         list_file = os.listdir(type_menu if type_menu == "profile_pic" or type_menu == "cover_pic" else "")
         for path in list_file:
             if path.lower().endswith(".png"):exten = ".png";list_path.append({"path":path, "exten":exten})
             elif path.lower().endswith(".jpg"):exten = ".jpg";list_path.append({"path":path, "exten":exten})
             else:continue
             return list_path
             
    def Change_Profile(self, cookies):
        try:
            folder_profile = self.Open_pic("profile_pic")
            pic_data = random.choice(folder_profile)
            compile_file = open("profile_pic/{}".format(pic_data['path']), "rb").read()
            body = {"content-disposition": "form-data", "name": "profile_pic","filename": "profilepic.jpg", "content-type": "image/jpeg"}
            self.r.headers.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                'x-csrftoken': re.search('csrftoken=(.*?);',str(cookies)).group(1),
                'cookie': cookies
            })
            data = {"profile_pic": bytes(compile_file)}
            resp = self.r.post("https://www.instagram.com/api/v1/web/accounts/web_change_profile_picture/",data=body,files=data)
            if '"changed_profile":true' in str(resp.text):
                return('* Berhasil Menambahkan Foto Profile')
            else: return('* Gagal Menambahkan Foto Profile')
        except (Exception) as e: return(f'* Error Menambahkan Foto Profile: {str(e).title()}')
        
    def Add_Bio_Profile(self, email, fullname, username, cookies):
        try:            
            biog = 'Dev Knowing Is Here'
            self.r.headers.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                'x-csrftoken': re.search('csrftoken=(.*?);',str(cookies)).group(1),
                'cookie': cookies
            })
            body = {
                "biography": biog,
                "chaining_enabled": "on",
                "email": email,
                "external_url": "",
                "first_name": fullname,
                "phone_number": "",
                "username": username,
                "jazoest": "22773"
            }
            resp = self.r.post("https://www.instagram.com/api/v1/web/accounts/edit/", data=body)
            if '"status":"ok"' in str(resp.text):
                return(f'* Berhasil Menambahkan Bio Profile: {biog}')
            else: return(f'* Gagal Menambahkan Bio Profile: {biog}')
        except (Exception) as e: return(f'* Error Menambahkan Bio Profile: {str(e).title()}')

    def Aktifkan2F(self, cookies, url='https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
        try:
            curl = self.r.get(url, cookies={'cookie': cookies}).text
            head = {
                'host': 'accountscenter.instagram.com',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                'x-ig-app-id': '1217981644879628'
            }
            body = {
                'av': re.search('{"actorID":"(\d+)"', str(curl)).group(1),
                '__d': 'www',
                '__user': '0',
                '__a':'1',
                '__req': 'h',
                '__hs': re.search('"haste_session":"(.*?)"', str(curl)).group(1),
                'dpr': '2',
                '__ccg': 'GOOD',
                '__rev': re.search('{"consistency":{"rev":(\d+)}', str(curl)).group(1),
                '__s': '',
                '__hsi': re.search('"hsi":"(\d+)"', str(curl)).group(1),
                '__dyn': '',
                '__csr': '',
                '__comet_req': re.search('__comet_req=(\d+)', str(curl)).group(1),
                'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(curl)).group(1),
                'jazoest': re.search('jazoest=(\d+)', str(curl)).group(1),
                'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                '__spin_r': re.search('"__spin_r":(\d+)', str(curl)).group(1),
                '__spin_b': 'trunk',
                '__spin_t': re.search('"__spin_t":(\d+)', str(curl)).group(1),
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                'variables': json.dumps({"input":{"client_mutation_id": re.search('{"clientID":"(.*?)"}',str(curl)).group(1),"actor_id": re.search('{"actorID":"(\d+)"', str(curl)).group(1),"account_id": re.search('{"actorID":"(\d+)"', str(curl)).group(1),"account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
                'doc_id':'6282672078501565'
            }
            resp = self.r.post('https://accountscenter.instagram.com/api/graphql/', data=body, headers=head, cookies={'cookie':cookies}).text
            if "totp_key" in str(resp):
                 key_text = re.search('"key_text":"(.*?)"', str(resp)).group(1)
                 key_rep = key_text.replace(' ','')
                 kode = self.r.get(f'https://2fa.live/tok/{key_rep}').json()['token']
                 self.info.update({'SecretKey': key_rep})
                 self.Konfirmasi2F(cookies, kode, curl)
            else:
                 self.info.update({'SecretKey':'Tidak Ada'})
                 self.info.update({'success-a2f': False})
                 self.info.update({'kode-pemulihan':'Tidak Ada'})
        except AttributeError as e:
            self.info.update({'SecretKey':'Tidak Ada'})
            self.info.update({'success-a2f': False})
            self.info.update({'kode-pemulihan':'Tidak Ada'})
        return self.info  
        
    def Konfirmasi2F(self, cookies, kode, curl):
        try:
            head = {
                'host': 'accountscenter.instagram.com',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
                'x-ig-app-id': '1217981644879628'
            }
            body = {
                'av': re.search('{"actorID":"(\d+)"', str(curl)).group(1),
                '__d': 'www',
                '__user': '0',
                '__a':'1',
                '__req': 'h',
                '__hs': re.search('"haste_session":"(.*?)"', str(curl)).group(1),
                'dpr': '2',
                '__ccg': 'GOOD',
                '__rev': re.search('{"consistency":{"rev":(\d+)}', str(curl)).group(1),
                '__s': '',
                '__hsi': re.search('"hsi":"(\d+)"', str(curl)).group(1),
                '__dyn': '',
                '__csr': '',
                '__comet_req': re.search('__comet_req=(\d+)', str(curl)).group(1),
                'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(curl)).group(1),
                'jazoest': re.search('jazoest=(\d+)', str(curl)).group(1),
                'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                '__spin_r': re.search('"__spin_r":(\d+)', str(curl)).group(1),
                '__spin_b': 'trunk',
                '__spin_t': re.search('"__spin_t":(\d+)', str(curl)).group(1),
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorEnableTOTPMutation','variables': json.dumps({"input":{"client_mutation_id": re.search('{"clientID":"(.*?)"}',str(curl)).group(1),"actor_id": re.search('"actorID":"(\d+)"', str(curl)).group(1),"account_id": re.search('"actorID":"(\d+)"', str(curl)).group(1),"account_type":"INSTAGRAM","verification_code": kode,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
                'server_timestamps':'true',
                'doc_id':'7032881846733167'
            }
            resp = self.r.post('https://accountscenter.instagram.com/api/graphql/', data=body, headers=head, cookies={'cookie':cookies}).text
            if '"success":true' in str(resp):
                 self.info.update({'success-a2f': 'True'})
                 body1 = {
                     'av': re.search('{"actorID":"(\d+)"', str(curl)).group(1),
                     '__d': 'www',
                     '__user': '0',
                     '__a':'1',
                     '__req': 'h',
                     '__hs': re.search('"haste_session":"(.*?)"', str(curl)).group(1),
                     'dpr': '2',
                     '__ccg': 'GOOD',
                     '__rev': re.search('{"consistency":{"rev":(\d+)}', str(curl)).group(1),
                     '__s': '',
                     '__hsi': re.search('"hsi":"(\d+)"', str(curl)).group(1),
                     '__dyn': '',
                     '__csr': '',
                     '__comet_req': re.search('__comet_req=(\d+)', str(curl)).group(1),
                     'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(curl)).group(1),
                     'jazoest': re.search('jazoest=(\d+)', str(curl)).group(1),
                     'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                     '__spin_r': re.search('"__spin_r":(\d+)', str(curl)).group(1),
                     '__spin_b': 'trunk',
                     '__spin_t': re.search('"__spin_t":(\d+)', str(curl)).group(1),
                     'fb_api_caller_class': 'RelayModern',
                     'fb_api_req_friendly_name': 'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation',
                     'variables': json.dumps({"input":{"client_mutation_id": re.search('{"clientID":"(.*?)"}',str(curl)).group(1),"actor_id": re.search('"actorID":"(\d+)"', str(curl)).group(1),"account_id": re.search('"actorID":"(\d+)"', str(curl)).group(1),"account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}),
                     'doc_id':'24010978991879298'
                 }
                 head1 = {
                     'host': 'accountscenter.instagram.com',
                     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                     'content-type': 'application/x-www-form-urlencoded',
                     'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                     'x-fb-friendly-name': 'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation'
                 }
                 reco = self.r.post('https://accountscenter.instagram.com/api/graphql/', data=body1, headers=head1, cookies={'cookie':cookies}).text
                 if '"success":true' in str(reco):
                     code = re.search('"recovery_codes":(.*?)}', str(reco)).group(1)
                     self.info.update({'kode-pemulihan': code})
                 else: self.info.update({'kode-pemulihan':'-'})
            else:
                self.info.update({'success-a2f': False})
                self.info.update({'kode-pemulihan':'Tidak Ada'})
        except AttributeError as e:
            self.info.update({'success-a2f': False})
            self.info.update({'kode-pemulihan':'Tidak Ada'})
        return self.info