"""
——— Source ———
From the lecture
——— Purpose ———
Example of unpacking a list values
"""


def total(galleons, sickles, knuts):
	return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 10, 10]

print(total(*coins), "Knuts")
