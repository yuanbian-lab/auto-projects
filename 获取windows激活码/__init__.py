# -*- coding=utf-8 -*-
import time
from get_active_code import get_kms_keys


keys = get_kms_keys()
for system, key in keys:
    print("system:", system, "key:", key)
    time.sleep(0.5)