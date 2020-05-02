# jsond

[![Build Status](https://travis-ci.org/EDITD/jsond.svg?branch=master)](https://travis-ci.org/EDITD/jsond)
[![Pypi Version](https://img.shields.io/pypi/v/jsond.svg)](https://pypi.org/project/jsond/)
[![Python Versions](https://img.shields.io/pypi/pyversions/jsond.svg)](https://pypi.org/project/jsond/)

An extension of json: but one that (naively) handles dates.


## Installation

You can use pip. (Note that it uses `setuptools`)
```
pip install jsond
```

To also install development tools use:
```
pip install jsond[dev]
# or
pip install -e .[dev]
```

## Simple Usage

I have a date.
```python
>>> import datetime
>>> my_date = datetime.datetime(2011, 3, 15, 0, 0, 0)
```

Standard `json` doesn't deal with dates :(
```python
>>> import json
>>> json.dumps(my_date)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.py", line 243, in dumps
    return _default_encoder.encode(obj)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/encoder.py", line 207, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/encoder.py", line 270, in iterencode
    return _iterencode(o, 0)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/encoder.py", line 184, in default
    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: datetime.datetime(2011, 3, 15, 0, 0) is not JSON serializable
```

But `jsond` will handle it
```python
>>> import jsond
>>> jsond.dumps(my_date)
'"datetime:2011-03-15T00:00:00"'
>>>
```

And we can pull the date back as well.
```python
>>> jsond.loads('"datetime:2011-03-15T00:00:00"')
datetime.datetime(2011, 3, 15, 0, 0)
>>> date2 = jsond.loads('"datetime:2011-03-15T00:00:00"')
>>> type(date2)
<type 'datetime.datetime'>
>>> date2 == my_date
True
>>> date2
datetime.datetime(2011, 3, 15, 0, 0)
>>>
```

Also, `jsond` will produce output that won't break `json`.
(Though of course, you'll get a string rather than a datetime object.)
```python
>>> enc = jsond.dumps(my_date)
>>> json.loads(enc)
u'datetime:2011-03-15T00:00:00'
>>>
```


## Other usage

Often message-processing systems will use json internally to serialise messages.

But that means that dates can't (easily) be used.

To help with this, we provide two functions: `from_json_serialisable_object`
and `to_json_serialisable_object`.

For those who prefer spelling serialise with a 'z', there are two 'alias'
functions for convenience.

- `from_json_serializable_object` -> `from_json_serialisable_object`
- `to_json_serializable_object` -> `to_json_serialisable_object`

```python
def handle_message(original_message):
    # At this stage original_message will be a dict, list etc, but it won't
    # have any datetime objects as it was json-serialisable.
    # We might have prepared it earlier with jsond.dumps, but that means that
    # we have 'datetime:...' string instead of datetime objects.
    message = jsond.from_json_serialisable_object(original_message)

    # message will now have datetime objects
    # We can do whatever processing we want.

    # Now we have to put message back on the queue. We have to output an
    # object that the broker will put back onto the queue etc.
    # So we can't have datetime objects. But we want to output an object
    # (not an encoded string).
    new_message = jsond.to_json_serialisable_object(message)

    # Now we can output/emit/etc new_message.
    return new_message
```
