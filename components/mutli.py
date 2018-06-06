from meya import Component
from meya.cards import Card

import re

class MultiText(Component):

    def start(self):
        messages = []        
        chunks = ["foo", "bar", "bazz", "bax", "john", "doe"]

        for chunk in chunks:
			      messages.append(self.create_message(text=chunk))
            
        return self.respond(messages=messages, action="next")