#import the re module
import re

#create a function to take in the user's phone input and returns if it matches the format pattern (xxx-xxx-xxxx)
def verify_phone(phone):
    pattern = r'\d{3}-\d{3}-\d{4}'
    return re.match(pattern, phone)

#create a function to take in the user's ssn input and returns if it matches the format pattern (xxx-xx-xxxx)
def verify_ssn(ssn):
    pattern = r'\d{3}-\d{2}-\d{4}'
    return re.match(pattern, ssn)

#create a function to take in the user's zip code input and returns if it matches the format pattern (xxxxx)
def verify_zip_code(zip_code):
    pattern = r'\d{5}'
    return re.match(pattern, zip_code)

#asks the user for their phone, ssn and zip code in the correct format.
def main():
    phone = input("Enter your phone number (xxx-xxx-xxxx): ")
    ssn = input("Enter your Social Security Number (xxx-xx-xxxx): ")
    zip = input("Enter your zip code ( xxxxx ): ")

    #gets the match condition by running the verify functions, and informs the user on whether or not their input was validated.
    if verify_ssn(ssn):
        print('Social Security Number verified.')
    else:
        print('Error getting Social Security Number. Ensure correct format and try again.')

    if verify_phone(phone):
        print('Phone number verified.')
    else:
        print('Error getting Phone Number. Ensure correct format and try again.')

    if verify_zip_code(zip):
        print('Zip code verified.')
    else:
        print('Error getting Zip Code. Ensure correct format and try again.')

main()