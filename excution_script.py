import pandas as pd
import numpy as np
import datetime

def Excutioner(ticker):
  x=np.array(pd.read_csv("https://finance.google.com/finance/getprices?q="+ticker+"&i=60&p=1d&f=d,c,h,l,o,v",skiprows=7,header=None))
  date=[]
  for i in range(0,len(x)):
      if x[i][0][0]=='a':
         t= datetime.datetime.fromtimestamp(int(x[i][0].replace('a','')))
         date.append(t)
      else:
         date.append(t+datetime.timedelta(minutes =int(x[i][0])))
  data1=pd.DataFrame(x,index=date)
  data1.columns=['a','Open','High','Low','Close','Vol']
  result = {'Open':data1['Open'], 'High':data1['High'], 'Low':data1['Low'], 'Close':data1['Close']}
  frame = pd.DataFrame(data=result)
  frame.to_csv('Excelfile_name.csv', sep=',')
  print "Done!!"


if __name__ == "__main__":
  Excutioner(sys.argv[1])
  
