CREATE TABLE ch_file_upload ( 
id serial PRIMARY KEY, 
facility_id integer,
file_name VARCHAR(50) NOT NULL,
date_uploaded timestamp with time zone NOT NULL, 
uploaded_by VARCHAR(20) NOT NULL DEFAULT 'SCRIPT',
date_completed timestamp with time zone NULL,
version VARCHAR(10) NULL,
status ch_file_status default 'pending'
);
