-- ACTION SUBJECT id OPTIONS

-- DDL Commands / DATABASE
DROP DATABASE e_shop_l2_v2
CREATE DATABASE e_shop_l2_v2

create table products(
    id SERIAL PRIMARY KEY,
    name character varying(30)
);

create table money(
    amount integer,
    currency character varying(3),
    product_id integer,
    constraint money_product_fk 
        foreign key (product_id)
        references products(id)
);
--ALTER
drop table products;

 alter table money 
 add constraint money_product_fk 
 foreign key (product_id)
 references products(id);

--DML COMMANDS / DATA
--CRUD
---------------------------------------------

insert into products (name) VALUES ('Mac Book Air');
insert into products (name) VALUES ('iPhone XX');
select * from products;

insert into money VALUES (2000, 'USD', 3);
insert into money VALUES (4000, 'USD', 2);
insert into money VALUES (10000, 'USD', 10);



 update products set price=1050 where id=1;

 delete from products where id =3;

select products.id, products.name, money.amount, money.currency from
products join 
money on money.product_id =products.id;

--data visual representation
select products.id, products.name, floor(money.amount/1.2) as "ammount", 'EUR' as "currency" from
products join 
money on money.product_id =products.id;


--ADVANCED UPDATE / DELETE
-- +10% price, price < 3000

UPDATE money SET amount = amount *1.1 where amount <3000;


-- Remove the price for 'MacBook Air'
delete from money
using products
where products.name = 'Mac Book Air';



