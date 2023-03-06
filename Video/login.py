import dtlpy as dl
if dl.token_expired():
    dl.login()

class Init:
    def __init__(self, projectId, datasetId, itemId):
        self.project = dl.projects.get(project_id=projectId)
        self.dataset = self.project.datasets.get(dataset_id=datasetId)
        self.item = self.dataset.items.get(item_id=itemId)
