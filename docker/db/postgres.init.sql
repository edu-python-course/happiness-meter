/* put database initialization script here */

-- for example
CREATE ROLE happymeter WITH ENCRYPTED PASSWORD '.fq33$jXK@/ShVyN' LOGIN;
COMMENT ON ROLE happymeter IS 'happiness meter django application';

CREATE DATABASE happymeter OWNER happymeter;
COMMENT ON DATABASE happymeter IS 'happiness meter project database';
