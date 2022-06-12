
import os
import json
import facebook

os.environ['FACEBOOK_TEMP_TOKEN'] = "EAAFFaZBT4WtUBAK7zZCnCZBZC4azzMVInFAZBylk8EngSqpTBKia5nQZAOYEcftEgY16tIZAZChkHjXr7QvNo988wSVeAPwVoRZAMndMPKyk9Ki40fPwUPEufZB9nZBUHwVv1tOj8ajOyus4Mb3vLYAvCCD6WZBF26CpecZCx8xZBCZCBqv5vxHclRUUmGIW5bRS4RDYksZD"

class clsFBook():
    """description of class"""
    token = ""
    fields = []

    token = os.getenv('FACEBOOK_TEMP_TOKEN')
    #token = os.environ.get("FACEBOOK_TEMP_TOKEN")
    #token = os.environ["FACEBOOK_TEMP_TOKEN"]

    #print(os.environ)
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='first_name,location,link,email')
    print(json.dumps(profile,  indent=4))
    #friends = graph.get_connections("10218366275052919", "friends")
    print(json.dumps(profile, indent=4))
    
    fields = ['id', 'name', 'about', 'likes', 'band_members']

    fields = ','.join(fields)
    page_name = input("Enter a Page Name: ")

    page = graph.get_object(page_name, fields=fields)
    print(json.dumps(page, indent=4))


    pass # fim da classe