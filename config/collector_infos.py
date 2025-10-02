db_path = "/home/haojie/posixGEN/LwIP_HTTP_Server_Socket_RTOS/STM32CubeIDE/Release_1/DATABASE"
query_file = "temp_query.ql"
# temperary output files
output_csv = "tmp/common_info.csv"
output_bqrs = "tmp/common_info.bqrs"
output_json = "tmp/common_info.json"

# common infos collector
function_collector_query_file = "queries/collectors/common/info_function_collector.ql"
function_structure_query_file = ""
function_call_collector_query_file = "queries/collectors/common/info_function_call_collector.ql"
struct_collector_query_file = "queries/collectors/common/info_struct_collector.ql"
enum_collector_query_file = "queries/collectors/common/info_enum_collector.ql"
file_collector_query_file = "queries/collectors/common/info_file_collector.ql"

# mmio & driver infos collector
mmio_structure_query_file = ""
mmio_function_query_file = "queries/collectors/mmio/info_mmio_function_collector.ql"
driver_function_query_file = "queries/collectors/mmio/info_driver_function_collector.ql"
buffer_function_query_file = "queries/collectors/mmio/info_buffer_function_collector.ql"

# driver info collector
driverfrom_function_query_file = "queries/collectors/driver/driver_info_driverfromfunction_collector.ql"     # 给大模型处理
driverfrom_expr_query_file = "queries/collectors/driver/driver_info_driverfromexpr_collector.ql"
driverfrom_function_contains_query_file = "queries/collectors/driver/driver_info_driverfromfunctioncontains_collector.ql"
driverto_functioncall_query_file = "queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql"

# deprecated
driverfrom_functioncall_query_file = "" # noReturnValue的直接注释掉，hasReturnValue的考虑返回值该是什么
driverusing_file_query_file = ""        # 这些是理论上的所有待处理文件（除了部分内核Asm内容）
cross_function_query_file = ""          # 
driverfrom_globalvar_query_file = ""    # 全部注释掉
