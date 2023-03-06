import dtlpy as dl
from random import random
project = dl.projects.get(project_id="9d292e3e-a3f8-43dc-ae3b-8f888b253dac")
dataset = project.datasets.get(dataset_name='My-First-Dataset')
recipe = dataset.recipes.list()[0]

dataset.add_label(label_name='Box')

pipeline = project.pipelines.create(
    name="pipeline_"+str(random()), project_id=project.id)

dataset_node = dl.DatasetNode(
    name=dataset.name,
    project_id=project.id,
    dataset_id=dataset.id,
    position=(0, 0)
)

task_name_1 = 'My Task'
task_node_1 = dl.TaskNode(
    name=task_name_1,
    recipe_id=recipe.id,
    recipe_title=recipe.title,
    task_owner="yogesh.b@dataloop.ai",
    workload=[dl.WorkloadUnit(assignee_id="shadi.m@dataloop.ai", load=50), dl.WorkloadUnit(assignee_id="yogesh.b@dataloop.ai", load=50)],
    position=(1, 1),
    project_id=project.id,
    dataset_id=dataset.id,
)


def run(item: dl.Item, width=0, height=0):
    if width != 0 and height != 0:
        item.width = width
        item.height = height
        item.update()

    item.set_description("Updated by pipeline")

    return item


code_node = dl.CodeNode(
    name='My Function',
    position=(2, 2),
    project_id=project.id,
    method=run,
    project_name=project.name
)

# function_node = dl.FunctionNode(
#     name='run',
#     position=(3, 3),
#     service=dl.services.get(service_id="service_id"),
#     function_name='move_item'
# )

pipeline.nodes.add(dataset_node).connect(node=task_node_1) \
    .connect(node=code_node, source_port=task_node_1.outputs[0]) 
    # \
    # .connect(node=function_node)

task_node_1.add_trigger()

pipeline.update()
pipeline = project.pipelines.get(pipeline_name=pipeline.name)
pipeline.install()
print("Pipeline ready")
