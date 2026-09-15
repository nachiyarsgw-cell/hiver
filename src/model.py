import re
from .taxonomy import KEYWORDS
def weak_intent(text):
 t=text.lower(); scores={k:sum(t.count(x) for x in kws) for k,kws in KEYWORDS.items()}
 if scores.get('security_privacy',0)>0: return 'security_privacy'
 b=max(scores,key=scores.get)
 return b if scores[b] else 'other_escalate'
def clean(text): return re.sub(r'\s+',' ',re.sub(r'http\S+|@\w+',' ',text.lower())).strip()
