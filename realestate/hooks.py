# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "realestate"
app_title = "Erpnext Real Estate Crm"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Real Estate Crm for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/realestate/css/realestate.bundle.css"
app_include_js = "/assets/realestate/js/realestate.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "realestate.engine.on_document_submit",
        "on_cancel": "realestate.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "realestate.engine.daily_scheduled_sync"
    ]
}
