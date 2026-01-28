def ticket_application(tickets_remaining, buyer_counter):
    
    #inputted requested ticket amount aassigned to an unverified variable
    purchase_check = int(input('How many tickets would you like to purchase? (max 4)'))
    
    #if the purchase is inelibigible than this will recognize it, find the problem, message the user and restart the process
    if purchase_check <= 0 or purchase_check >= 5 or purchase_check > tickets_remaining:
        
        #for if there is not enough tickets
        if purchase_check > tickets_remaining:
            print('We only have ' + str(tickets_remaining) + ' tickets left.')
            return(tickets_remaining, buyer_counter)
        
        #for if the user says they want 0 or negative tickets
        elif purchase_check <= 0:
            print('bye')
            return(tickets_remaining, buyer_counter)
        
        #for if the user says they want more than the alloted 4 tickets
        elif purchase_check >= 5:
            print('You may only buy a maximum of 4 tickets.')
            return(tickets_remaining, buyer_counter)
    
    #after purchase eligibility is verified a confirmed purchase veriable recieves the value
    purchase = purchase_check
    
    #records the tickets remaining and number of buyers
    tickets_remaining = tickets_remaining - purchase
    buyer_counter = buyer_counter + 1
    
    #information for the user after they successfully purchased tickets
    print('Here are your ' + str(purchase) + ' tickets!')
    print('There are ' + str(tickets_remaining) + ' tickets left.')
    
    #return the tickets remaining and buyer accumulator for the next cycle
    return(tickets_remaining, buyer_counter)

def main():
    
    #initialize buyer counter and tickets remaining outside of the while loops
    buyer_counter = 0
    tickets_remaining = 20
    #while loop to sell the tickets until there are none left
    while tickets_remaining > 0:
        tickets_remaining, buyer_counter = ticket_application(tickets_remaining, buyer_counter)
    #messages once the tickets are sold out and the loops have ended
    print('All tickets are sold out for now.')
    print(str(buyer_counter) + ' People bought tickets.')

main()