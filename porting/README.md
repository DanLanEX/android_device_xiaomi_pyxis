# Experimental Android 16 port (pyxis)

This branch starts from LineageOS `lineage-22.2` and targets `lineage-23.2` with the **existing Linux 4.9 kernel**. It is not ready to compile or flash.

## Run source preflight

From an initialized Android checkout:

```bash
python3 device/xiaomi/pyxis/porting/check_source.py .
```

To additionally require extracted proprietary files:

```bash
python3 device/xiaomi/pyxis/porting/check_source.py . --require-vendor
```

The script is read-only; it checks a small set of required paths, **not** whether those paths provide valid modules or Android 16-compatible HAL implementations. Missing `hardware/qcom-caf/*` and `device/qcom/sepolicy_vndr` entries require properly sourced projects, not dummy empty folders.

The original `lineage-22.2` branch remains unchanged. Build compatibility and real-device hardware behavior are pending verification. Do not flash untested images.
