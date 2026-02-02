import dtlpy as dl
import json
import io

if dl.token_expired():
    dl.login()
project = dl.projects.get(project_id='5b9a9de4-00e7-41b4-a74a-746ee0a6769c')

# Get the dataset
dataset = project.datasets.get(dataset_id='69240056616069eaed3b8757')

# Create a io.BytesIO object from the data json
data = {
  "prompt": "# Sample Markdown\n\nThis is sample markdown content.",
  "slider_1756714160576": 52,
  "response1": "Sample text",
  "response2": "Sample text",
  "response3": "Sample text",
  "rating1": 3,
  "rating2": 3,
  "rating3": 3,
  "confident": "true",
  "confidence": 1,
  "more": "Sample text"
}
buffer = io.BytesIO(json.dumps(data).encode('utf-8'))
buffer.name = '6825ef871ea4a49ab3890793-data-yogesoh1.json'
buffer.seek(0)
item = dataset.items.upload(
    local_path=buffer,
    item_metadata={
        'system': {
            'shebang': {
                'dltype': 'evaluation-studio'
            },
            'modalities': {
                'type': 'preview',
            },
            'evaluation': {
                'layoutName': '6825ef871ea4a49ab3890793'
            }
        }
    }
)

print("Item uploaded successfully:", item.id)
print("Open in platform:", item.platform_url)
