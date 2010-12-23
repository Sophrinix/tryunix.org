#!/usr/bin/env python
# encoding: utf-8

from web.core import Controller, RESTMethod

_all_ = ['RootController']

class Execute(RESTMethod):
    def get(self):
        return dict(template="tryunix.views.index", 
                    data=dict(title="Try Unix!", 
                              result="Please enter a command.",
                             )
                    )
                
    def post(self, command, *args):
        return dict(template="tryunix.views.index", 
                    data=dict(title="Try Unix - Command Result",
                              result=" ".join('Command:', command,
                                              'Args: ', repr(args)
                                             )
                              )
                    )
        
class RootController(Controller):
    index = Execute()    
    def about(self):
        return "Oh, well, uh... I'm made of python."



