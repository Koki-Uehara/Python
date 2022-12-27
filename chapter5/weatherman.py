import report
description = report.get_description()
print("today's weather : ", description)

from report import get_descriptiont
description = get_descriptiont()
print("today's weather : ", description)

from report import get_description as do_it
description = do_it()
print("today's weather : ", description)

# 上記はすべて同様に動作する。
# 必要なものだけをインポートする。