# -*- coding: utf-8 -*-
from meya import Component


class HelloWorld(Component):

    def start(self):
        text = ""
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
