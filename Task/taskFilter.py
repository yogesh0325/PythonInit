
import datetime
import dtlpy as dl
from login import Init
plan = Init(projectId="9d292e3e-a3f8-43dc-ae3b-8f888b253dac",
            datasetId="63ea0db4d1dbe6ed18f63663", itemId="63ea30343a09ce79bd78bd09")

# Create a task with all items in a specific folder
filters = dl.Filters(field='/home/yogesh/Desktop/aa/',
                     values='/home/yogesh/Desktop/aa/')
# filter items without annotations
filters = dl.Filters(field='birds', values=False)
# Create annotation task with filters
task = plan.dataset.tasks.create(
    task_name='task_check',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    # The items will be divided equally between assignments
    filters=filters  # filter by folder directory or use other filters
)
# Create QA task with filters
qa_task = plan.dataset.tasks.create_qa_task(task=task,
                                            due_date=datetime.datetime(
                                                day=1, month=1, year=2029).timestamp(),
                                            assignee_ids=[
                                                'annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
                                            filters=filters  # this filter is for "completed items"
                                            )
