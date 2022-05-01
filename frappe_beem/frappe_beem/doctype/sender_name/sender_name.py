# Copyright (c) 2022, Africlouds Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests


class SenderName(Document):

    def db_insert(self):
        pass

    def load_from_db(self):
        pass

    def db_update(self):
        pass

    def get_list(self, args):
        settings = frappe.get_single("Beem Settings")

        session = requests.Session()
        session.auth = (settings.api_key, settings.api_secret)

        sender_names = session.get(
            settings.sms_api_base_url+"/public/v1/sender-names").json()['data']
        for idx, sender_name in enumerate(sender_names):
            sender_name = sender_names[idx]
            sender_name['name'] = sender_name['id']
            sender_names[idx] = sender_name
        print(sender_names)
        return sender_names

    def get_count(self, args):
        pass

    def get_stats(self, args):
        pass
