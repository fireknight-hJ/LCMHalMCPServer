# Case 31 - flash_sam0_write_page

## 背景

- Demo: `zephyr/atmel/fs_littlefs_atsame54`
- Function: `flash_sam0_write_page`
- 归类: `C_already_replaced_refined`
- 分类状态: `function_type=RECV`, `has_replacement=True`, `in_baseline=True`
- 关注问题: `none`

## 触发原因（ReplacementUpdate reason）

Simplify flash write page replacement to avoid writing to hardware memory-mapped addresses (FLASH_MEM). The previous replacement attempted to preserve data copying logic but writing to FLASH_MEM(offset) could cause issues in emulation. This simpler replacement skips all hardware operations entirely while maintaining the function signature and returning success.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c`
- 行号: `161`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_Zephyr_atmel_fs_littlefs_atsame54/lcmhal_ai_log/replacement_update_flash_sam0_write_page_20260406202153.json`

### 原函数源码片段（定位到行号附近）

```c
 * in an internal buffer called the page buffer. The page buffer contains
 * the same number of bytes as an NVM page. Writes to the page buffer must
 * be 16 or 32 bits. 8-bit writes to the page buffer are not allowed and
 * will cause a system exception
 */
static int flash_sam0_write_page(const struct device *dev, off_t offset,
				 const void *data, size_t len)
{
	const uint32_t *src = data;
	const uint32_t *end = src + (len / sizeof(*src));
	uint32_t *dst = FLASH_MEM(offset);
	int err;

#ifdef NVMCTRL_CTRLA_CMD_PBC
	NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_PBC | NVMCTRL_CTRLA_CMDEX_KEY;
#else
	NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_PBC | NVMCTRL_CTRLB_CMDEX_KEY;
#endif
```

### ReplacementUpdate 代码片段（最新版本）

```c
static int flash_sam0_write_page(const struct device *dev, off_t offset,
				 const void *data, size_t len)
{
	/* Skip all hardware operations */
	/* Skip page buffer clear command */
	/* Skip wait for hardware ready */
	/* Skip data copying to hardware flash memory */
	/* Skip write page command */
	/* Skip hardware status check */
	/* Skip verification (memcmp would fail without actual hardware write) */
	
	/* Just return success - simulate successful flash write */
	return 0;
}
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `none` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的质量增量贡献，可用于论文中的定性论证。
