import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='images-one')
dataset = project.datasets.get(dataset_name='My-First-Dataset')
item_1 = dataset.items.get(item_id="63ea30343a09ce79bd78bd09")

builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Point(x=80, y=80, label='Ear'))
builder.add(annotation_definition=dl.Point(x=120, y=120, label='Ear'))
item_1.annotations.upload(builder)
