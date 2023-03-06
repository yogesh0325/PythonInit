import dtlpy as dl
from login import Init
plan = Init(projectId="9d292e3e-a3f8-43dc-ae3b-8f888b253dac",
            datasetId="63ea0db4d1dbe6ed18f63663", itemId="63ea30343a09ce79bd78bd09")
builder = plan.item.annotations.builder()
builder.add(annotation_definition=dl.Box(top=200,
                                         left=625,
                                         bottom=290,
                                         right=699,
                                         label='Person'))
plan.item.annotations.upload(builder)
