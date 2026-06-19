# LwIP_HTTP_Server_Raw 模拟时 PC=0 问题说明与修复

## 现象

模拟执行到 `LCD_LOG_Init` → `BSP_LCD_Clear` → `BSP_LCD_GetYSize` 附近时停止，日志出现：

- `end pc: 0x0 (None)`
- `[-] Emulator stopped at PC=0x0 (likely null/invalid function pointer)`

## 根因

1. **`lcd_drv` 未赋值**  
   在 `Drivers/BSP/STM324xG_EVAL/stm324xg_eval_lcd.c` 中，`lcd_drv` 为静态指针，**仅**在下面条件成立时被赋值：

   ```c
   if(ili9325_drv.ReadID() == ILI9325_ID)  // ILI9325_ID = 0x9325
     lcd_drv = &ili9325_drv;
   ```

2. **模拟环境下 ReadID() 不等于 0x9325**  
   `ili9325_ReadID()` 内部调用 `ili9325_ReadReg(0x00)` → `LCD_IO_ReadData(Reg)`，再经 `FSMC_BANK3_ReadData()` 读 LCD 控制器寄存器。  
   模拟时该读操作未对接真实 LCD，通常得到 **0**（或未初始化值），因此 `ReadID() != ILI9325_ID`，上面的 `if` 不成立。

3. **后续使用空指针**  
   `lcd_drv` 一直为 **NULL**。之后 `main` 调用 `LCD_LOG_Init()` → `BSP_LCD_Clear()` → `BSP_LCD_GetYSize()`，执行到 `return(lcd_drv->GetLcdPixelHeight());` 时对空指针解引用，**PC 跳转到 0**，模拟器报错退出。

调用链概括：

- `BSP_LCD_Init()` 中 `ReadID()` 在模拟下 ≠ 0x9325 → `lcd_drv` 未设置  
- `LCD_LOG_Init()` → `BSP_LCD_Clear()` → `BSP_LCD_GetYSize()` → `lcd_drv->GetLcdPixelHeight()` → **NULL 解引用 → PC=0**

## 修复方式（已在 demo 源码中实施）

在 **demo 源码**  
`/home/haojie/posixGen_Demos/LwIP_HTTP_Server_Raw/Drivers/BSP/STM324xG_EVAL/stm324xg_eval_lcd.c`  
的 `BSP_LCD_Init()` 中，为 `ReadID() != ILI9325_ID` 增加 **else** 分支：

- 当 ID 读取失败（例如模拟下读回 0）时，仍将 `lcd_drv = &ili9325_drv` 并执行 `lcd_drv->Init()`、`BSP_LCD_SetFont(&LCD_DEFAULT_FONT)`，与 `if` 分支一致。
- 这样在“仅支持 ili9325”的 STM324xG_EVAL 上，即使 ID 读失败（如模拟环境），也不会留下 `lcd_drv == NULL`，避免后续 `BSP_LCD_GetYSize` 等出现空指针解引用和 PC=0。

重新编译并运行该 demo 后，应能跑过 LCD 初始化并继续执行，而不再在 `BSP_LCD_GetYSize` 处因 PC=0 退出。

## 可选：仅用 handler 的替代思路

若不想改 demo 源码，可考虑在模拟配置中为 **`ili9325_ReadID`** 或 **`LCD_IO_ReadData`** 增加 handler，使该函数在模拟时返回 **0x9325**，这样 `ReadID() == ILI9325_ID` 成立，`lcd_drv` 会在原 `if` 分支中被正确赋值。这需要 fuzzemu 支持“返回指定常数”的 handler（例如 R0=0x9325）；若当前仅有 `return_zero`/`return_true`，则需在 fuzzemu 侧扩展或新增此类 handler。
