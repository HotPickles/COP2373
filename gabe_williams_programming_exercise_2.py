def main():

    #create my list of flagged spam words
    spam_word_list = [" now", " hurry", " chance", " order", " don't wait", " fast", " time", " winner", " win", " call", " free", " miss", " opportunity", " won't last long", " running out", " stock", " delay", " deadline", " limited", " alert", " offer", " off", " forget", " steps", " action", " security", " fraud", " investigated", " click", " bonus"]

    #create a function to use the previous list to execute the email scan
    def spam_scanner():

        #prompt the user to compose their email
        user_email = input("Compose")
        #change the email to lowercase so that regardless of capitalization the flagged words will be recognized
        user_email_lowercase = user_email.lower()

        #initialize the spam score and flagged words list
        spam_score = 0
        triggered_words = []

        #accumulate the number of flagged words into a spam_score count and add the words to the triggered_words list
        for word in spam_word_list:
            count = user_email_lowercase.count(word.lower())
            if count > 0:
                spam_score += count
                triggered_words.append(word)

        #give the emailer a score of how their email looked to the system
        if spam_score <= 1:
            likelihood_spam = "Low likelihood of spam"
        elif spam_score <= 3:
            likelihood_spam = "Moderate likelihood of spam"
        elif spam_score >= 4:
            likelihood_spam = "High likelihood of spam"

        #tell the user exactly how many words flagged the system
        print("\n" + "=" * 30)
        print(f"Total spam score: {spam_score}")
        #give the user a rating of their email's suspicion by the system
        print(f"Spam likelihood: {likelihood_spam}")

        #tell the user exactly which words were flagged by the system
        if triggered_words:
            print(f"Specific flagged words: {triggered_words}")
        else:
            print("No words were flagged as spam.")
        print("=" * 30)

    #run the scam scanner script
    spam_scanner()

#run the list and the scam scanner script
main()