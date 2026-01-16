import dtlpy as dl
if dl.token_expired():
    dl.login()

projectId = "5b9a9de4-00e7-41b4-a74a-746ee0a6769c"
datasetId = "69293a02b405649bfacadecf"
itemId = "69293a5a64a397fa69d285f4"
project = dl.projects.get(project_id=projectId)
dataset = project.datasets.get(dataset_id=datasetId)
item = dataset.items.get(item_id=itemId)

system = item.metadata['system']
if 'modalities' not in system:
    print("modalities not found")
    service = project.services.get(service_name="custom-webm-converter-service")
    execution = service.execute(
        function_name="run", 
        item_id=item.id,
        project_id=project.id
    )
    execution = execution.wait()
    print("--------------------------------")
    if execution.latest_status["status"] == "success":
        result = execution.output
        print(f"Service executed successfully: {result}")
    else:
        print(f"Execution failed: {execution.latest_status['message']}")
else:
    print("modalities found")

item.metadata['system']['errors'] = []
item.update(system_metadata=True)
