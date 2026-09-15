import argparse,csv,json,os
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,classification_report,confusion_matrix
from sklearn.pipeline import Pipeline
def main():
 p=argparse.ArgumentParser(); p.add_argument('--gold',required=True); p.add_argument('--out',default='reports/results'); a=p.parse_args(); os.makedirs(a.out,exist_ok=True)
 rows=[r for r in csv.DictReader(open(a.gold,encoding='utf-8')) if r.get('gold_intent')]
 if len(rows)<20: raise SystemExit('Need labelled gold_intent values before evaluation.')
 X=[r['customer_text'] for r in rows]; y=[r['gold_intent'] for r in rows]
 tr,te=train_test_split(range(len(y)),test_size=.25,random_state=42,stratify=y)
 maj=Counter(y[i] for i in tr).most_common(1)[0][0]; yt=[y[i] for i in te]; pred_maj=[maj]*len(te)
 pipe=Pipeline([('tfidf',TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True)),('lr',LogisticRegression(max_iter=2000,class_weight='balanced'))]); pipe.fit([X[i] for i in tr],[y[i] for i in tr]); pred=pipe.predict([X[i] for i in te])
 metrics={'n_labeled':len(rows),'test_size':len(te),'majority_accuracy':accuracy_score(yt,pred_maj),'majority_macro_f1':f1_score(yt,pred_maj,average='macro',zero_division=0),'tfidf_lr_accuracy':accuracy_score(yt,pred),'tfidf_lr_macro_f1':f1_score(yt,pred,average='macro',zero_division=0)}
 json.dump(metrics,open(os.path.join(a.out,'metrics.json'),'w'),indent=2); labels=sorted(set(y)); open(os.path.join(a.out,'classification_report.txt'),'w').write(classification_report(yt,pred,zero_division=0)); cm=confusion_matrix(yt,pred,labels=labels)
 with open(os.path.join(a.out,'confusion_matrix.csv'),'w',newline='') as f:
  w=csv.writer(f); w.writerow(['true/pred']+labels); [w.writerow([lab]+list(row)) for lab,row in zip(labels,cm)]
 print(json.dumps(metrics,indent=2))
if __name__=='__main__': main()
