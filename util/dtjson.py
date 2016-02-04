'''JSON dump/load with support for datetime objects.'''

from datetime import datetime, date
import re
import json
from io import StringIO

# datetime (and date) objects are dumped as strings prefixed with !!datetime,
# then fields (Y m d H M S Ms)
# Example:
#       "!!datetime  2010 7 30 14 30 56 0"
#       "!!date 2010 7 30

dt_prefix = '!!datetime '
d_prefix = '!!date '

fmt_dt = (
    dt_prefix +
    '{0.year} {0.month} {0.day} {0.hour} {0.minute} {0.second} {0.microsecond}'
).format

fmt_d = (d_prefix + '{0.year} {0.month} {0.day}').format

# type -> formatter
formatters = {
    datetime: fmt_dt,
    date: fmt_d,
}

is_dt = re.compile('^!!date(time)? ').search


def dt_handler(obj):
    '''
    >>> dt_handler(date(2013, 1, 2))
    '!!date 2013 1 2'
    >>> dt_handler(1)
    1
    '''
    fmt = formatters.get(type(obj))
    return fmt(obj) if fmt is not None else obj


def parse_dt(match, obj):
    '''
    >>> obj = '!!date 2013 1 2'
    >>> match = is_dt(obj)
    >>> parse_dt(match, obj)
    datetime.date(2013, 1, 2)
    >>> obj = '!!datetime 2013 1 2 3 4 5 6'
    >>> match = is_dt(obj)
    >>> parse_dt(match, obj)
    datetime.datetime(2013, 1, 2, 3, 4, 5, 6)
    '''
    cls = datetime if match.group() == dt_prefix else date
    # Trim prefix and create list of integer fields
    fields = [int(v) for v in obj[match.end():].split()]
    return cls(*fields)


def fix_dt(obj):
    '''Fix data/datetime values in obj, return generator of (key, value)

    >>> sorted(list(fix_dt({'x': '!!date 2013 1 2', 'y': 7})))
    [('x', datetime.date(2013, 1, 2)), ('y', 7)]
    '''
    for key, value in obj.iteritems():
        match = is_dt(value if isinstance(value, basestring) else '')
        if match:
            value = parse_dt(match, value)
        yield key, value


def object_hook(obj):
    '''Fix date/datetime values in obj, return new object.

    >>> object_hook({'x': '!!date 2013 1 2', 'y': 7})
    {'y': 7, 'x': datetime.date(2013, 1, 2)}
    '''
    return dict(fix_dt(obj))


def dump(obj, out):
    '''Dump `obj` to `out`, convert date/datetime objects to string
    representation.
    '''
    json.dump(obj, out, default=dt_handler, indent=4)


def load(fo):
    '''Load from `fo`, convert date/datetime from string representation to
    values.
    '''
    return json.load(fo, object_hook=object_hook)


def dumps(obj):
    '''Dump `obj` to string'''
    io = StringIO()
    dump(obj, io)
    return io.getvalue()


def loads(s):
    '''Load from `s` (string)'''
    io = StringIO(s)
    return load(io)


def _test():
    from doctest import testmod
    testmod()

if __name__ == '__main__':
    _test()
