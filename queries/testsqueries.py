CREATE_TEST = """
INSERT INTO tests (user_id, name, status)
VALUES (%s, %s, %s)
RETURNING id
"""
READ_ALL_TESTS = """
SELECT name FROM tests 
"""

READ_USER_TEST = """
SELECT name FROM tests WHERE user_id = %s
"""

UPDATE_TEST = """
UPDATE tests
SET name = %s
WHERE name = %s
"""

DELETE_TEST = """
DELETE FROM tests
WHERE name = %s
"""