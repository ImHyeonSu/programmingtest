-- SELECT
--     Sub.name
-- FROM
--     (
--         SELECT
--             SalesPerson.sales_id,
--             SalesPerson.name,
--             orders.com_id
--         FROM
--             SalesPerson
--             LEFT JOIN Orders ON SalesPerson.sales_id = Orders.sales_id
--     ) AS Sub
--     LEFT JOIN Company ON Sub.com_id = Company.com_id
-- GROUP BY
--     Sub.sales_id
-- HAVING
--     SUM(
--         CASE
--             WHEN Company.name = 'RED' THEN 1
--             ELSE 0
--         END
--     ) = 0;

SELECT
    Sub.name
FROM
    SalesPerson AS Sub
    LEFT JOIN Orders ON Sub.sales_id = Orders.sales_id
    LEFT JOIN Company ON Orders.com_id = Company.com_id
GROUP BY
    Sub.sales_id, Sub.name
HAVING
    SUM(CASE WHEN Company.name = 'RED' THEN 1 ELSE 0 END) = 0;