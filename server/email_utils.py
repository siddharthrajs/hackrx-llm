# email_utils.py
import extract_msg

def extract_text_from_email(msg_path):
    msg = extract_msg.Message(msg_path)
    return msg.body
