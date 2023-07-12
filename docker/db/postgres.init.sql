/* put database initialization script here */

-- for example
CREATE ROLE docker WITH ENCRYPTED PASSWORD 'docker' LOGIN;
COMMENT ON ROLE docker IS 'docker user for tests';

CREATE DATABASE docker OWNER docker;
COMMENT ON DATABASE docker IS 'docker db for tests owned by docker user';
