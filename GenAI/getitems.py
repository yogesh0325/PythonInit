import dtlpy as dl
if dl.token_expired():
    dl.login()
projectId = 'f1bd5cf4-5ff6-47f6-9ed0-c58f349f20aa'
modalityType = 'preview'
project = dl.projects.get(project_id=projectId)
datasets = project.datasets.list()
for dataset in datasets:
    print("Name of the dataset is ",dataset.name)
    items = dataset.items.list()
    for item in items.all():
        system = item.metadata.get('system', {})
        modalities = system.get('modalities')
        if modalities:
            for modality in modalities:
                typ = modality.get('type')
                if typ == modalityType:
                    print(item.name, " and the type is ", typ)