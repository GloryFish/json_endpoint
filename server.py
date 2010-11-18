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
    
    @cherrypy.expose
    def random(self):
        nums = [random.randint(0, 100) for i in range(10)]
        return json.dumps(nums)

    @cherrypy.expose
    def lorem(self, count=3):
        count = int(count)
        
        lipgen = lipsum.Generator()
        paragraphs = [lipgen.generate_paragraph() for i in range(count)]
        
        return json.dumps(paragraphs)

if __name__ == '__main__':
    cherrypy.quickstart(Endpoint())
    