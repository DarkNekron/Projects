import random

R_AREA = "You can find Sony Authorized Stores at https://www.sony.co.in/microsite/retailshops/"
R_LOCAL = "Yes! Ofcourse you can go to any of the Sony Authorized Stores or your Local Dealer for better Experience!"
R_THANKYOU = 'You\'re welcome! For more info, you can contact us at 18001037799 or at our Website: https://web.sony-asia.com/in/contact-us/?cid=gwt:footer:contactus, Do you want to conclude this Session?'
R_ORDER = 'To view our Headphones range, you can visit us at https://www.sony.co.in/headphones/headband'


def unknown():
    response = ["Could you please re-write that? ",
                "...",
                "Sorry, I can not understand you.",
                "What does that mean?"][
        random.randrange(4)]
    return response
