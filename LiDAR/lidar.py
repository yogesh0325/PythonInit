import dtlpy as dl
from login import Init
plan = Init("01a10497-0af6-4eca-b0d2-240304080d4c",
            "63985d5b41f1b6c0ca28e435", "639865643c3d9b199cd3ce53")

# item = dl.items.get(item_id="639865643c3d9b199cd3ce53")

builder = plan.item.annotations.builder()

builder.add(annotation_definition=dl.Cube3d(label='bike', scale=[
            5, 1, 5], rotation=[0, 0, 0], position=[0, 0, 0]))
plan.item.annotations.upload(builder)

plan.item.print()
