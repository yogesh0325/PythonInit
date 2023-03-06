import dtlpy as dl
from login import Init
plan = Init(projectId="9d292e3e-a3f8-43dc-ae3b-8f888b253dac",
            datasetId="63eb2dfecd34d22a26c4f054", itemId="63ec765468efcb8680cd7ac2")

for annotation in plan.item.annotations.list():
    print(annotation.object_id)
    for key in annotation.frames:
        frame = annotation.frames[key]
        print(frame.left, frame.right, frame.top, frame.bottom,key)
