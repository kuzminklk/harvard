"""
——— Source ———
From the shorts
——— Behavior ———
Prints spacecraft report
——— Purpose ———
Example of dictionaries methods (“get(), update()”)
"""

spacecrafts = [
	{"name": "Voyager 1", "distance": "161 AU"},
	{"name": "James Webb Space Telescope", "distance": "0.01 AU", "orbit": "Sun"},
]


def main():
	spacecrafts[1].update({"distance": "0.011 AU"})  # Update for example
	for spacecraft in spacecrafts:
		print(make_report(spacecraft))


def make_report(spacecraft):
	return f"""
————————— Report —————————
Name: {spacecraft.get("name", "Unknown")}
Distance: {spacecraft.get("distance", "Unknown")}
Orbit: {spacecraft.get("orbit", "Unknown")}
"""


main()
