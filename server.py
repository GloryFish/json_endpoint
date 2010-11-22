# 
#  server.py
#  json_endpoint
#
#  A simple server you can run locally which provides some different 
#  bits of data as JSON which you can use for testing JSON-consuming apps.
# 
#  Created by Jay Roberts on 2010-11-18.
#  Copyright 2010 GloryFish.org. All rights reserved.
# 

import cherrypy
import json
import random
import lipsum

class Endpoint:
    
    def __init__(self):
        random.seed()
        # Create a set of videos
        self.vids = []
        self.vids.append(dict(
            vid=1,
            title="Fun times with friends",
        ))
        self.vids.append(dict(
            vid=2,
            title="First birthday party",
        ))
        self.vids.append(dict(
            vid=3,
            title="Opening night",
        ))
        self.vids.append(dict(
            vid=4,
            title="Janet's concert footage",
        ))
        self.vids.append(dict(
            vid=5,
            title="Learn to read",
        ))
    
    
    
    @cherrypy.expose
    def random(self):
        '''Returns an array containing ten random integers from 0 to 100'''
        nums = [random.randint(0, 100) for i in range(10)]
        response = dict(random=nums)
        return json.dumps(response)

    @cherrypy.expose
    def lorem(self, count=3):
        '''Returns an array containing paragraphs of lorem ipsum text. Returns three paragraphs by default. Specify more or less in the url.'''
        count = int(count)
        
        lipgen = lipsum.Generator()
        paragraphs = [lipgen.generate_paragraph() for i in range(count)]
        
        return json.dumps(paragraphs)

    @cherrypy.expose
    def error(self):
        '''Returns a random HTTP error'''
        errors = [403, 404, 500]
        raise cherrypy.HTTPError(random.choice(errors))
    
    @cherrypy.expose    
    def videos(self):
        '''Returns a list of videos'''
        response = dict(videos = self.vids)
        return json.dumps(response)

    @cherrypy.expose
    def video(self, vid=1):
        vid = int(vid)
        video = [v for v in self.vids if v['vid'] == vid]
        
        return json.dumps(video)


if __name__ == '__main__':
    cherrypy.quickstart(Endpoint())
    