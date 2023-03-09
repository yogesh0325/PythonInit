from login import Init
plan = Init(projectId="01a10497-0af6-4eca-b0d2-240304080d4c",
            datasetId="63ec7bbe4c420d738c7d1df4", itemId="64060c34400b63222630e1f9")

plan.item.download(local_path="./")