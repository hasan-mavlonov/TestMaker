CREATE_TEST = """
INSERT INTO tests (user_id, name, status)
VALUES (%s, %s, %s)
RETURNING id
"""