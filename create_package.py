
import dtlpy as dl

package_name = "image-processing"
project_name = "images-one"
project = dl.projects.get(project_name=project_name)

modules = [dl.PackageModule(
    name=package_name,
    entry_point='main.py',
    functions=[
        dl.PackageFunction(
            name='add_classification',
            inputs=[
                dl.FunctionIO(name='item', type=dl.PackageInputType.ITEM),
            ],
            outputs=[
                dl.FunctionIO(name='items', type=dl.PackageInputType.ITEMS)
            ],
            description='adds a classification to the item'
        )
    ]
)]

package = project.packages.push(package_name=package_name, modules=modules, src_path='./functions/add_annotation_to_item')
print('New Package has been deployed')
