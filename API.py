

import Utils

def get_prediction(url, model):

    score = 180
    InTop1Million = False
    isOlderThan3Months = True


    try:
        # Finding Possible Target URLs
        print("Finding Target URLs...")
        target_urls = Utils.find_target_urls(url, 8)
    except:
        print("Error occurred while finding target URLs!")

    if Utils.check_top1million_database(url) or Utils.check_top1million_database_2(url):
        InTop1Million = True
    else:
        score-=10

    if InTop1Million:
        return score, InTop1Million, isOlderThan3Months

    
    if Utils.get_days_since_creation(url, 3) != True:
        print("Domain is less than 3 months old")
        isOlderThan3Months = False
        score -= 10

    

    return score, InTop1Million, isOlderThan3Months
