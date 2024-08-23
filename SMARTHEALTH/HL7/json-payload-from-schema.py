################################################################################
#  Licensed to the FIWARE Foundation (FF) under one
#  or more contributor license agreements. The FF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  Author: alain.galdemas@mail.com
################################################################################

# This program will create json payload example files for each type of entity for HL7/FHIR mapping in NGSI-LD
# It take the json schema from the directory, validate it, 
# Use the pysmartdatamodels library to produce a json sample payload, create the directory to put examples

# contact alain.galdemas@mail.com

import json
import os
import copy
import pathlib
import sys
import jsonschema
#from jsonschema import validate, RefResolver, Draft202012Validator
import requests
import jsonref
# from pysmartdatamodels import *
import pysmartdatamodels as sdm


###############################################################################
# global variables
global_schema_file = "overall_schema_4.3.json"  #'fhir.schema.5.0.json' # # HL7/FHIR origin schema file name
definition_file = (
    "common-hl7-schema.json"  # common base definitions for HL7/FHIR mapping
)
schema_url = "https://json-schema.org/draft-07/schema#"

# define the base url for "$id" don't forget a "/" at the end !
base_schema_url = (
    "https://raw.githubusercontent.com/agaldemas/incubated/master/SMARTHEALTH/HL7/"
)
# path to FHIR release for a specific directory
fhir_release_path='FHIR-R4/'
# 
###############################################################################
# Functions
        
# for the moment the schema must be published on the web (github), 
# to be processed through the pysmartdatamodels library
# but to prepare the url to load the schema we'll use the current directories from the repo
entity_type = 'Patient'
results = {}

# try:
# base_schema = 'https://raw.githubusercontent.com/agaldemas/incubated/master/SMARTHEALTH/HL7/FHIR-R4/common-hl7-schema.json'
# print('validate base schema: ' + base_schema)
# results = sdm.validate_data_model_schema(base_schema)
# print(results)
print('=================================================')

schema_url = base_schema_url + fhir_release_path + entity_type + '/schema.json'
# schema_url = 'https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/eb97b0d8cc77d3258ea4a96da5dfe6e5597f229a/RoadSegment/schema.json'
# schema_url = 'https://raw.githubusercontent.com/smart-data-models/incubated/blob/master/SMARTCITIES/SMARTPORTS/NEW_PORT/MarineTransport-schema.json'
schema_url = 'https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/MosquitoDensity/schema.json'

print('>>>>>>>>> schemaUrl: ', schema_url)
results = sdm.validate_data_model_schema(schema_url)
print(results)
# print('=================================================')
# example = sdm.ngsi_ld_example_generator(schema_url)
# print('example of json:')
# print(example)

#except Exception as e:
#    print("An error occurred while validating the data model schema:", e)
    # sys.exit(1)
