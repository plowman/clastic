from __future__ import unicode_literals

from clastic import (Application,
                     default_response,
                     GetParamMiddleware)
from clastic.session import CookieSessionMiddleware
from clastic.tests.common import session_hello_world
from clastic.middleware import SimpleContextProcessor

from pprint import pformat
import time
import sys


def see_modules(start_time, module_list, name=None):
    name = name or 'world'
    return (('Hello, %s, this app started at %s and has the following'
             ' modules available to it: \n\n%s')
            % (name, start_time, pformat(sorted(module_list))))


def create_decked_out_app():
    resources = {'start_time': time.time(),
                 'module_list': sys.modules.keys()}
    middlewares = [GetParamMiddleware(['name', 'date', 'session_id']),
                   CookieSessionMiddleware(),
                   SimpleContextProcessor('name')]
    routes = [('/', session_hello_world, default_response),
              ('/modules/', see_modules, default_response)]
    return Application(routes, resources, None, middlewares)


if __name__ == '__main__':
    create_decked_out_app().serve()
