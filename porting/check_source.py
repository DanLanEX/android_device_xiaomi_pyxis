#!/usr/bin/env python3
"""Read-only pyxis Android 16 source-tree preflight. Run from any cwd."""
import argparse
from pathlib import Path
import sys

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_root", type=Path, help="Android checkout root")
    parser.add_argument("--require-vendor", action="store_true", help="Fail when proprietary blobs are not yet extracted")
    args = parser.parse_args()
    root = args.source_root.resolve()
    required = {
        "device/xiaomi/pyxis/BoardConfig.mk": "pyxis configuration",
        "device/xiaomi/sdm710-common/BoardConfigCommon.mk": "SDM710 shared configuration",
        "kernel/xiaomi/sdm710/Makefile": "existing Linux 4.9 kernel",
        "hardware/xiaomi": "Xiaomi hardware modules",
        "hardware/qcom-caf/common/common.mk": "Qualcomm CAF common framework",
        "hardware/qcom-caf/sdm845/audio": "legacy Qualcomm audio HAL",
        "hardware/qcom-caf/sdm845/display": "legacy Qualcomm display HAL",
        "hardware/qcom-caf/sdm845/media": "legacy Qualcomm media HAL",
        "device/qcom/sepolicy/SEPolicy.mk": "Qualcomm platform SELinux policy",
        "device/qcom/sepolicy_vndr/legacy-um/SEPolicy.mk": "Qualcomm legacy vendor SELinux policy",
        "hardware/qcom-caf/wlan": "Qualcomm CAF WLAN module namespace",
        "vendor/qcom/opensource/usb/etc": "Qualcomm USB settings",
        "vendor/qcom/opensource/dataservices": "Qualcomm data services",
        "vendor/qcom/opensource/display": "Qualcomm display compatibility source",
        "vendor/qcom/opensource/commonsys/display": "Qualcomm commonsys display",
        "vendor/qcom/opensource/commonsys-intf/display": "Qualcomm commonsys display interfaces",
    }
    missing = []
    for rel, label in required.items():
        exists = (root / rel).exists()
        print(f"{'OK' if exists else 'MISSING'} {rel} ({label})")
        if not exists:
            missing.append(rel)
    for rel in ("vendor/xiaomi/pyxis/BoardConfigVendor.mk",
                "vendor/xiaomi/sdm710-common/BoardConfigVendor.mk"):
        exists = (root / rel).exists()
        print(f"{'OK' if exists else 'NOT EXTRACTED'} {rel} (proprietary vendor input)")
        if args.require_vendor and not exists:
            missing.append(rel)
    if missing:
        print("\nSource checkout incomplete. Resolve paths without replacing the legacy kernel.", file=sys.stderr)
        return 1
    print("\nSource paths present. This does NOT establish Android 16 build compatibility.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
