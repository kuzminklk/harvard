import pytest

from watch import parse


def test_parse():
	assert (
		parse(
			'<iframe width="560" height="315" src="https://www.youtube.com/embed/abc123" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
		)
		== "https://youtu.be/abc123"
	)
	assert (
		parse(
			'<iframe src="https://www.youtube.com/embed/def456" width="560" height="315" frameborder="0" allowfullscreen></iframe>'
		)
		== "https://youtu.be/def456"
	)
	assert (
		parse(
			'<iframe src="http://www.youtube.com/embed/ghi789" width="560" height="315" frameborder="0" allowfullscreen></iframe>'
		)
		== "https://youtu.be/ghi789"
	)
	assert (
		parse(
			'<iframe src="https://youtube.com/embed/jkl012" width="560" height="315" frameborder="0" allowfullscreen></iframe>'
		)
		== "https://youtu.be/jkl012"
	)


def test_not_parse_invalid():
	assert not parse('<ifsdffffdfframeborder="0" allowfullscreen></iframe>')
	assert not parse('<iframe src=aaaaasdasdqwe width="560" height="315" frameborder="0" allowfullscreen></iframe>')
