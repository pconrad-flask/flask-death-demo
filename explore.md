A few things we can tell from session below.

* At the top level, the data (which we are accessing through variable `d`) has two keys: `meta` and `data`
* `d['data']` is a list of 10,296 rows, each of which is also a list.   Each of the rows is a list of 14 items.
* Here is a sample item from data, i.e. `d['data'][0]`
   ```
   [15029,
    '0E3080FB-5EF8-4BEF-834E-54B52DB8DFF3',
    15029,
    1534786069,
    '1099577',
    1534786069,
    '1099577',
    None,
    '2016',
    'Accidents (unintentional injuries) (V01-X59,Y85-Y86)',
    'Unintentional injuries',
    'Alabama',
    '2755',
    '55.5']
   ```

The next step is to try to use the information in `d['meta']` to make sense of the 14 fields in each of the rows 
of the `d['data']` array.

We note that the length of `d['meta']['view']['columns']` is exactly 14, which leads us to the not unreasonable
hypothesis that each of the items in that list is a description of one of the columns:

```
>>> type(d['meta']['view']['columns'])
<class 'list'>
>>> len(d['meta']['view']['columns'])
14
>>> 
```

So, looking deeper into `d['meta']['view']['columns']` we can start to decode these mysterious 14 items from `d['data'][0]`




