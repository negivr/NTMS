import os
from PIL import Image
from time import time
from django.conf import settings


def get_uploaded_cdl_file_name(instance, filename):
    print(filename)
    print(instance.img.path)
    filename_ext = os.path.splitext(filename)[1]
    dob_name = str(instance.person.dob)
    time_issue_name = str(instance.date_issue)
    time_name = str(time()).replace(".", "_")
    driver_name = f"{instance.person.first_name}_{instance.person.last_name}"
    driver_name_dob = f"{driver_name}_{dob_name}"
    directory = os.path.join(settings.MEDIA_ROOT, "cdls", driver_name_dob)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # if not filename_ext == ".pdf":
    #     im = Image.open(filename)
    #     if im.mode == "RGBA":
    #         im = im.convert("RGB")
    #         filename_ext = ".pdf"
    #         temp_file =

    f_name = f"{driver_name}_CDL_{time_issue_name}_{time_name}{filename_ext}"
    path = os.path.join("cdls", driver_name_dob, f_name)

    return path
