SELECT people.name FROM people
INNER JOIN stars ON people.id = stars.person_id
INNER JOIN movies ON stars.movie_id = movies.id

WHERE
	stars.movie_id IN
	(
		SELECT stars.movie_id FROM stars
		INNER JOIN people ON stars.person_id = people.id
		WHERE people.name = "Kevin Bacon"
	);
