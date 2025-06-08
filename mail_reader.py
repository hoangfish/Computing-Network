class MailReader:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def get_latest_command_mail(self):
        # Trả về chuỗi giả lập nội dung mail
        return "Đây là nội dung mail mới nhất giả lập để test giao diện."
