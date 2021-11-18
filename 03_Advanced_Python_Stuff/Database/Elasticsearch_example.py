# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
from datetime import datetime
from elasticsearch import Elasticsearch
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Tue Oct  9 15:08:47 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        
        #Connect to Elasticsearch server
        es = Elasticsearch()

        doc = {
            'author': 'MJordi',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now(),
        }
        
        #Create an index and add data
        res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
        print(res['result'])
        
        #Read index
        res = es.get(index="test-index", doc_type='tweet', id=1)
        print(res['_source'])
        
        #Refreshing
        es.indices.refresh(index="test-index")
        
        #Searching
        res = es.search(index="test-index", body={"query": {"match_all": {}}})
        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
        
        
    except:
        traceback.print_exc()
