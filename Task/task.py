
import datetime
import dtlpy as dl
from login import Init
plan = Init(projectId="9d292e3e-a3f8-43dc-ae3b-8f888b253dac",
            datasetId="63ea0db4d1dbe6ed18f63663", itemId="63ea30343a09ce79bd78bd09")

items = plan.dataset.items.list()
items_list = [item for item in items.all()]
task = plan.dataset.tasks.create(
    task_name='firstTask',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['yogesh.b@dataloop.ai', 'annotator2@dataloop.ai'],
    # The items will be divided equally between assignments
    items=items_list
)
