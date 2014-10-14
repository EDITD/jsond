# jsond

An extension of json: but one that (naively) handles dates.


## Installation

You can use pip. (Note that it uses `setuptools`)
```
pip install jsond
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
