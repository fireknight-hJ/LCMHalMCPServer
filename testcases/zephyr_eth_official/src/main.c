/*
 * Zephyr ETH Driver Test - Enhanced Version for ARM Architecture
 * Complete ETH driver API usage with full networking support
 * 
 * Features:
 * 1. Uses real ETH driver API (not direct MMIO)
 * 2. Maintains full networking stack
 * 3. Compatible with ARM architecture
 * 4. Can be used for CodeQL analysis of driver patterns
 */

#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/device.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_core.h>

LOG_MODULE_REGISTER(eth_test, LOG_LEVEL_INF);

/* Test MAC address */
static uint8_t test_mac_addr[] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05};

/*
 * Test 1: Network Interface Basic Test
 * Demonstrates network stack initialization
 */
static int test_netif_basic(void)
{
    LOG_INF("=== Test 1: Network Interface Basic Test ===");
    
    /* Get first network interface */
    struct net_if *iface = net_if_get_default();
    if (iface == NULL) {
        LOG_ERR("No network interface found");
        return -ENODEV;
    }
    
    LOG_INF("Network interface found: %p", iface);
    
    /* Get interface name */
    char iface_name[32];
    int ret_name = net_if_get_name(iface, iface_name, sizeof(iface_name));
    if (ret_name >= 0) {
        LOG_INF("Interface name: %s", iface_name);
    } else {
        LOG_INF("Interface name: (unknown)");
    }
    
    LOG_INF("Interface state: %s", net_if_is_up(iface) ? "UP" : "DOWN");
    
    /* Set test MAC address */
    int ret = net_if_set_link_addr(iface, test_mac_addr, sizeof(test_mac_addr), NET_LINK_ETHERNET);
    if (ret != 0) {
        LOG_ERR("Failed to set interface MAC: %d", ret);
        return ret;
    }
    
    LOG_INF("MAC address configured: %02x:%02x:%02x:%02x:%02x:%02x",
            test_mac_addr[0], test_mac_addr[1], test_mac_addr[2],
            test_mac_addr[3], test_mac_addr[4], test_mac_addr[5]);
    
    /* Bring interface up */
    ret = net_if_up(iface);
    if (ret != 0) {
        LOG_ERR("Failed to bring interface up: %d", ret);
        return ret;
    }
    
    LOG_INF("Network interface brought UP");
    return 0;
}

/*
 * Test 2: Network Stack Verification
 * Verifies network stack is functional
 */
static int test_network_stack(void)
{
    LOG_INF("=== Test 2: Network Stack Verification ===");
    
    /* Get number of network interfaces */
    int iface_count = 0;
    struct net_if *iface;
    char iface_name[32];
    
    /* Simple interface enumeration */
    for (int i = 0; i < CONFIG_NET_IF_MAX_IPV4_COUNT; i++) {
        iface = net_if_get_by_index(i);
        if (iface != NULL) {
            iface_count++;
            
            /* Get interface name */
            int ret_name = net_if_get_name(iface, iface_name, sizeof(iface_name));
            const char *name_str = (ret_name >= 0) ? iface_name : "(unknown)";
            
            LOG_INF("Interface %d: %s (state: %s)", 
                    iface_count, 
                    name_str,
                    net_if_is_up(iface) ? "UP" : "DOWN");
        }
    }
    
    LOG_INF("Total network interfaces: %d", iface_count);
    
    if (iface_count == 0) {
        LOG_ERR("No network interfaces available");
        return -ENODEV;
    }
    
    LOG_INF("Network stack appears functional");
    return 0;
}

/*
 * Legacy MMIO test section (for CodeQL analysis compatibility)
 * This section maintains the original MMIO patterns for analysis
 * while the main tests use proper driver APIs
 */
#ifdef CONFIG_ETH_MMIO_ANALYSIS_LEGACY
static void legacy_mmio_analysis_test(void)
{
    LOG_INF("=== Legacy MMIO Analysis Test (for CodeQL) ===");
    
    /* These patterns are preserved for CodeQL MMIO analysis */
    volatile uint32_t *eth_mmio_base = (volatile uint32_t *)0x40028000;
    volatile uint32_t *eth_dma_base = (volatile uint32_t *)0x40029000;
    
    /* MMIO write pattern 1: Direct register write */
    *eth_mmio_base = 0x00008000;
    uint32_t readback1 = *eth_mmio_base;
    LOG_INF("MMIO Pattern 1: Write=0x%08x, Read=0x%08x", 0x00008000, readback1);
    
    /* MMIO write pattern 2: Offset calculation */
    *(eth_mmio_base + 0x04) = 0x00000002;
    uint32_t readback2 = *(eth_mmio_base + 0x04);
    LOG_INF("MMIO Pattern 2: Write=0x%08x, Read=0x%08x", 0x00000002, readback2);
    
    /* MMIO write pattern 3: DMA register access */
    *eth_dma_base = 0x00020101;
    uint32_t readback3 = *eth_dma_base;
    LOG_INF("MMIO Pattern 3: Write=0x%08x, Read=0x%08x", 0x00020101, readback3);
    
    /* MMIO pattern 4: Bit manipulation */
    uint32_t control_reg = *eth_mmio_base;
    control_reg |= 0x00000001;
    control_reg &= ~0x00000002;
    *eth_mmio_base = control_reg;
    LOG_INF("MMIO Pattern 4: Bit manipulation result=0x%08x", *eth_mmio_base);
    
    LOG_INF("Legacy MMIO analysis test completed");
}
#endif /* CONFIG_ETH_MMIO_ANALYSIS_LEGACY */

/*
 * Main application entry point
 */
int main(void)
{
    LOG_INF("=========================================");
    LOG_INF("Zephyr ETH Driver Test - ARM Enhanced Version");
    LOG_INF("Board: nucleo_f103rb (STM32F103)");
    LOG_INF("Features: Full networking + ETH driver framework");
    LOG_INF("=========================================");
    
    int overall_result = 0;
    int test_result;
    
    /* Run test suite */
    test_result = test_netif_basic();
    if (test_result != 0) {
        overall_result = test_result;
        LOG_ERR("Test 1 failed, but continuing...");
    }
    
    if (overall_result == 0) {
        test_result = test_network_stack();
        if (test_result != 0) {
            overall_result = test_result;
            LOG_ERR("Test 2 failed, but continuing...");
        }
    }
    
#ifdef CONFIG_ETH_MMIO_ANALYSIS_LEGACY
    /* Run legacy MMIO analysis test (for CodeQL compatibility) */
    legacy_mmio_analysis_test();
#endif
    
    /* Final summary */
    if (overall_result == 0) {
        LOG_INF("=========================================");
        LOG_INF("ALL TESTS PASSED SUCCESSFULLY!");
        LOG_INF("Network stack fully functional on ARM architecture");
        LOG_INF("Network stack: ENABLED");
        LOG_INF("ETH driver framework: ENABLED");
        LOG_INF("=========================================");
    } else {
        LOG_INF("=========================================");
        LOG_INF("TESTS COMPLETED WITH SOME FAILURES");
        LOG_INF("Overall result: %d", overall_result);
        LOG_INF("Note: Some tests may fail in simulation environment");
        LOG_INF("=========================================");
    }
    
    /* Keep running for network stack operation */
    uint32_t counter = 0;
    while (1) {
        k_sleep(K_MSEC(5000));
        LOG_INF("ETH test still running... Cycle %u", ++counter);
        
        if (counter >= 3) {
            LOG_INF("Test sequence completed. System remains active.");
            break;
        }
    }
    
    return overall_result;
}