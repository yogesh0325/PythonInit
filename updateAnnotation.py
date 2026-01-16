import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_id='7e943bad-51e3-4320-8258-169215e92af4')
dataset = project.datasets.get(dataset_id='6853dbb56da8de0e75995f15')
item = dataset.items.get(item_id='68752f422b9a3d711e4115af')
child_annotation = item.annotations.get(annotation_id='68ac25f7f6fbca749152a040')
child_annotation.parent_id = None
child_annotation.update(system_metadata=True)
print("Parent-child relation removed.")