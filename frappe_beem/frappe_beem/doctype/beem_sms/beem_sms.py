# Copyright (c) 2022, Africlouds Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json
import requests


class BeemSMS(Document):
    def send(self):
        if self.response:
            frappe.throw('Already Sent. Please use the resend function')
        settings = frappe.get_single("Beem Settings")
        session = requests.Session()
        session.auth = (settings.api_key, settings.api_secret)
        response = session.post(settings.sms_api_base_url+"/v1/send", data={
            "source_addr": self.source_addr,
            "encoding": "0",
            "message": self.message,
            "recipients": [
                {
                                "recipient_id": 1,
                                "dest_addr": "250788306159"
                                }

            ]
        })

        self.response = json.dumps(response.json())
        self.response_code = response.json()['code']
        self.response_message = response.json()['message']
        self.save()

    def resend(self):
        sms = self
        sms.response = None
        sms.response_code = None
        sms.response_message = None
        sms = sms.insert()
        sms.send()


@frappe.whitelist()
def send(sms):
    sms = frappe.get_doc('Beem SMS', sms)
    sms.send()


@frappe.whitelist()
def resend(sms):
    sms = frappe.get_doc('Beem SMS', sms)
    sms.resend()
