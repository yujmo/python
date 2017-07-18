# -*- coding: utf-8 -*-

import time
import uuid
import json
from urllib.parse import urlencode, quote
from urllib.request import urlopen
from hashlib import sha1
import hmac
import base64

def sign(access_secret, **params):
    sorted_params = sorted(params.items(), key=lambda x: x[0])

    encoded_query_string = ''
    for (key, value) in sorted_params:
        encoded_query_string += '&' + x_encode(key) + '=' + x_encode(value)

    string_to_sign = 'GET&%2F&' + x_encode(encoded_query_string[1:])
    bytes_to_sign = bytes(string_to_sign, encoding='utf-8')

    bytes_access_secret = bytes(access_secret + '&', encoding='utf-8')
    h = hmac.new(bytes_access_secret, bytes_to_sign, sha1)
    bytes_signature = base64.encodebytes(h.digest()).strip()

    return bytes_signature.decode('utf-8')


def x_encode(data):
    data = str(data)
    data = quote(data.encode('utf8'), '')
    data = data.replace('+', '%20')
    data = data.replace('*', '%2A')
    data = data.replace('%7E', '~')
    return data


def get_public_ip():
    res = urlopen('http://members.3322.org/dyndns/getip').read()
    return res.strip().decode('utf-8')

class AliyunDNSApi:
    __api_url = 'http://alidns.aliyuncs.com/?'
    __api_domain = 'alidns.aliyuncs.com'
    __api_port = '80'

    def __init__(self, access_key, access_key_secret, record_id):
        self.__access_key = access_key
        self.__access_key_secret = access_key_secret
        self.__record_id = record_id

    def __common_params(self):
        return {
            "AccessKeyId": self.__access_key,

            "Timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            "SignatureNonce": str(uuid.uuid1()),
            "Format": 'JSON',
            "Version": '2015-01-09',
            "SignatureMethod": "HMAC-SHA1",
            "SignatureVersion": "1.0"
        }

    def update_record(self, **kwargs):
        parameters = {
            "Action": 'UpdateDomainRecord',
            "RecordId": kwargs["RecordId"],
            "RR": kwargs["RR"],
            "Value": kwargs["Value"],
            "Type": kwargs["Type"],
            "TTL": kwargs["TTL"],
            "Le.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtimine": kwargs["Line"],
        }
        parameters = dict(parameters, **self.__common_params())

        signature = sign(self.__access_key_secret, **parameters)
        parameters['Signature'] = signature

        url = self.__api_url + urlencode(parameters)
        response = urlopen(url).read()
        print(response.decode('utf-8'))

    def get_record(self):
        parameters = {
            "Action": 'DescribeDomainRecords',
            "DomainName": 'mooyu.site'
        }
        parameters = dict(parameters, **self.__common_params())

        signature = sign(self.__access_key_secret, **parameters)
        parameters['Signature'] = signature

        url = self.__api_url + urlencode(parameters)
        response = urlopen(url).read()
        print(response.decode('utf-8'))


    def query_record(self):
        parameters = {
            "Action": 'DescribeDomainRecordInfo',
            "RecordId": self.__record_id
        }
        parameters = dict(parameters, **self.__common_params())

        signature = sign(self.__access_key_secret, **parameters)
        parameters['Signature'] = signature

        url = self.__api_url + urlencode(parameters)
        response = urlopen(url).read()
        return json.loads(response.decode('utf-8'))


if __name__ == '__main__':
	api = AliyunDNSApi('xxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '000000000000')
#    result = api.query_record()
    print(api.get_record())
#    print(result)
    # 获取本机公网ip地址
    current_ip = get_public_ip()
    # 比较,如果不同,则更新解析记录
#    if current_ip != result['Value']:
#        result['Value'] = current_ip
#        api.update_record(**result)
#        # 输出更新后的解析记录
#        result = api.query_record()
#        print(result)

    exit()
