import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True


        #def response(bot_response, list_of_words, single_response=False, required_words=[]):
        #nonlocal highest_prob_list
        #highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)




    # Counts how many words are present in each message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1



    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))


    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break


    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0



def check_all_messages(message):
    highest_prob_list = {}


    # Simplifies response creation / adds it to the dictionary
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses that are recorded.

    response('Hello! I\'m a Bot created to help you to buy Sony Headphones.', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response(long.R_ORDER, ['I', 'want', 'to', 'buy', 'headphones', 'Headphones'], required_words=['headphones'])
    response(long.R_THANKYOU, ['thank', 'thanks'], single_response=True)
    response('Thank you for contacting us!', ['Yes', 'I', 'Session', 'want'], required_words=['session'])

    # Longer responses
    response(long.R_LOCAL, ['local', 'advice'], required_words=['local'])
    response(long.R_AREA, ['area'], required_words=['area'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response




# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))