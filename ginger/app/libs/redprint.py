# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/17 17:21'


class RedPrint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)  # pythonic写法
            bp.add_url_rule(url_prefix+rule, endpoint, f, **options)



