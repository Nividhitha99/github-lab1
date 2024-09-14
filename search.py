import json
import re

def search_json(json_data, search_string):
       results = []
       for each_data in json_data:
           for key in each_data:
              if (re.search(search_string, key)):
            #if search_string in user_data:
                results.append({key: each_data[key]})
    
       return results

    
           



    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    # return results