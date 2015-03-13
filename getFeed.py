from facepy import GraphAPI
from django.core.serializers.json import DjangoJSONEncoder
import json

group_id = "" #facebook group ID
access_token = "" #not needed for open groups

graph = GraphAPI(access_token)
pages = graph.get(group_id + "/feed", page=True, retry=3, limit=1)
i = 0
for p in pages:
    print 'Downloading page', i
    with open('content%i.json' % i, 'w') as outfile:
        json.dump(p, outfile, indent = 4, cls=DjangoJSONEncoder)
    i += 1