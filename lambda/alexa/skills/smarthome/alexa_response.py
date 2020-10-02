# -*- coding: utf-8 -*-

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: LicenseRef-.amazon.com.-AmznSL-1.0
# Licensed under the Amazon Software License  http://aws.amazon.com/asl/

import datetime
import math
import random
import uuid
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class AlexaResponse:
    """Helper class to generate an AlexaResponse"""

    def __init__(self, opts={}):
        
        self.context_properties = []
        self.payload_endpoints = []
        self.context = {}
        self.event = opts.get('event', None)
        
        if self.event == None:
            self.event = {
                'header': {
                    'namespace': opts.get('namespace', 'Alexa'),
                    'name': opts.get('name', 'Response'),
                    'messageId': opts.get('messageId', str(uuid.uuid4())),
                    'payloadVersion': opts.get('payloadVersion', '3')
                },
                'endpoint': {
                    'scope': {
                        'type': 'BearerToken',
                        'token': opts.get('token', 'INVALID'),
                    },
                    'endpointId': opts.get('endpointId', 'INVALID')
                },
                'payload': opts.get('payload', {})
            }

        if 'correlation_token' in opts:
            self.event['header']['correlation_token'] = opts.get('correlation_token', 'INVALID')

        if 'cookie' in opts:
            self.event['endpoint']['cookie'] = opts.get('cookie', '{}')

        # No endpoint in an AcceptGrant or Discover request
        if self.event['header']['name'] == 'AcceptGrant.Response' or self.event['header']['name'] == 'Discover.Response':
            del self.event['endpoint']

    def add_context_property(self, opts):
        """Add a property to the context.
        
        @param opts Contains options for the property.
        """
        self.context_properties.append(self.create_context_property(opts))

    def add_payload_endpoint(self, opts):
        """Add an endpoint to the payload.
        
        @param opts Contains options for the endpoint.
        """
        self.payload_endpoints.append(self.create_payload_endpoint(opts))

    def create_context_property(self, opts):
        """Creates a property for the context.

        @param opts Contains options for the property.
        """
        now = datetime.datetime.now()
        iso_time = now.strftime('%Y-%m-%dT%H:%M:%SZ') 

        context_property = {
            'namespace': opts.get('namespace', 'Alexa.EndpointHealth'),
            'name': opts.get('name', 'connectivity'),
            'value': opts.get('value',{'value':'OK'}),
            'timeOfSample': iso_time,
            'uncertaintyInMilliseconds': opts.get('uncertaintyInMilliseconds', 0)
        }
        
        if 'instance' in opts:
            context_property['instance'] = opts.get('instance', 'UNDEFINED')

        return context_property

    def create_payload_endpoint(self, opts={}):
        """Creates an endpoint for the payload.

        @param opts Contains options for the endpoint.
        """
        endpoint = {
            'capabilities': opts.get('capabilities', []),
            'description': opts.get('description', 'Sample Endpoint Description'),
            'displayCategories': opts.get('displayCategories', ['OTHER']),
            'endpointId': opts.get('endpointId', 'endpoint_' + str(math.floor(random.random() * 90000 + 10000))),
            'friendlyName': opts.get('friendlyName', 'Sample Endpoint'),
            'manufacturerName': opts.get('manufacturerName', 'Sample Manufacturer')
        }
        
        if 'cookie' in opts:
            endpoint['cookie'] = opts.get('cookie', {})

        return endpoint

    def get(self, remove_empty=True):

        response = {
            'context': self.context,
            'event': self.event
        }

        if len(self.context_properties) > 0:
            response['context']['properties'] = self.context_properties

        if len(self.payload_endpoints) > 0:
            response['event']['payload']['endpoints'] = self.payload_endpoints

        if remove_empty:
            if len(response['context']) < 1:
                response.pop('context')

        return response