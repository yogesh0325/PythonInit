import dtlpy as dl
if dl.token_expired():
    dl.login()

projectId = "5b9a9de4-00e7-41b4-a74a-746ee0a6769c"
datasetId = "694a7e1a5dbba29577f2f58c" #"69293a02b405649bfacadecf"
itemId = "694e2a3eec87e5a125c4e930" #"69425724580424d34071044e"
project = dl.projects.get(project_id=projectId)
dataset = project.datasets.get(dataset_id=datasetId)
item = dataset.items.get(item_id=itemId)

drivers = project.packages.list()
for driver in drivers:
    print(driver.name)
print(drivers)
service = project.services.get(service_name="custom-webm-converter-service")
print(service)
execution = service.execute(
    function_name="run", 
    item_id=item.id,
    project_id=project.id
)
# execution = execution.wait()
print(execution)
# print("--------------------------------")
# if execution.latest_status["status"] == "success":
#     result = execution.output
#     print(f"Service executed successfully: {result}")
# else:
#     print(f"Execution failed: {execution.latest_status['message']}")
# item.metadata['system']['errors'] = []
# item.update(system_metadata=True)
