import dtlpy as dl
from login import Init
plan = Init(projectId="ddc76cb7-5f05-4670-bf7a-350468c68a8f",
            datasetId="63edc4efd6116c109cd20188", itemId="63fc4da38a0d76fbe161609f")

filters = dl.Filters()
# filters.add(field='filename', values='/1.jpg')
pages = plan.dataset.items.list(filters=filters)
print('Number of items in dataset: {}'.format(pages.items_count))
# for page in pages:
#     for item in page:
#         item.print()

annos = plan.item.annotations.get("63fc4e3e1b9bc8b573733f29")
print(annos)


