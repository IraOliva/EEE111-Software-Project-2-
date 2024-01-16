import json
from ReqDbEntry import ReqDbEntry

class ReqDb:

    def __init__(self, dbName='ReqDb.csv'):   
        self.dbName = dbName
        print('TODO: __init__')
        self.requirementsList = []

    def fetch_requirements(self):
        print('TODO: fetch_requirements')
        tupleList = []
        for requirement in self.requirementsList:
            requirementData = (requirement.id, requirement.description, requirement.subject, requirement.priority, requirement.status)
            tupleList.append(requirementData)
        return tupleList

    def insert_requirement(self, id, description, subject, priority, status):
        newEntry = ReqDbEntry(id=id, description=description, subject=subject, priority=priority, status=status)
        print('TODO: insert_requirement')
        self.requirementsList.append(newEntry)

    def delete_requirement(self, id):
        print('TODO: delete_requirement')
        for requirement in self.requirementsList:
            if requirement.id == id:
                self.requirementsList.remove(requirement)
                break

    def update_requirement(self, new_description, new_subject, new_priority, new_status, id):
        print('TODO: update_requirement')
        for requirement in self.requirementsList:
            if requirement.id == id:
                requirement.description = new_description
                requirement.subject = new_subject
                requirement.priority = new_priority
                requirement.status = new_status
                break

    def export_csv(self):
        print('TODO: export_csv')
        with open(self.dbName, 'w') as file:
            for requirement in self.requirementsList:
                requirementData = str(requirement.id) + ',' + requirement.description + ',' + requirement.subject + ',' + requirement.priority + ',' + requirement.status + '\n'
                file.write(requirementData)

    def id_exists(self, id):
        for requirement in self.requirementsList:
            if requirement.id == id:
                return True
        return False
    
    def import_csv(self, file):
        print('TODO: import_csv')
        file = open(file, 'r')
        lines = file.readlines()  
        file.close()
        for line in lines:
            data = line.strip().split(',')
            entry = ReqDbEntry(data[0], data[1], data[2], data[3], data[4])
            self.requirementsList.append(entry)
    
    def export_json(self):
        print('TODO: export_json')
        requirementData = []
        for requirement in self.requirementsList:
            requirementDict = {
                'id': requirement.id,
                'description': requirement.description,
                'subject': requirement.subject,
                'priority': requirement.priority,
                'status': requirement.status
            }
            requirementData.append(requirementDict)

        with open('ReqDB.json', 'w') as json_file:
            json.dump(requirementData, json_file, indent=4)

