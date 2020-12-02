CREATE TABLE public.gebruikers (
	gebruiker_id serial NOT NULL,
	user_email bpchar(50) NOT NULL,
	hash varchar(94) NOT NULL,
	role_id int4 NOT NULL
);

CREATE TABLE public.reviews (
	review_id serial NOT NULL,
	user_name bpchar(50) NOT NULL,
	user_review bpchar(140) NULL,
	user_consent bool NULL,
	review_date date NOT NULL DEFAULT CURRENT_DATE,
	review_time time(0) NOT NULL DEFAULT CURRENT_TIME,
	mod_id int4 NULL,
	mod_comment varchar(244) NULL,
	mod_review_date date NULL,
	mod_review_time time(0) NULL,
	mod_approval bool NULL,
	tweeted bool NULL,
	CONSTRAINT reviews_pkey PRIMARY KEY (review_id)
);
