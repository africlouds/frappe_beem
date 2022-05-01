// Copyright (c) 2022, Africlouds Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Beem SMS', {
	 refresh: function(frm) {
		if(!frm.doc.response)
		frm.add_custom_button(__("Send"), function () {
			frappe.call({
				method: "frappe_beem.frappe_beem.doctype.beem_sms.beem_sms.send",
				args:{
					sms: frm.doc.name
				},
				callback: function(r) {
					frm.reload_doc()						
					frappe.msgprint("Sent");
				}
			})
		});
		if(frm.doc.response)
		frm.add_custom_button(__("Resend"), function () {
			frappe.call({
				method: "frappe_beem.frappe_beem.doctype.beem_sms.beem_sms.resend",
				args:{
					sms: frm.doc.name
				},
				callback: function(r) {
					frm.reload_doc()						
					frappe.msgprint("Resent");
				}
			})
		});
	 }
});
