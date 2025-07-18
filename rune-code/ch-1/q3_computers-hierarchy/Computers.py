from abc import ABC, abstractmethod

class Computer(ABC):
    """Base class for all computer types."""
    def __init__(self,
                 cpu: str,
                 ram_gb: int,
                 storage_tb: float,
                 os: str):
        self.cpu = cpu
        self.ram_gb = ram_gb
        self.storage_tb = storage_tb
        self.os = os
        self.is_powered_on = False

    def power_on(self):
        if not self.is_powered_on:
            print(f"Booting {self.__class__.__name__} with {self.cpu}...")
            self.is_powered_on = True

    def power_off(self):
        if self.is_powered_on:
            print(f"Shutting down {self.__class__.__name__}...")
            self.is_powered_on = False

    def restart(self):
        self.power_off()
        self.power_on()

    @abstractmethod
    def info(self) -> str:
        """Return a one-line description."""
        ...

class Desktop(Computer):
    def info(self) -> str:
        return (f"Desktop(cpu={self.cpu}, ram={self.ram_gb}GB, "
                f"storage={self.storage_tb}TB, os={self.os})")

class Laptop(Computer):
    def __init__(self,
                 cpu: str,
                 ram_gb: int,
                 storage_tb: float,
                 os: str,
                 battery_capacity_mah: int):
        super().__init__(cpu, ram_gb, storage_tb, os)
        self.battery_capacity_mah = battery_capacity_mah
        self.battery_level = 100  # percent

    def charge(self, percent: int):
        self.battery_level = min(100, self.battery_level + percent)
        print(f"Charging laptop to {self.battery_level}%")

    def info(self) -> str:
        return (f"Laptop(cpu={self.cpu}, ram={self.ram_gb}GB, "
                f"storage={self.storage_tb}TB, os={self.os}, "
                f"battery={self.battery_capacity_mah}mAh)")

class Server(Computer):
    def __init__(self,
                 cpu: str,
                 ram_gb: int,
                 storage_tb: float,
                 os: str,
                 rack_units: int):
        super().__init__(cpu, ram_gb, storage_tb, os)
        self.rack_units = rack_units

    def allocate_resources(self, cpu_cores: int, ram_gb: int):
        print(f"Allocating {cpu_cores} cores and {ram_gb}GB RAM on server")

    def info(self) -> str:
        return (f"Server(cpu={self.cpu}, ram={self.ram_gb}GB, "
                f"storage={self.storage_tb}TB, os={self.os}, "
                f"rack_units={self.rack_units})")

class EmbeddedDevice(Computer):
    def __init__(self,
                 cpu: str,
                 ram_gb: int,
                 storage_tb: float,
                 os: str,
                 sensor_type: str):
        super().__init__(cpu, ram_gb, storage_tb, os)
        self.sensor_type = sensor_type

    def connect_sensor(self):
        print(f"Connecting {self.sensor_type} sensor")

    def info(self) -> str:
        return (f"EmbeddedDevice(cpu={self.cpu}, ram={self.ram_gb}GB, "
                f"storage={self.storage_tb}TB, os={self.os}, "
                f"sensor={self.sensor_type})")

# ── Example Usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    devices = [
        Desktop("Intel i5", 8, 1, "Windows 10"),
        Laptop("Intel i7", 16, 0.5, "Ubuntu 22.04", battery_capacity_mah=5000),
        Server("AMD EPYC", 128, 10, "CentOS 8", rack_units=2),
        EmbeddedDevice("ARM Cortex-M4", 1, 0.016, "FreeRTOS", sensor_type="temperature"),
    ]
    for d in devices:
        print(d.info())
        d.power_on()
        if isinstance(d, Laptop):
            d.charge(10)
        if isinstance(d, Server):
            d.allocate_resources(cpu_cores=8, ram_gb=32)
        if isinstance(d, EmbeddedDevice):
            d.connect_sensor()
        print()
