'''
Created on Mar 10, 2018

@author: ITAUser
'''
def tax(filing_status, income):
    
    if filing status == 'single':
        def tax (filling_status,income):

        if (income >= 0) and (income <=9275):
            tax = (0.1income)
        elif (income > 9275) and (income <= 37650):
            tax=(.19275+ 0.15(income-9275))
        elif (income > 37650) and (income<=91150):
            tax=(.19275+0.15(37650-9275)+.25(income-37650))
        elif (income > 91150) and (income <= 190150):
            tax=(.19275+0.15(37650-9275)+.25(91150-37650)+ .28(income-91151))
        elif (income > 190150) and (income<=190150):
            tax=(.19275+0.15(37650-9275)+.25(91150-37650)+ .28(190150-91151)+.33(income-190151)) 
        elif (income > 413351) and (income<=415050):
            tax=(.19275+0.15(37650-9275)+.25(91150-37650)+ .28(190150-91151)+.33(413350-190151)+.35(income-413351))
        elif (income > 415051):
            tax=(.19275+0.15(37650-9275)+.25(91150-37650)+ .28(190150-91151)+.33(413350-190151)+.35(415050-413351)+.396(income-415051))
    
        
if filling_status == "married filing jointly"
    if (income >= 0) and (income <=9275)
        tax = (0.1*income)
   
    if (income > 466951):
        tax += (income-415050)(.396)
        tax += 120529.75
    elif(415050 >= income > 413351):
        tax += (income-466950)(.35)
        tax += 119934.75
    elif(413350 >= income > 231451):
        tax += (income-413350)(.33)
        tax += 46278.75
    elif(190150 >= income > 151901):
        tax += (income-231450)(.28)
        tax += 18558.75
    elif(91150 >= income > 75301):
        tax += (income-151900)(.25)
        tax += 5183.75
    elif(37650 >= income > 18550):
        tax += (income-75300)(.15)
        tax += 927.5
    else:
        tax = (income)*(.1)
        
if filling_status == "widover"
    if (income >= 0) and (income <=9275)
        tax = (0.1*income)
   
    if (income > 466951):
        tax += (income-415050)(.396)
        tax += 120529.75
    elif(415050 >= income > 413351):
        tax += (income-466950)(.35)
        tax += 119934.75
    elif(413350 >= income > 231451):
        tax += (income-413350)(.33)
        tax += 46278.75
    elif(190150 >= income > 151901):
        tax += (income-231450)(.28)
        tax += 18558.75
    elif(91150 >= income > 75301):
        tax += (income-151900)(.25)
        tax += 5183.75
    elif(37650 >= income > 18550):
        tax += (income-75300)(.15)
        tax += 927.5
        
if filling_status == "married filing separately":
    if (income >= 0) and (income <=9275)
        tax = (0.1*income)
   
    if (income > 233476):
        tax += (income-415050)(.396)
        tax += 120529.75
    elif(415050 >= income > 206676):
        tax += (income-233475)(.35)
        tax += 119934.75
    elif(413350 >= income > 115726):
        tax += (income-206675)(.33)
        tax += 46278.75
    elif(190150 >= income > 75951):
        tax += (income-115725)(.28)
        tax += 18558.75
    elif(91150 >= income > 37650):
        tax += (income-37650)(.25)
        tax += 5183.75
    elif(37650 >= income > 9275):
        tax += (income-9275)(.15)
        tax += 927.5
    else:
        tax = (income)*(.1)
        
if filling_status == "head of household"

        if (income >= 0) and (income <=9275)
        tax = (0.1*income)
   
    if (income > 441001):
        tax += (income-415050)(.396)
        tax += 120529.75)
    elif(415050 >= income > 413351):
        tax += (income-441001)(.35)
        tax += 119934.75)
    elif(413350 >= income > 210801):
        tax += (income-413350)(.33)
        tax += 46278.75)
    elif(190150 >= income > ):
        tax += (income-91150)(.28)
        tax += 18558.75)
    elif(91150 >= income > 50401):
        tax += (income-130150)(.25)
        tax += 5183.75)
    elif(37650 >= income > 13251):
        ta0x += (income-9275)(.15)
        tax += 927.5-)
    else:
        tax = (income)*(.1)
        
def percent_of_tax(tax, income):
def is_valid(filing_status, income):
    
    all_valid = True 
    if(income < 0):
        return False 
    elif ((filing_status != "single")and 
          (filing_status != "married filing jointly")
          -)
    
    
return true 
    else 
def main(filing_status, income):
    print 