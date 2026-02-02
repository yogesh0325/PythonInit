import dtlpy as dl

if dl.token_expired():
    dl.login()
project = dl.projects.get(project_id="f1bd5cf4-5ff6-47f6-9ed0-c58f349f20aa")
datasets = project.datasets.list()
for dataset in datasets:
    print("Name of the dataset is ",dataset.name)
    items = dataset.items.list()
    for item in items.all():
        system = item.metadata.get("system", {})
        shebang = system.get("shebang")
        if shebang:
            dltype = shebang.get("dltype")
            if dltype == "prompt":
                print(item.name, " and the type is ", dltype)
