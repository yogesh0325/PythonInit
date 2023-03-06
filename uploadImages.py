import dtlpy as dl
from login import Init
plan = Init(projectId="9d292e3e-a3f8-43dc-ae3b-8f888b253dac",
            datasetId="63eb2dfecd34d22a26c4f054", itemId="63ec62a827392968db4b56a2")


plan.dataset.items.upload(local_path='/home/yogesh/Desktop/rbg.jpeg')
# plan.dataset.add_label(label_name='birds')
# Create a builder instance
builder = plan.item.annotations.builder()
# Create box annotation with label
# builder.add(annotation_definition=dl.Box(top=10,left=10,bottom=100,right=100,label='birds'))
# Upload box to the item
plan.item.annotations.upload(builder)
