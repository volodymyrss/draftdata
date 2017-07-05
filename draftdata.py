from collections import defaultdict
import yaml

draft_dir=None

rec_dd = lambda: defaultdict(rec_dd)

class DraftData(object):    
    def __init__(self,section="results"):
        self.section=section
    
    def __enter__(self):
        try:
            self.data=yaml.load(open(draft_dir+"/"+self.section+".yaml"))
        except:
            self.data=rec_dd()
        return self.data
        
    def __exit__(self, type, value, traceback):
        yaml.dump(self.data,open(draft_dir+"/"+self.section+".yaml","w"))                    

