from Temporary.Data.data import *

class Encrypt_PWD:
    def __init__(self) -> None:
        pass
        
    def signature(self, data,ig_sig_key="SIGNATURE",ig_sig_key_version="4"):
        if ig_sig_key.isdigit():
            body=(hmac.new(ig_sig_key.encode("utf-8"),json.dumps(data).encode("utf-8"),hashlib.sha256).hexdigest()+"."+urllib.parse.quote(json.dumps(data)))
            return "signed_body={}&ig_sig_key_version={}".format(body,ig_sig_key_version)
        else:
            body=ig_sig_key+"."+urllib.parse.quote(json.dumps(data))
            if ig_sig_key_version is not None:return "signed_body={}&ig_sig_key_version=".format(body,ig_sig_key_version)
            return "signed_body={}".format(body)
            
    def MOBILE_CFG(self,user_agent=None,ig_sig_key="SIGNATURE",ig_sig_key_version=None):
        byps = requests.Session()
        try:
            b={
                "bool_opt_policy":"0",
                "mobileconfigsessionless":"",
                "api_version":"3",
                "unit_type":"1",
                "query_hash":"6894cdfea7fb5941e14847d18d1cf2d7c6679cec82e4f786a48fb6a7ace73131",
                "device_id":None,
                "fetch_type":"ASYNC_FULL",
                "family_device_id":None
}
            x=byps.post("https://www.instagram.com/api/v1/launcher/mobileconfig/",data=self.signature(data=b,ig_sig_key=ig_sig_key,ig_sig_key_version=ig_sig_key_version), headers={'user-agent': user_agent})
            public_key=x.headers.get("ig-set-password-encryption-pub-key")
            public_key_id=x.headers.get("ig-set-password-encryption-key-id")
            return public_key,public_key_id
        except (Exception) as e:
            return (None, None)
            
    def InstagramPWD(self, password=None,timestamp=None,public_key=None,public_key_id=None):
        timestamp=timestamp or str(datetime.datetime.now().timestamp())[:10]
        try:
            session_key=get_random_bytes(32)
            iv=get_random_bytes(12)
            decoded_publickey=base64.b64decode(public_key.encode())
            recipient_key=RSA.import_key(decoded_publickey)
            cipher_rsa=PKCS1_v1_5.new(recipient_key)
            rsa_encrypted=cipher_rsa.encrypt(session_key)
            cipher_aes=AES.new(session_key,AES.MODE_GCM,iv)
            cipher_aes.update(timestamp.encode())
            aes_encrypted,tag=cipher_aes.encrypt_and_digest(password.encode("utf8"))
            size_buffer=len(rsa_encrypted).to_bytes(2,byteorder="little")
            encrypted=base64.b64encode(b''.join([b'\x01',int(public_key_id).to_bytes(1,byteorder="big"),iv,size_buffer,rsa_encrypted,tag,aes_encrypted]))
            password=str(encrypted.decode("utf-8"))
            return "#PWD_INSTAGRAM:4:{}:{}".format(timestamp,password)
        except (Exception) as e:
            return "#PWD_INSTAGRAM:0:{}:{}".format(timestamp,password)