```
169-231-87-146:explore pconrad$ python3 -i explore_death.py 
>>> type(d)
<class 'dict'>
>>> type(d.keys())
<class 'dict_keys'>
>>> keys = list(d.keys())
>>> len(keys)
2
>>> keys
['meta', 'data']
>>> d['meta']
{'view': {'id': 'bi63-dtpu', 'name': 'NCHS - Leading Causes of Death: United States', 'attribution': 'National Center for Health Statistics', 'averageRating': 0, 'category': 'NCHS', 'createdAt': 1449080633, 'description': 'This dataset presents the age-adjusted death rates for the 10 leading causes of death in the United States beginning in 1999.\r\n\r\nData are based on information from all resident death certificates filed in the 50 states and the District of Columbia using demographic and medical characteristics. Age-adjusted death rates (per 100,000 population) are based on the 2000 U.S. standard population. Populations used for computing death rates after 2010 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for non-census years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nCauses of death classified by the International Classification of Diseases, Tenth Revision (ICD–10) are ranked according to the number of deaths assigned to rankable causes. Cause of death statistics are based on the underlying cause of death.\r\n\r\nSOURCES\r\nCDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\r\n\r\nREFERENCES\r\n\r\n1. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\r\n\r\n2. Murphy SL, Xu JQ, Kochanek KD, Curtin SC, and Arias E. Deaths: Final data for 2015. National vital statistics reports; vol 66. no. 6. Hyattsville, MD: National Center for Health Statistics. 2017. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_06.pdf.', 'displayType': 'table', 'downloadCount': 54853, 'hideFromCatalog': False, 'hideFromDataJson': False, 'indexUpdatedAt': 1534786118, 'licenseId': 'PUBLIC_DOMAIN', 'newBackend': False, 'numberOfComments': 0, 'oid': 26650094, 'provenance': 'official', 'publicationAppendEnabled': False, 'publicationDate': 1503517561, 'publicationGroup': 5829091, 'publicationStage': 'published', 'rowClass': '', 'rowsUpdatedAt': 1534786071, 'rowsUpdatedBy': 's6ey-4vqh', 'tableId': 14417583, 'totalTimesRated': 0, 'viewCount': 23371, 'viewLastModified': 1534786063, 'viewType': 'tabular', 'columns': [{'id': -1, 'name': 'sid', 'dataTypeName': 'meta_data', 'fieldName': ':sid', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': -1, 'name': 'id', 'dataTypeName': 'meta_data', 'fieldName': ':id', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': -1, 'name': 'position', 'dataTypeName': 'meta_data', 'fieldName': ':position', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': -1, 'name': 'created_at', 'dataTypeName': 'meta_data', 'fieldName': ':created_at', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': -1, 'name': 'created_meta', 'dataTypeName': 'meta_data', 'fieldName': ':created_meta', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': -1, 'name': 'updated_at', 'dataTypeName': 'meta_data', 'fieldName': ':updated_at', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': -1, 'name': 'updated_meta', 'dataTypeName': 'meta_data', 'fieldName': ':updated_meta', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': -1, 'name': 'meta', 'dataTypeName': 'meta_data', 'fieldName': ':meta', 'position': 0, 'renderTypeName': 'meta_data', 'format': {}, 'flags': ['hidden']}, {'id': 317117533, 'name': 'Year', 'dataTypeName': 'number', 'description': '', 'fieldName': 'year', 'position': 1, 'renderTypeName': 'number', 'tableColumnId': 33023980, 'width': 148, 'cachedContents': {'largest': '2016', 'non_null': 10296, 'average': '2007.5', 'null': 0, 'top': [{'item': '2016', 'count': 20}, {'item': '2015', 'count': 19}, {'item': '2014', 'count': 18}, {'item': '2013', 'count': 17}, {'item': '2012', 'count': 16}, {'item': '2011', 'count': 15}, {'item': '2010', 'count': 14}, {'item': '2009', 'count': 13}, {'item': '2008', 'count': 12}, {'item': '2007', 'count': 11}, {'item': '2006', 'count': 10}, {'item': '2005', 'count': 9}, {'item': '2004', 'count': 8}, {'item': '2003', 'count': 7}, {'item': '2002', 'count': 6}, {'item': '2001', 'count': 5}, {'item': '2000', 'count': 4}, {'item': '1999', 'count': 3}], 'smallest': '1999', 'sum': '20669220'}, 'format': {'precisionStyle': 'standard', 'noCommas': 'true', 'align': 'right'}}, {'id': 317117534, 'name': '113 Cause Name', 'dataTypeName': 'text', 'description': '', 'fieldName': '_113_cause_name', 'position': 2, 'renderTypeName': 'text', 'tableColumnId': 33023981, 'width': 268, 'cachedContents': {'largest': 'Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)', 'non_null': 10296, 'null': 0, 'top': [{'item': 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)', 'count': 20}, {'item': 'All Causes', 'count': 19}, {'item': "Alzheimer's disease (G30)", 'count': 18}, {'item': 'Malignant neoplasms (C00-C97)', 'count': 17}, {'item': 'Chronic lower respiratory diseases (J40-J47)', 'count': 16}, {'item': 'Diabetes mellitus (E10-E14)', 'count': 15}, {'item': 'Diseases of heart (I00-I09,I11,I13,I20-I51)', 'count': 14}, {'item': 'Influenza and pneumonia (J09-J18)', 'count': 13}, {'item': 'Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)', 'count': 12}, {'item': 'Cerebrovascular diseases (I60-I69)', 'count': 11}, {'item': 'Intentional self-harm (suicide) (*U03,X60-X84,Y87.0)', 'count': 10}], 'smallest': 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)'}, 'format': {'displayStyle': 'plain', 'align': 'left'}}, {'id': 317117535, 'name': 'Cause Name', 'dataTypeName': 'text', 'description': '', 'fieldName': 'cause_name', 'position': 3, 'renderTypeName': 'text', 'tableColumnId': 33023982, 'width': 220, 'cachedContents': {'largest': 'Unintentional injuries', 'non_null': 10296, 'null': 0, 'top': [{'item': 'Unintentional injuries', 'count': 20}, {'item': 'All causes', 'count': 19}, {'item': "Alzheimer's disease", 'count': 18}, {'item': 'Cancer', 'count': 17}, {'item': 'CLRD', 'count': 16}, {'item': 'Diabetes', 'count': 15}, {'item': 'Heart disease', 'count': 14}, {'item': 'Influenza and pneumonia', 'count': 13}, {'item': 'Kidney disease', 'count': 12}, {'item': 'Stroke', 'count': 11}, {'item': 'Suicide', 'count': 10}], 'smallest': 'All causes'}, 'format': {'displayStyle': 'plain', 'align': 'left'}}, {'id': 317117536, 'name': 'State', 'dataTypeName': 'text', 'description': '', 'fieldName': 'state', 'position': 4, 'renderTypeName': 'text', 'tableColumnId': 33023983, 'width': 160, 'cachedContents': {'largest': 'Wyoming', 'non_null': 10296, 'null': 0, 'top': [{'item': 'Illinois', 'count': 20}, {'item': 'Indiana', 'count': 19}, {'item': 'Iowa', 'count': 18}, {'item': 'Kansas', 'count': 17}, {'item': 'Kentucky', 'count': 16}, {'item': 'Louisiana', 'count': 15}, {'item': 'Maine', 'count': 14}, {'item': 'Maryland', 'count': 13}, {'item': 'Massachusetts', 'count': 12}, {'item': 'Michigan', 'count': 11}, {'item': 'Minnesota', 'count': 10}, {'item': 'Mississippi', 'count': 9}, {'item': 'Missouri', 'count': 8}, {'item': 'Montana', 'count': 7}, {'item': 'Nebraska', 'count': 6}, {'item': 'Nevada', 'count': 5}, {'item': 'New Hampshire', 'count': 4}, {'item': 'New Jersey', 'count': 3}, {'item': 'New Mexico', 'count': 2}, {'item': 'New York', 'count': 1}], 'smallest': 'Alabama'}, 'format': {'displayStyle': 'plain', 'align': 'left'}}, {'id': 317117537, 'name': 'Deaths', 'dataTypeName': 'number', 'description': '', 'fieldName': 'deaths', 'position': 5, 'renderTypeName': 'number', 'tableColumnId': 33023984, 'width': 172, 'cachedContents': {'largest': '2712630', 'non_null': 10296, 'average': '15326.67667055167', 'null': 0, 'top': [{'item': '299', 'count': 20}, {'item': '289', 'count': 19}, {'item': '272', 'count': 18}, {'item': '245', 'count': 17}, {'item': '258', 'count': 16}], 'smallest': '21', 'sum': '157803463'}, 'format': {'precisionStyle': 'standard', 'noCommas': 'false', 'align': 'right'}}, {'id': 317117538, 'name': 'Age-adjusted Death Rate', 'dataTypeName': 'number', 'description': '', 'fieldName': 'aadr', 'position': 6, 'renderTypeName': 'number', 'tableColumnId': 33023985, 'width': 148, 'cachedContents': {'largest': '1087.3', 'non_null': 10296, 'average': '128.0264277389277', 'null': 0, 'top': [{'item': '40.4', 'count': 20}, {'item': '35.2', 'count': 19}, {'item': '44.7', 'count': 18}, {'item': '42.8', 'count': 17}, {'item': '40.8', 'count': 16}], 'smallest': '2.6', 'sum': '1318160.1'}, 'format': {'precisionStyle': 'standard', 'noCommas': 'false', 'precision': '2', 'align': 'right'}}], 'grants': [{'inherited': False, 'type': 'viewer', 'flags': ['public']}], 'license': {'name': 'Public Domain'}, 'metadata': {'rdfSubject': '0', 'rdfClass': '', 'jsonQuery': {'order': [{'columnFieldName': 'aadr', 'ascending': True}]}, 'custom_fields': {'Common Core': {'Contact Email': 'nchsdata@cdc.gov', 'Contact Name': 'National Center for Health Statistics', 'Program Code': '009:020', 'Publisher': 'National Center for Health Statistics', 'Bureau Code': '009:00'}}, 'rowLabel': 'Row', 'availableDisplayTypes': ['table', 'fatrow', 'page'], 'renderTypeConfig': {'visible': {'table': True}}}, 'owner': {'id': 'ki96-txhe', 'displayName': 'NCHS', 'profileImageUrlLarge': '/api/users/ki96-txhe/profile_images/LARGE', 'profileImageUrlMedium': '/api/users/ki96-txhe/profile_images/THUMB', 'profileImageUrlSmall': '/api/users/ki96-txhe/profile_images/TINY', 'screenName': 'NCHS', 'type': 'interactive', 'flags': ['mayBeStoriesCoOwner']}, 'query': {'orderBys': [{'ascending': True, 'expression': {'columnId': 317117538, 'type': 'column'}}]}, 'rights': ['read'], 'tableAuthor': {'id': 'ki96-txhe', 'displayName': 'NCHS', 'profileImageUrlLarge': '/api/users/ki96-txhe/profile_images/LARGE', 'profileImageUrlMedium': '/api/users/ki96-txhe/profile_images/THUMB', 'profileImageUrlSmall': '/api/users/ki96-txhe/profile_images/TINY', 'screenName': 'NCHS', 'type': 'interactive', 'flags': ['mayBeStoriesCoOwner']}, 'tags': ['leading causes of death', 'mortality', 'state', 'united states', 'nchs'], 'flags': ['default', 'restorable', 'restorePossibleForType']}}
>>> type(d['meta'])
<class 'dict'>
>>> len(d['meta'].keys())
1
>>> len(d['meta']['view'].keys())
39
>>> import pprint
>>> pprint.pprint(d['meta']['view'])
{'attribution': 'National Center for Health Statistics',
 'averageRating': 0,
 'category': 'NCHS',
 'columns': [{'dataTypeName': 'meta_data',
              'fieldName': ':sid',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'sid',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'dataTypeName': 'meta_data',
              'fieldName': ':id',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'id',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'dataTypeName': 'meta_data',
              'fieldName': ':position',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'position',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'dataTypeName': 'meta_data',
              'fieldName': ':created_at',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'created_at',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'dataTypeName': 'meta_data',
              'fieldName': ':created_meta',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'created_meta',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'dataTypeName': 'meta_data',
              'fieldName': ':updated_at',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'updated_at',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'dataTypeName': 'meta_data',
              'fieldName': ':updated_meta',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'updated_meta',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'dataTypeName': 'meta_data',
              'fieldName': ':meta',
              'flags': ['hidden'],
              'format': {},
              'id': -1,
              'name': 'meta',
              'position': 0,
              'renderTypeName': 'meta_data'},
             {'cachedContents': {'average': '2007.5',
                                 'largest': '2016',
                                 'non_null': 10296,
                                 'null': 0,
                                 'smallest': '1999',
                                 'sum': '20669220',
                                 'top': [{'count': 20, 'item': '2016'},
                                         {'count': 19, 'item': '2015'},
                                         {'count': 18, 'item': '2014'},
                                         {'count': 17, 'item': '2013'},
                                         {'count': 16, 'item': '2012'},
                                         {'count': 15, 'item': '2011'},
                                         {'count': 14, 'item': '2010'},
                                         {'count': 13, 'item': '2009'},
                                         {'count': 12, 'item': '2008'},
                                         {'count': 11, 'item': '2007'},
                                         {'count': 10, 'item': '2006'},
                                         {'count': 9, 'item': '2005'},
                                         {'count': 8, 'item': '2004'},
                                         {'count': 7, 'item': '2003'},
                                         {'count': 6, 'item': '2002'},
                                         {'count': 5, 'item': '2001'},
                                         {'count': 4, 'item': '2000'},
                                         {'count': 3, 'item': '1999'}]},
              'dataTypeName': 'number',
              'description': '',
              'fieldName': 'year',
              'format': {'align': 'right',
                         'noCommas': 'true',
                         'precisionStyle': 'standard'},
              'id': 317117533,
              'name': 'Year',
              'position': 1,
              'renderTypeName': 'number',
              'tableColumnId': 33023980,
              'width': 148},
             {'cachedContents': {'largest': 'Nephritis, nephrotic syndrome and '
                                            'nephrosis '
                                            '(N00-N07,N17-N19,N25-N27)',
                                 'non_null': 10296,
                                 'null': 0,
                                 'smallest': 'Accidents (unintentional '
                                             'injuries) (V01-X59,Y85-Y86)',
                                 'top': [{'count': 20,
                                          'item': 'Accidents (unintentional '
                                                  'injuries) '
                                                  '(V01-X59,Y85-Y86)'},
                                         {'count': 19, 'item': 'All Causes'},
                                         {'count': 18,
                                          'item': "Alzheimer's disease (G30)"},
                                         {'count': 17,
                                          'item': 'Malignant neoplasms '
                                                  '(C00-C97)'},
                                         {'count': 16,
                                          'item': 'Chronic lower respiratory '
                                                  'diseases (J40-J47)'},
                                         {'count': 15,
                                          'item': 'Diabetes mellitus '
                                                  '(E10-E14)'},
                                         {'count': 14,
                                          'item': 'Diseases of heart '
                                                  '(I00-I09,I11,I13,I20-I51)'},
                                         {'count': 13,
                                          'item': 'Influenza and pneumonia '
                                                  '(J09-J18)'},
                                         {'count': 12,
                                          'item': 'Nephritis, nephrotic '
                                                  'syndrome and nephrosis '
                                                  '(N00-N07,N17-N19,N25-N27)'},
                                         {'count': 11,
                                          'item': 'Cerebrovascular diseases '
                                                  '(I60-I69)'},
                                         {'count': 10,
                                          'item': 'Intentional self-harm '
                                                  '(suicide) '
                                                  '(*U03,X60-X84,Y87.0)'}]},
              'dataTypeName': 'text',
              'description': '',
              'fieldName': '_113_cause_name',
              'format': {'align': 'left', 'displayStyle': 'plain'},
              'id': 317117534,
              'name': '113 Cause Name',
              'position': 2,
              'renderTypeName': 'text',
              'tableColumnId': 33023981,
              'width': 268},
             {'cachedContents': {'largest': 'Unintentional injuries',
                                 'non_null': 10296,
                                 'null': 0,
                                 'smallest': 'All causes',
                                 'top': [{'count': 20,
                                          'item': 'Unintentional injuries'},
                                         {'count': 19, 'item': 'All causes'},
                                         {'count': 18,
                                          'item': "Alzheimer's disease"},
                                         {'count': 17, 'item': 'Cancer'},
                                         {'count': 16, 'item': 'CLRD'},
                                         {'count': 15, 'item': 'Diabetes'},
                                         {'count': 14, 'item': 'Heart disease'},
                                         {'count': 13,
                                          'item': 'Influenza and pneumonia'},
                                         {'count': 12,
                                          'item': 'Kidney disease'},
                                         {'count': 11, 'item': 'Stroke'},
                                         {'count': 10, 'item': 'Suicide'}]},
              'dataTypeName': 'text',
              'description': '',
              'fieldName': 'cause_name',
              'format': {'align': 'left', 'displayStyle': 'plain'},
              'id': 317117535,
              'name': 'Cause Name',
              'position': 3,
              'renderTypeName': 'text',
              'tableColumnId': 33023982,
              'width': 220},
             {'cachedContents': {'largest': 'Wyoming',
                                 'non_null': 10296,
                                 'null': 0,
                                 'smallest': 'Alabama',
                                 'top': [{'count': 20, 'item': 'Illinois'},
                                         {'count': 19, 'item': 'Indiana'},
                                         {'count': 18, 'item': 'Iowa'},
                                         {'count': 17, 'item': 'Kansas'},
                                         {'count': 16, 'item': 'Kentucky'},
                                         {'count': 15, 'item': 'Louisiana'},
                                         {'count': 14, 'item': 'Maine'},
                                         {'count': 13, 'item': 'Maryland'},
                                         {'count': 12, 'item': 'Massachusetts'},
                                         {'count': 11, 'item': 'Michigan'},
                                         {'count': 10, 'item': 'Minnesota'},
                                         {'count': 9, 'item': 'Mississippi'},
                                         {'count': 8, 'item': 'Missouri'},
                                         {'count': 7, 'item': 'Montana'},
                                         {'count': 6, 'item': 'Nebraska'},
                                         {'count': 5, 'item': 'Nevada'},
                                         {'count': 4, 'item': 'New Hampshire'},
                                         {'count': 3, 'item': 'New Jersey'},
                                         {'count': 2, 'item': 'New Mexico'},
                                         {'count': 1, 'item': 'New York'}]},
              'dataTypeName': 'text',
              'description': '',
              'fieldName': 'state',
              'format': {'align': 'left', 'displayStyle': 'plain'},
              'id': 317117536,
              'name': 'State',
              'position': 4,
              'renderTypeName': 'text',
              'tableColumnId': 33023983,
              'width': 160},
             {'cachedContents': {'average': '15326.67667055167',
                                 'largest': '2712630',
                                 'non_null': 10296,
                                 'null': 0,
                                 'smallest': '21',
                                 'sum': '157803463',
                                 'top': [{'count': 20, 'item': '299'},
                                         {'count': 19, 'item': '289'},
                                         {'count': 18, 'item': '272'},
                                         {'count': 17, 'item': '245'},
                                         {'count': 16, 'item': '258'}]},
              'dataTypeName': 'number',
              'description': '',
              'fieldName': 'deaths',
              'format': {'align': 'right',
                         'noCommas': 'false',
                         'precisionStyle': 'standard'},
              'id': 317117537,
              'name': 'Deaths',
              'position': 5,
              'renderTypeName': 'number',
              'tableColumnId': 33023984,
              'width': 172},
             {'cachedContents': {'average': '128.0264277389277',
                                 'largest': '1087.3',
                                 'non_null': 10296,
                                 'null': 0,
                                 'smallest': '2.6',
                                 'sum': '1318160.1',
                                 'top': [{'count': 20, 'item': '40.4'},
                                         {'count': 19, 'item': '35.2'},
                                         {'count': 18, 'item': '44.7'},
                                         {'count': 17, 'item': '42.8'},
                                         {'count': 16, 'item': '40.8'}]},
              'dataTypeName': 'number',
              'description': '',
              'fieldName': 'aadr',
              'format': {'align': 'right',
                         'noCommas': 'false',
                         'precision': '2',
                         'precisionStyle': 'standard'},
              'id': 317117538,
              'name': 'Age-adjusted Death Rate',
              'position': 6,
              'renderTypeName': 'number',
              'tableColumnId': 33023985,
              'width': 148}],
 'createdAt': 1449080633,
 'description': 'This dataset presents the age-adjusted death rates for the 10 '
                'leading causes of death in the United States beginning in '
                '1999.\r\n'
                '\r\n'
                'Data are based on information from all resident death '
                'certificates filed in the 50 states and the District of '
                'Columbia using demographic and medical characteristics. '
                'Age-adjusted death rates (per 100,000 population) are based '
                'on the 2000 U.S. standard population. Populations used for '
                'computing death rates after 2010 are postcensal estimates '
                'based on the 2010 census, estimated as of July 1, 2010. Rates '
                'for census years are based on populations enumerated in the '
                'corresponding censuses. Rates for non-census years before '
                '2010 are revised using updated intercensal population '
                'estimates and may differ from rates previously published.\r\n'
                '\r\n'
                'Causes of death classified by the International '
                'Classification of Diseases, Tenth Revision (ICD–10) are '
                'ranked according to the number of deaths assigned to rankable '
                'causes. Cause of death statistics are based on the underlying '
                'cause of death.\r\n'
                '\r\n'
                'SOURCES\r\n'
                'CDC/NCHS, National Vital Statistics System, mortality data '
                '(see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see '
                'http://wonder.cdc.gov).\r\n'
                '\r\n'
                'REFERENCES\r\n'
                '\r\n'
                '1. National Center for Health Statistics. Vital statistics '
                'data available. Mortality multiple cause files. Hyattsville, '
                'MD: National Center for Health Statistics. Available from: '
                'https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\r\n'
                '\r\n'
                '2. Murphy SL, Xu JQ, Kochanek KD, Curtin SC, and Arias E. '
                'Deaths: Final data for 2015. National vital statistics '
                'reports; vol 66. no. 6. Hyattsville, MD: National Center for '
                'Health Statistics. 2017. Available from: '
                'https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_06.pdf.',
 'displayType': 'table',
 'downloadCount': 54853,
 'flags': ['default', 'restorable', 'restorePossibleForType'],
 'grants': [{'flags': ['public'], 'inherited': False, 'type': 'viewer'}],
 'hideFromCatalog': False,
 'hideFromDataJson': False,
 'id': 'bi63-dtpu',
 'indexUpdatedAt': 1534786118,
 'license': {'name': 'Public Domain'},
 'licenseId': 'PUBLIC_DOMAIN',
 'metadata': {'availableDisplayTypes': ['table', 'fatrow', 'page'],
              'custom_fields': {'Common Core': {'Bureau Code': '009:00',
                                                'Contact Email': 'nchsdata@cdc.gov',
                                                'Contact Name': 'National '
                                                                'Center for '
                                                                'Health '
                                                                'Statistics',
                                                'Program Code': '009:020',
                                                'Publisher': 'National Center '
                                                             'for Health '
                                                             'Statistics'}},
              'jsonQuery': {'order': [{'ascending': True,
                                       'columnFieldName': 'aadr'}]},
              'rdfClass': '',
              'rdfSubject': '0',
              'renderTypeConfig': {'visible': {'table': True}},
              'rowLabel': 'Row'},
 'name': 'NCHS - Leading Causes of Death: United States',
 'newBackend': False,
 'numberOfComments': 0,
 'oid': 26650094,
 'owner': {'displayName': 'NCHS',
           'flags': ['mayBeStoriesCoOwner'],
           'id': 'ki96-txhe',
           'profileImageUrlLarge': '/api/users/ki96-txhe/profile_images/LARGE',
           'profileImageUrlMedium': '/api/users/ki96-txhe/profile_images/THUMB',
           'profileImageUrlSmall': '/api/users/ki96-txhe/profile_images/TINY',
           'screenName': 'NCHS',
           'type': 'interactive'},
 'provenance': 'official',
 'publicationAppendEnabled': False,
 'publicationDate': 1503517561,
 'publicationGroup': 5829091,
 'publicationStage': 'published',
 'query': {'orderBys': [{'ascending': True,
                         'expression': {'columnId': 317117538,
                                        'type': 'column'}}]},
 'rights': ['read'],
 'rowClass': '',
 'rowsUpdatedAt': 1534786071,
 'rowsUpdatedBy': 's6ey-4vqh',
 'tableAuthor': {'displayName': 'NCHS',
                 'flags': ['mayBeStoriesCoOwner'],
                 'id': 'ki96-txhe',
                 'profileImageUrlLarge': '/api/users/ki96-txhe/profile_images/LARGE',
                 'profileImageUrlMedium': '/api/users/ki96-txhe/profile_images/THUMB',
                 'profileImageUrlSmall': '/api/users/ki96-txhe/profile_images/TINY',
                 'screenName': 'NCHS',
                 'type': 'interactive'},
 'tableId': 14417583,
 'tags': ['leading causes of death',
          'mortality',
          'state',
          'united states',
          'nchs'],
 'totalTimesRated': 0,
 'viewCount': 23371,
 'viewLastModified': 1534786063,
 'viewType': 'tabular'}
>>> 

>>> type(d['data'])
<class 'list'>
>>> len(type(d['data']))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'type' has no len()
>>> len(d['data'])
10296
>>> type(d['data'][0])
<class 'list'>
>>> len(d['data'][0]))
  File "<stdin>", line 1
    len(d['data'][0]))
                     ^
SyntaxError: invalid syntax
>>> len(d['data'][0])
14
>>> pprint.pprint(d['data'][0])
[15029,
 '0E3080FB-5EF8-4BEF-834E-54B52DB8DFF3',
 15029,
 1534786069,
 '1099577',
 1534786069,
 '1099577',
 None,
 '2016',
 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)',
 'Unintentional injuries',
 'Alabama',
 '2755',
 '55.5']
>>> pprint.pprint(d['data'][1])
[15030,
 '5A6F1799-07FB-4C97-B6FC-A8BB792C5137',
 15030,
 1534786069,
 '1099577',
 1534786069,
 '1099577',
 None,
 '2016',
 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)',
 'Unintentional injuries',
 'Alaska',
 '439',
 '63.1']
>>> pprint.pprint(d['data'][2])
[15031,
 '50D8F132-BD59-4267-A3F9-7179EF5C2628',
 15031,
 1534786069,
 '1099577',
 1534786069,
 '1099577',
 None,
 '2016',
 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)',
 'Unintentional injuries',
 'Arizona',
 '4010',
 '54.2']
>>> 
```

