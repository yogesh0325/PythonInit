import dtlpy as dl
if dl.token_expired():
    dl.login()
# Get the project
project = dl.projects.get(project_name='images-one')
project.print()
# Get the dataset
dataset = project.datasets.get(dataset_name='My-First-Dataset')

dataset.add_label(label_name='pcd')

item_1 = dataset.items.get(item_id='63ea30343a09ce79bd78bd09')

builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='pcd'))
item_1.annotations.upload(builder)
