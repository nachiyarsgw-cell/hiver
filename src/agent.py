import argparse,csv
from .model import weak_intent
from .taxonomy import HIGH_RISK
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def run(message,pairs):
 texts=[r['customer_text'] for r in pairs]; vec=TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True); mat=vec.fit_transform(texts+[message]); sims=cosine_similarity(mat[-1],mat[:-1]).ravel(); idx=int(sims.argmax()); sim=float(sims[idx]); intent=weak_intent(message); esc=intent in HIGH_RISK or sim<0.20; reason='high_risk_intent' if intent in HIGH_RISK else ('low_retrieval_similarity' if sim<0.20 else '')
 reply=pairs[idx]['response_text'] if not esc else 'I’m sorry you’re having trouble. This request should be reviewed by a support specialist so the next step can be confirmed safely.'
 return {'intent':intent,'similarity':round(sim,3),'auto_handle':not esc,'decision':'auto_handle' if not esc else 'escalate','reason':reason,'reply':reply,'retrieved_customer':pairs[idx]['customer_text']}
if __name__=='__main__':
 p=argparse.ArgumentParser(); p.add_argument('--message',required=True); p.add_argument('--pairs',default='data/amazon_pairs.csv'); a=p.parse_args(); print(run(a.message,list(csv.DictReader(open(a.pairs,encoding='utf-8')))))
