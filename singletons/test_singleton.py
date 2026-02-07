from singletons.config_manager import ConfigManager

config1 = ConfigManager()
config2 = ConfigManager()

print(f"Config1 Address: {id(config1)}")
print(f"Config2 Address: {id(config2)}")
print(f"Is config1 the same as config2? {config1 is config2}")
