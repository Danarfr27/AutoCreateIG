from Temporary.Data.data import *
from Temporary.Penyimpanan.MainWblock import CreateIgWblock

class Main_Instagram:
    def __init__(self):
        self.r = requests.Session()
        self.InstagramMain()
        
    def clear_terminal(self):
        try: os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except: pass

    def InstagramMain(self):
        self.clear_terminal()
        while True:
            try: CreateIgWblock()
            except (Exception, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError) as e:
                print(f'* Error: {str(e).title()}')
                time.sleep(5)
                Main_Instagram()
            
if __name__=="__main__":
    try: os.mkdir('OK') or os.mkdir('CP')
    except: pass
    try: Main_Instagram()
    except (Exception) as e: exit(f'* Error: {str(e).title()}')
