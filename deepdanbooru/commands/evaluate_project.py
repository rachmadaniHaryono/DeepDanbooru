import os

import deepdanbooru as dd


def evaluate_project(project_path, target_path, threshold):
    if not os.path.exists(target_path):
        raise Exception(f'Target path {target_path} is not exists.')

    if os.path.isfile(target_path):
        taget_image_paths = [target_path]

    else:
        patterns = [
            '*.[Pp][Nn][Gg]',
            '*.[Jj][Pp][Gg]',
            '*.[Jj][Pp][Ee][Gg]',
            '*.[Gg][Ii][Ff]'
        ]

        taget_image_paths = dd.io.get_file_paths_in_directory(
            target_path, patterns)

        taget_image_paths = dd.extra.natural_sorted(taget_image_paths)

    project_context, model, tags = dd.project.load_project(project_path)

    width = project_context['image_width']
    height = project_context['image_height']

    for image_path in taget_image_paths:
        print(f'Tags of {image_path}:')
        for tag, score in dd.redistribution.evaluate_image(
                image_path, model, tags, threshold, width, height):
            print(f'({score:05.3f}) {tag}')

        print()
