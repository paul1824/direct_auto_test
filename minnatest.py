import common
from common import handle_config
package_id = "wdw"
payload = handle_config.sql_payload['gp_sql_tables']['gp_add_sql_table']
# payload1 = '{"fields":[],"operatorBeans":[],"paramSetting":[],"memorize":false,"initTime":0,"lastUpdateTime":0,"editable":false,"selected":0,"type":2,"engineType":0,"pack":"'+package_id+'","name":"合同事实表","sql":"0DWkpLqaCG5BozNbdl3UYYJZZMfxPzf3wLzBkAW9LXYc8osNpsGcavle+9IdFTI0","connectionName":"gp","operators":[],"transferName":"合同事实表"}'

print(payload.replace("'+package_id+'",package_id))