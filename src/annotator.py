import streamlit as st,pandas as pd
from pathlib import Path
p=Path('data/gold_set.csv'); df=pd.read_csv(p)
intents=['account_access','billing_payment','order_delivery','refund_return','prime_subscription','product_purchase','device_setup','app_service_failure','connectivity','content_media','feature_howto','security_privacy','other_escalate']
i=st.number_input('Example index',0,len(df)-1,0)
r=df.iloc[int(i)]
st.title('AmazonHelp Gold Set Review')
st.info('Seed label shown below is only a starting point. Review it before calling the set hand-labelled.')
st.write('### Customer message'); st.info(r.customer_text)
st.write('### Historical AmazonHelp reply'); st.write(r.response_text)
st.write('Suggested label:',r.gold_intent)
label=st.selectbox('Gold intent',intents,index=intents.index(r.gold_intent) if r.gold_intent in intents else 0)
notes=st.text_area('Labeler notes',value='')
if st.button('Save this label'):
 df.loc[int(i),'gold_intent']=label; df.loc[int(i),'label_status']='HUMAN_REVIEWED'; df.to_csv(p,index=False); st.success('Saved.')
