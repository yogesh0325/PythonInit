import dtlpy as dl
from login import Init
plan = Init(projectId="9d292e3e-a3f8-43dc-ae3b-8f888b253dac",
            datasetId="63eb2dfecd34d22a26c4f054", itemId="63ec765468efcb8680cd7ac2")


plan.dataset.add_label(label_name='watch')
# Create a builder instance

annotation = dl.Annotation.new(item=plan.item)
# Span the annotation over 100 frames. Change this or use a different approach based on your context
for i_frame in range(557):
    i = i_frame % 270
    if i_frame >= 270:
        i = i_frame - (i_frame % 270)*2
    # go over 100 frame
    annotation.add_frame(annotation_definition=dl.Box(top=200 + 3 * i,
                                                      left=3 * (i_frame + 10),
                                                      bottom=280 + 3 * i,
                                                      right=3 *
                                                      (i_frame + 100),
                                                      label="watch"),
                         frame_num=i_frame,  # set the frame for the annotation
                         )
# upload to platform
annotation.upload()


# create annotation builder
builder = plan.item.annotations.builder()
for i_frame in range(100):
    # go over 100 frames
    for i_detection in range(10):
        # for each frame we have 10 different detections (location is just for the example)
        builder.add(annotation_definition=dl.Box(top=10 * i_frame,
                                                 left=50 * i_detection+10 * i_frame,
                                                 bottom=10 * i_frame + 40,
                                                 right=50 * i_detection + 40 + 10 * i_frame,
                                                 label="birds"),
                    # set the frame for the annotation
                    frame_num=i_frame,
                    # need to input the element id to create the connection between frames
                    object_id=i_detection + 1,
                    )
# Upload the annotations to platform
plan.item.annotations.upload(builder)
