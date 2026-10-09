from datetime import date

from seasons import convert


def test_convert():
	today = date.fromisoformat("2026-10-05")
	birth_date = date.fromisoformat("1999-01-01")
	difference = today - birth_date

	assert convert(difference) == "Fourteen Million, Six Hundred Thousand, One Hundred And Sixty"
