# 
#  videos.py
#  json_endpoint
#  
#  Created by Jay Roberts on 2010-11-22.
# 

import cherrypy
import json

class Videos(object):
    
    # Create a set of videos
    vids = [
        dict(
            vid=1,
            title="Fun times with friends",
        ),
        dict(
            vid=2,
            title="First birthday party",
        ),
        dict(
            vid=3,
            title="Opening night",
        ),
        dict(
            vid=4,
            title="Janet's concert footage",
        ),
        dict(
            vid=5,
            title="Learn to read",
        ),
    ]    

    @cherrypy.expose
    def index(self):
        '''Returns a list of videos'''
        return json.dumps(dict(videos = self.vids))
