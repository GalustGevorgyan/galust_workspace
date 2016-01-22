#!/usr/bin/python

import json
 
with open('cucumber.json') as json_file:
    json_data = json.load(json_file)
    for json_object in json_data:
        for element in  json_object['elements']:
            for steps_list in element['steps']:
                if steps_list['result']['status'] == 'failed':
                    print "Test case Failed " +steps_list['result']['status']
                    print steps_list['name']
                    for tag in element['tags']:
                        print 'Failed test cases tags ' + tag['name']
