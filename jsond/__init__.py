"""Just provide wrappers to the standard json functions but ones that can
handle dates.
"""
import json
import datetime

import dateutil.parser


class JSONDateEncoder(json.JSONEncoder):

    def default(self, obj):
        if type(obj) == datetime.date:
            # We want to ensure that we have a datetime.
            #
            obj = datetime.datetime.combine(obj, datetime.time.min)
        
        if isinstance(obj, datetime.datetime):
            return 'datetime:' + obj.isoformat()

        # We don't have a datetime, so we simply fall back to the json
        # encoder.
        #
        return json.JSONEncoder.default(self, obj)


class JSONDateDecoder(json.JSONDecoder):

    def str_to_datetime(self, s):
        try:
            # parse output from datetime.isoformat()
            #
            d = s.replace('datetime:', '')
            return dateutil.parser.parse(d)
        except ValueError:
            # Oops! However it could have been a string that happened to start
            # with 'datetime:'. So return that.
            #
            return s

    def _decode(self, data):
        if isinstance(data, basestring) and data.startswith('datetime:'):
            return self.str_to_datetime(data)

        if isinstance(data, list):
            return [self._decode(d) for d in data]

        if isinstance(data, dict):
            d = {}
            for key, value in data.iteritems():
                d[key] = self._decode(value)
            return d

        return data
    
    def decode(self, json_string):
        # First decode it using json.
        #
        decoded_obj = json.JSONDecoder.decode(json.JSONDecoder(), json_string)

        # Now check decoded object for any potential datetime objects within.
        #
        return self._decode(decoded_obj)



def dumps(*args, **kwargs):
    kwargs["cls"] = JSONDateEncoder
    return json.dumps(*args, **kwargs)


def loads(*args, **kwargs):
    kwargs["cls"] = JSONDateDecoder
    return json.loads(*args, **kwargs)


def dump(*args, **kwargs):
    kwargs["cls"] = JSONDateEncoder
    return json.dump(*args, **kwargs)


def load(*args, **kwargs):
    kwargs["cls"] = JSONDateDecoder
    return json.load(*args, **kwargs)
