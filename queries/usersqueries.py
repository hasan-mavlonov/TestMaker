CREATE_USER = """
INSERT INTO users (full_name, password)
VALUES (%s, %s)
RETURNING id
"""

READ_USER_BY_NAME = """
SELECT * FROM users WHERE full_name = %s
"""

UPDATE_USER = """
UPDATE users
SET full_name = %s
WHERE full_name = %s
"""

DELETE_USER = """
DELETE FROM users
WHERE full_name = %s
"""

GET_PASSWORD = """
SELECT password FROM users WHERE full_name = %s
"""

GET_USER_ID = """
SELECT id FROM users WHERE full_name = %s
"""
