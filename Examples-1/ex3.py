INTEREST_RATE= .04
def main():
    principal=eval(input("Enter the amount of the deposit:"))
    numberofyears=eval(input("Enter the number of years:"))
    (bal,intearned)=balancedİnterest(principal,numberofyears)
    print("Balance: ${0:,.2f} İnterest Earned: $ {1:,.2f}".format(bal,intearned))

def balancedİnterest(prin,numYears):
    balance=prin * ((1+INTEREST_RATE)**numYears)
    interestEarned= balance-prin
    return (balance,interestEarned)

main()
