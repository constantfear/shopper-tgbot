BEGIN;


CREATE TABLE IF NOT EXISTS public.users
(
    user_id integer NOT NULL,
    "Name" character varying COLLATE pg_catalog."default" NOT NULL,
    tg_user_id integer NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS public.orders
(
    order_id integer NOT NULL,
    user_id integer NOT NULL,
    date date,
    adress character varying,
    phone character varying,
    order_status integer,
    PRIMARY KEY (order_id)
);

CREATE TABLE IF NOT EXISTS public.status
(
    status_id integer,
    status_name character varying,
    PRIMARY KEY (status_id)
);

CREATE TABLE IF NOT EXISTS public.order_list
(
    id integer NOT NULL,
    order_id integer NOT NULL,
    product_id integer NOT NULL,
    amount integer NOT NULL,
    total_price integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.products
(
    product_id integer NOT NULL,
    name character varying NOT NULL,
    img character varying NOT NULL,
    description text,
    price integer NOT NULL,
    product_type integer NOT NULL,
    PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS public.type
(
    type_id integer NOT NULL,
    type_name character varying NOT NULL,
    PRIMARY KEY (type_id)
);

ALTER TABLE IF EXISTS public.orders
    ADD FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.orders
    ADD FOREIGN KEY (order_status)
    REFERENCES public.status (status_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.order_list
    ADD FOREIGN KEY (order_id)
    REFERENCES public.orders (order_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.order_list
    ADD FOREIGN KEY (product_id)
    REFERENCES public.products (product_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.products
    ADD FOREIGN KEY (product_type)
    REFERENCES public.type (type_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


END;