# ?? System Bootstrap Entry
from control.harmony.harmony_core import start_harmony

if __name__ == "__main__":
    status = start_harmony()
    print(f"System status: {status}")
