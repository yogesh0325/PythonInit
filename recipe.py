import dtlpy as dl
from login import Init
plan = Init("9d292e3e-a3f8-43dc-ae3b-8f888b253dac", "63ea0db4d1dbe6ed18f63663","63ea30343a09ce79bd78bd09")
plan.dataset.add_label(label_name='ram', color=(34, 6, 231), attributes=['big', 'small'])
# plan.dataset.upload_annotations()