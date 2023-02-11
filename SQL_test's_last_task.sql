SET sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

create temporary table laikina
(select a.actor_id, a.first_name, a.last_name, sum(p.amount) as suma,
case
when i.store_id = 1 then 'Shop_1'
else 'Shop_2'
end as Rental_shop
from payment as p
join rental as r
on r.rental_id = p.rental_id
join inventory as i
on i.inventory_id = r.inventory_id
join film_actor as fa
on fa.film_id = i.film_id
join actor as a
on a.actor_id = fa.actor_id
group by a.actor_id, i.store_id, Rental_shop);


create temporary table Temp_parduotuve1
select actor_id, first_name, last_name, Rental_shop, max(suma) as incomes
from laikina
as parde_1
where Rental_shop = 'Shop_1';


create temporary table Temp_parduotuve2
select actor_id, first_name, last_name, Rental_shop, max(suma) as incomes
from laikina
where Rental_shop = 'Shop_2';

select * from Temp_parduotuve1
union
select * from Temp_parduotuve2;

/* OR */


select  "pirma" as "parduotuve", actor_id, first_name, last_name, (total_income) from (
    select a.actor_id, a.first_name, a.last_name, sum(amount) total_income from payment p
    join rental r
    on r.rental_id = p.rental_id
    join inventory i
    on i.inventory_id = r.inventory_id
    join store s
    on s.store_id = i.store_id
    -- join film f
    -- on i.film_id = f.film_id
    join film_actor fa
    on i.film_id = fa.film_id
    join actor a
    on fa.actor_id = a.actor_id
    group by a.actor_id, s.store_id
    having s.store_id = 1
    order by sum(amount) desc
    limit 1
) as table2
union
select  "antra", actor_id, first_name, last_name, (total_income) from (
    select a.actor_id, a.first_name, a.last_name, sum(amount) total_income from payment p
    join rental r
    on r.rental_id = p.rental_id
    join inventory i
    on i.inventory_id = r.inventory_id
    join store s
    on s.store_id = i.store_id
    -- join film f
    -- on i.film_id = f.film_id
    join film_actor fa
    on i.film_id = fa.film_id
    join actor a
    on fa.actor_id = a.actor_id
    group by a.actor_id, s.store_id
    having s.store_id = 2
    order by sum(amount) desc
    limit 1
) as table2;