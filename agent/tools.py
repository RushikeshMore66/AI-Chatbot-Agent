from integrations.email import send_email

def execute_tools(step):
    action = step.get("action")
    data = step.get("data", {})

    if action == "send_email":
        result = send_email(
            to=data.get("to"),
            subject=data.get("subject"),
            body=data.get("body")
        )
        
    elif action == "update_crm":
        return "CRM updated successfully"
        
    elif action == "notify":
        return "Notification sent successfully"
        
    elif action == "reply":
        return data.get("message","Done")
    return "Unknown action"