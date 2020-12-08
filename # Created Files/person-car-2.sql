create table car (
	car_uuid UUID NOT NULL PRIMARY KEY,
	make VARCHAR(100) NOT NULL,
	model VARCHAR(100) NOT NULL,
	price NUMERIC(19, 2) NOT NULL CHECK (price > 0)
);


-- INSERT INTO CAR
insert into car (car_uuid, make, model, price) values (uuid_generate_v4(), 'Land Rover', 'Sterling', '87665.38');
insert into car (car_uuid, make, model, price) values (uuid_generate_v4(), 'GMC', 'Acadia', '17662.69');



create table person (
    person_uuid UUID NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	gender VARCHAR(7) NOT NULL,
	email VARCHAR(100),
	date_of_birth DATE NOT NULL,
	country_of_birth VARCHAR(50) NOT NULL,
	car_uuid UUID REFERENCES car(car_uuid),
	UNIQUE(car_uuid),
	UNIQUE(email)
);


-- INSERT INTO PERSON
insert into person (person_uuid, first_name, last_name, gender, email, date_of_birth, country_of_birth)
values (uuid_generate_v4(), 'Fernanda', 'Beardon', 'Female', 'fernandab@is.gd', '1953-10-28', 'Comoros');

insert into person (person_uuid, first_name, last_name, gender, email, date_of_birth, country_of_birth) 
values (uuid_generate_v4(), 'Omar', 'Colmore', 'Male', null, '1921-04-03', 'Finland');

insert into person (person_uuid, first_name, last_name, gender, email, date_of_birth, country_of_birth) 
values (uuid_generate_v4(), 'Adriana', 'Matuschek', 'Female', 'amatuschek2@feedburner.com', '1965-02-28', 'Cameroon');