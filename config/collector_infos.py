db_path = "/home/haojie/posixGEN/LwIP_HTTP_Server_Socket_RTOS/STM32CubeIDE/Release_1/DATABASE"
query_file = "temp_query.ql"
output_csv = "_output_infos/output.csv"
output_bqrs = "_output_infos/output.bqrs"
output_json = "_output_infos/output.json"

# common infos collector
function_collector_query_file = "codeql_scripts/info_function_collector.ql"
function_structure_query_file = ""
function_call_collector_query_file = "codeql_scripts/info_function_call_collector.ql"
struct_collector_query_file = "codeql_scripts/info_struct_collector.ql"
enum_collector_query_file = "codeql_scripts/info_enum_collector.ql"
file_collector_query_file = "codeql_scripts/info_file_collector.ql"

# mmio & driver infos collector
mmio_structure_query_file = ""
mmio_function_query_file = "codeql_scripts/info_mmio_function_collector.ql"
driver_function_query_file = "codeql_scripts/info_driver_function_collector.ql"
buffer_function_query_file = "codeql_scripts/info_buffer_function_collector.ql"