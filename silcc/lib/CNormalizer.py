import re
import sys
import csv
import nltk

from silcc.lib.util import CIList, capitalization_type
from silcc.lib.basictagger import BasicTagger

 
class CNormalize:
    
 
   
    def Normalize(self, text):
        '''
        Determines the type of capitilzation used:
        ALLCAPS - All words capitilized
        TITLE - First Letter capitalized
        P_TITLE - Few words in capital
        LOWER - All words lower cased
        
        to compensate for capital words like BTW, added them straight in stopwords
        '''
        fc_val=0        #Number of first Letters which are capital
        tc_val=0        #Number of Total Letters which are capita
        tc_cnt=0        #Total Count of letters except white spaces, includes punctuation marks
        
        tokens = text.split()   
        text_arr=list(text)
    
        for i in range(0,  len(text_arr)):
            if (text_arr[i].isalpha() and text_arr[i].islower() and text_arr[i-2] == '.' and text_arr[i-1] == ' '):
                text_arr[i] = text_arr[i].upper()
            if (text_arr[i] == 'i' and text_arr[i-1] == ' ' and text_arr[i+1] == ' '): # for small i
                text_arr[i] = 'I'
        text_arr[0] = text_arr[0].upper()
        text =''.join(text_arr)

               
        
      
        
        for tok in tokens:
            
            for i in range (0,  len(tok)):
                #if 
                tc_cnt+=1
                if (tok[i].upper() == tok[i] and tok[i].isalpha()):  #Checking for alphabet only, less punctuation gives a fake positive
                    tc_val+=1
                    if(i==0):
                        fc_val+=1
                
        #Metrics
        tc_frc = float(tc_val)/float(tc_cnt)
        fc_frc = float(fc_val)/float(len(tokens))
        
        
        #straight calls to functions to reduce comparison overhead
        #Only metric based, values can always be adjusted
        if tc_frc >= .8:
            return self.AllC(text)
        elif fc_frc >= .8:
            return self.TitleC(text)
        elif fc_frc >= .3:
            return self.P_Title(text)
        elif tc_frc <= .1:  
            return self.Lower(text)
        else:
            pass
        
    
    
    def TitleC(self,  text):
        print 'TitleC'
        return text
        #Convert to Sentence Case
     
    
    def P_Title(self,  text):
        print 'P_Title'
        return text
        #Convert all words which have First letter capitalization to full 
       
    def AllC(self,  text):
        print 'AllC'
        return text
        #Convert all to lower except for U.S.A type words
       
    def Lower(self, text):
        print 'Lower'
        return text
        #Attempt to find u.s.a words and capitalize them
      
    

if __name__ == '__main__':
    text = sys.argv[1]
    cn = CNormalize()
    text = cn.Normalize(text)
    print text


'''
Account for typos like TAg,  1) convert case if lower case is a dictionary match
'''
