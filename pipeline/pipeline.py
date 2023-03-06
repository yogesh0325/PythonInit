import dtlpy as dl
from login import Init
plan = Init("9d292e3e-a3f8-43dc-ae3b-8f888b253dac", "63ea0db4d1dbe6ed18f63663","63ea30343a09ce79bd78bd09")

# is_deleted = plan.project.pipelines.delete(pipeline_name='My-First-Pipeline')
# pipeline = plan.project.pipelines.create(name='My-First-Pipeline')

pipelines = plan.project.pipelines.list()
for pipeline in pipelines:
    for item in pipeline:
        print(item)



plan.project.pipelines.open_in_web(pipeline_name='My-First-Pipeline')


# pipeline = plan.project.pipelines.get(pipeline_name='My-First-Pipeline')
# this is not working
# pipeline_execution= plan.project.pipelines.execute(pipeline='pipeline_entity', execution_input= {'item': 'item_id'} )

# print(plan.item)