# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:24:37 2021

@author: ktyhz
"""

creditScore = 0

print('Hello,\nThis program calculates and displays your credit score. ')
print('-------------------------------------------------------')
print()


def main():
    phoneInput = phoneCheck()
    homeInput = homeCheck()
    accountInput = accountCheck()
    jobInput = jobCheck()
    residenceInput = residenceCheck()
    incomeAndDebtInput = debtPercentageCheck()
    confirmation(phoneInput, homeInput, accountInput, jobInput, residenceInput, incomeAndDebtInput)
    


def phoneCheck():  #This function calculates credit score according to phone criteria.

    global creditScore

    while True:
        phoneQuestion = input("Type 'Y' if you have phone on your name, type 'N' if you do not have: ")
        
        if phoneQuestion == 'Y' or phoneQuestion == 'y':
            creditScore += 5
            break
        elif phoneQuestion == 'N' or    phoneQuestion == 'n':
            break
        else:
            print("Invalid value. Please try again!")
            continue
    print('\n------------------------------------------------------\n------------------------------------------------------')
    
    return creditScore and phoneQuestion


def homeCheck(): #This function calculates credit score according to home criteria.
    
    global creditScore
    
    while True:
        homeQuestion = input("Type 'Y' if you have your own house, type 'N' if you do not have: ")
        
        if homeQuestion == 'Y' or homeQuestion == 'y':
            creditScore += 5
            break
        elif homeQuestion == 'N' or    homeQuestion == 'n':
            break
        else:
            print("Invalid value. Please try again!")
            continue
        
    print('\n------------------------------------------------------\n------------------------------------------------------')
    
    return creditScore and homeQuestion


def accountCheck(): #This function calculates credit score according to account or savings criteria.

    global creditScore
    
    while True:
        accountQuestion = input("Type 'Y' if you have savings or checking account, type 'N' if you do not have: ")
        
        if accountQuestion == 'Y' or accountQuestion == 'y':
            creditScore += 5
            break
        elif accountQuestion == 'N' or    accountQuestion == 'n':
            break
        else:
            print("Invalid value. Please try again!")
            continue

    print('\n------------------------------------------------------\n------------------------------------------------------')

    return creditScore and accountQuestion

    
def jobCheck(): #This function calculates credit score according to years at job criteria.
    
    global creditScore
    
    while True:
        
        
        try:
            yearsAtCurrentJob = float(input('How many years have you been working at your present job: '))
    
            if yearsAtCurrentJob < 0:
                print('Years at job can not be a negative number.\nPlease type again.')
                continue
            elif yearsAtCurrentJob < 2:
                break
                
            elif yearsAtCurrentJob < 4:
                creditScore += 3
                break
                
            else:
                creditScore += 5
                break
                
        except ValueError:
            print("Years at same job can not be a string!\nPlease enter a number!")
            continue
        
    print('\n------------------------------------------------------\n------------------------------------------------------')
         
    return creditScore and yearsAtCurrentJob
    
    
def residenceCheck(): #This function calculates credit score according to years at residence criteria.
    
    global creditScore
    
    while True:
        
        
        try:
            yearsAtCurrentResidence = float(input('How many years have you been living in your current residence: '))
    
            if yearsAtCurrentResidence < 0:
                print('Years in same residence can not be a negative number!\nPlease type again.')
                continue
            elif yearsAtCurrentResidence < 2:
                break
                
            elif yearsAtCurrentResidence < 4:
                creditScore += 3
                break
                
            else:
                creditScore += 5
                break
                
        except ValueError:
            print("Years in same residence can not be a string!\nPlease enter a number!")
            continue
        
    print('\n------------------------------------------------------\n------------------------------------------------------')
         
    return creditScore and yearsAtCurrentResidence

def debtPercentageCheck(): #This function calculates credit score according to income and debt criteria.
    
    global creditScore

    while True:
        
        try:
            income = float(input('Enter your total income: ')) 
            debt = float(input('Enter your total debt: ')) 
            
            incomeAndDebt = 'income: ' + str(income) + '    debt: '+ str(debt)
            
            if debt < 0 or income <= 0:
                print('Debt and income can not be negative number and income can not be zero!\nPlease enter again.')
                continue
            else:
                percentageOfDebt = (debt/income)*100
                
                if percentageOfDebt == 0:
                    creditScore += 10
                    break
        
                elif percentageOfDebt < 5:
                    creditScore += 5
                    break
                    
                elif percentageOfDebt < 25:
                    break
                    
                else:
                    creditScore -= 10
           

        except ValueError:
            print("Debt and income can not be a string!\nPlease enter a number.")
            continue
        
    print('\n------------------------------------------------------\n------------------------------------------------------')
         
    return creditScore and incomeAndDebt


def confirmation(phoneInput, homeInput, accountInput, jobInput, residenceInput, incomeAndDebtInput):
#This function shows user the values that he or she inputed. And asks he or she wants to make a change. 
#Respect to answer of the user, the program re-run again or displays the credit-score.

    global creditScore
    print("These are your answers: ")
    print("Have you got a phone on your name: ", phoneInput)
    print("Have you got your own house: ", homeInput )
    print("Have you got savings or checking accounts: ", accountInput)
    print("How many years have you been working at your current job: ", jobInput)
    print("How many years have you been living at your residence: ", residenceInput)
    print("How much is your income and debt: ", incomeAndDebtInput)
    
    while True:
            
        confirmation = input("Would you like to make a change?\nType 'Y' for change, or type 'N' to display your credit score: ")
        
        if confirmation == 'Y' or confirmation == 'y':
            creditScore = 0
            main()
            break
                
        elif confirmation == 'N' or confirmation == 'n':
            print("Your credit score is ",creditScore)
            
                
            while True:
                reRun = input("Do you want to calculate again?\nType 'Y' for yes, type 'N' for exit: ")
                    
                if reRun == 'Y' or reRun == 'y':
                    creditScore = 0
                    main()
                    break
                    
                elif reRun == 'N' or reRun == 'n':
                    break
                else: 
                    print("Invalid value. Try again!")
                    continue
            
            break
                
        else:
            print("Invalid value. Try again!")
            continue 

main()

print("Thank you for prefering us!")