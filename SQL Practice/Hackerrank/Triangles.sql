/*
The user inputs 3 values representing side lengths, and the query must determine which type of triangle it is.
That is, if it is a triangle at all.
*/

SELECT CASE
    WHEN A >= B + C OR B >= A + C OR C >= A + B THEN 'Not A Triangle'
    WHEN A = B AND B = C THEN 'Equilateral'
    WHEN A = B OR B = C OR A = C THEN 'Isosceles'
    WHEN A<>B AND A<>C AND B<>C THEN 'Scalene'
END
FROM TRIANGLES;
