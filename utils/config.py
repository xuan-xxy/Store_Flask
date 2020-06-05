# -*- coding: utf-8 -*-
#Auth:xuanxuan

import datetime
import time



def datetime_toTimestamp(dateTime = datetime.datetime.now()):
    return int(time.mktime(dateTime.timetuple()))






