#!/usr/bin/env python
# coding:UTF-8

import webapp2
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class PataHandler(BaseHandler):
    def get(self):
        self.render("pata.html")

    def post(self):
        word1 = self.request.get('word1')
        word2 = self.request.get('word2')
        if word1 is None or word2 is None:
            self.redirect('/pata')

        if len(word1) > len(word2):
            rest = word1[len(word2):]
        else:
            rest = word2[len(word1):]
        new_word = ''.join([char1 + char2 for char1, char2 in zip(word1, word2)])
        self.response.write(new_word + rest)
        self.render("pata.html")
