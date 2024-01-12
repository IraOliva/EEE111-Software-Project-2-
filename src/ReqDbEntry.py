class ReqDbEntry:
    def __init__(self,
                 id=1,
                 description='Quiz',
                 subject='Math 21',
                 priority='High',
                 status='Pending'):
        self.id = id
        self.description = description
        self.subject = subject
        self.priority = priority
        self.status = status
