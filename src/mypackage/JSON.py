'''
Created on May 17, 2014

@author: Mark.E.Frymire
'''
import json


someJSON = ['foo', { 'bar': ('baz', None, 1.0, 2) } ]

json.dumps( someJSON )

print json.dumps("\"foo\bar")

print json.dumps(u'\u1234')

print json.dumps('\\')

print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)


# Pretty print some JSON
print
print json.dumps( {'4': 5, '6': 7}, sort_keys=True, indent=4, separators=(',', ': ') )


x = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print x
